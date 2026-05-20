#!/usr/bin/env python3
"""
fetch_wikipedia_images.py

Scans content pages in 02_Foundations .. 12_Frontier-Maps, finds matching
Wikipedia articles, downloads 1-3 relevant images per page from Wikimedia
Commons, and embeds them in a `### From Wikipedia` subsection under
`## Visuals`. Idempotent: re-running skips pages already processed.

Per CLAUDE.md §5.11 we never auto-commit. Per §5.1 raw/ is untouched.
We do NOT replace existing authored SVGs or mermaid blocks — Wikipedia
images are *added alongside* them.

Per the user's direct instruction we skip the license-verification step in
visual-pipeline-runbook.md §4 — Commons content is overwhelmingly free-
licensed; per-image attribution is captured in the source URL we embed.

Output:
  - images written to `_attachments/<NN_Folder>/<page-slug>--<descriptor>.<ext>`
  - pages edited in place (only the `## Visuals` section)
  - progress logged to `.state/wiki-image-fetch.tsv` (resumable)
"""

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

VAULT = Path("/Users/nickma/Develop/My2ndBrain/A-Level/Physics")
ATTACHMENTS = VAULT / "_attachments"
LOG_PATH = VAULT / ".state" / "wiki-image-fetch.tsv"
USER_AGENT = (
    "A-Level-Physics-Vault/1.0 "
    "(https://github.com/; educational personal use) Python/urllib"
)
API_BASE = "https://en.wikipedia.org/w/api.php"

FOLDERS = [
    "02_Foundations",
    "03_Physical-Quantities",
    "04_Concepts",
    "05_Laws-and-Results",
    "06_Models",
    "07_Methods",
    "08_Representations",
    "09_Experiments-and-Practicals",
    "10_Applications",
    "11_Problems",
    "12_Frontier-Maps",
]

# Page types where a real-world image rarely helps (kept conservative).
SKIP_TYPES = {"method", "problem-type", "worked-example", "mistake-pattern"}

# Filename patterns to reject (icons, ui chrome, audio).
REJECT_FILENAME_PATTERNS = [
    r"commons-logo", r"edit[-_]?icon", r"wiki(media|pedia)[-_]?logo",
    r"\bambox\b", r"\bicon[-_ ]", r"\bflag of\b", r"\bred[ _-]?pen\b",
    r"speaker[-_]?icon", r"sound[-_]?icon", r"loudspeaker",
    r"\.ogg$", r"\.ogv$", r"\.webm$", r"\.mid$", r"\.wav$",
    r"\bcrystal[-_ ]", r"folder[-_]?icon", r"question[-_]?mark",
    r"info[-_]?icon", r"wikiquote", r"\bpadlock\b", r"semi[-_]?protection",
    r"\btranslation[-_]?arrow", r"magnify[-_]?clip",
    r"^featured\b", r"^symbol[-_ ]", r"^p[-_]?physics", r"^p[-_]?history",
    r"^office\b", r"^scale[-_]of[-_]justice", r"\bdisambig\b",
    r"^stub[-_]?icon", r"^arrow", r"^smiley", r"^searchtool",
    r"^cscr-?featured", r"^wiktionary", r"question[-_ ]?book",
    r"pd[-_]?icon", r"\bsymbol\b", r"text[-_ ]?document", r"oojs[-_]?ui",
    r"^p[-_]?vip", r"^p_history", r"^p_culture", r"^p_religion",
    r"^p_psi", r"^p_philosophy", r"^p_law", r"^p_art",
    r"^nuvola[-_ ]", r"^infosym", r"text-x-generic",
    r"merge-arrow", r"split-arrow", r"\barbcom",
]
REJECT_RE = re.compile("|".join(REJECT_FILENAME_PATTERNS), re.IGNORECASE)

ALLOWED_EXT_RE = re.compile(r"\.(svg|png|jpe?g|gif|webp)$", re.IGNORECASE)


# --------------------------- HTTP helpers ---------------------------

_last_request_ts = [0.0]
_MIN_INTERVAL = 0.6  # politeness: ~1.6 req/s


def http_get(url, params=None, raw=False, timeout=30):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    # rate limit
    elapsed = time.time() - _last_request_ts[0]
    if elapsed < _MIN_INTERVAL:
        time.sleep(_MIN_INTERVAL - elapsed)
    _last_request_ts[0] = time.time()

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            if raw:
                return data
            return json.loads(data.decode("utf-8"))
    except Exception as e:
        print(f"  [http] {type(e).__name__}: {e}", file=sys.stderr)
        return None


# --------------------------- Wikipedia API ---------------------------

def wiki_search(query, limit=3):
    """Return list of titles for top search hits."""
    res = http_get(API_BASE, {
        "action": "query", "list": "search", "srsearch": query,
        "srlimit": limit, "format": "json", "srnamespace": 0,
    })
    if not res:
        return []
    return [h["title"] for h in res.get("query", {}).get("search", [])]


def wiki_page_exists(title):
    """Return resolved title if a non-redirect, non-disambig article exists.

    Uses `titles=` + `redirects=` so a redirect resolves to its target; also
    checks `pageprops.disambiguation` so we reject disambig hubs.
    """
    res = http_get(API_BASE, {
        "action": "query", "titles": title, "redirects": 1,
        "prop": "pageprops", "format": "json",
    })
    if not res:
        return None
    pages = res.get("query", {}).get("pages", {})
    for pid, page in pages.items():
        if pid == "-1":
            return None  # missing
        if "disambiguation" in (page.get("pageprops") or {}):
            return None
        return page.get("title")
    return None


# Articles that are too generic to be useful as a Wikipedia match.
GENERIC_REJECT_RE = re.compile(
    r"^(physics|mathematics|chemistry|biology|science|astronomy|"
    r"engineering|technology|history of physics|"
    r"list of [\w\s]+|outline of [\w\s]+|index of [\w\s]+|"
    r"branches of [\w\s]+|glossary of [\w\s]+|"
    r"timeline of [\w\s]+|table of [\w\s]+)$",
    re.IGNORECASE,
)


def find_article(page_title, aliases):
    """Resolve a Wikipedia article for a vault page.

    Strategy (most specific first):
      1. Direct title lookup — handles e.g. "Acceleration", "Capacitance".
      2. Title with "(physics)" disambiguator.
      3. Combine title + " (physics)" via openSearch.
      4. Search "<title>" plain — top hit IF it overlaps with the title.
      5. Search "<title> physics" — top hit IF non-generic and overlapping.
      6. Try aliases the same way.
    Returns canonical article title or None.
    """
    candidates = [page_title]
    for a in aliases:
        a = a.strip()
        if a and 2 < len(a) < 50 and a.lower() != page_title.lower():
            candidates.append(a)

    title_words = set(re.findall(r"\w+", page_title.lower()))
    title_words -= {"the", "of", "a", "an", "and"}

    def overlaps(article_title):
        words = set(re.findall(r"\w+", article_title.lower()))
        words -= {"the", "of", "a", "an", "and", "physics"}
        return bool(title_words & words)

    for cand in candidates:
        # 1. exact title
        resolved = wiki_page_exists(cand)
        if resolved and not GENERIC_REJECT_RE.match(resolved):
            return resolved
        # 2. (physics) disambig
        resolved = wiki_page_exists(f"{cand} (physics)")
        if resolved and not GENERIC_REJECT_RE.match(resolved):
            return resolved

    # 3. plain search
    for cand in candidates:
        hits = wiki_search(cand, limit=5)
        for h in hits:
            if GENERIC_REJECT_RE.match(h):
                continue
            if overlaps(h) or h.lower() == cand.lower():
                resolved = wiki_page_exists(h) or h
                if not GENERIC_REJECT_RE.match(resolved):
                    return resolved

    # 4. "<title> physics" search
    for cand in candidates:
        hits = wiki_search(cand + " physics", limit=5)
        for h in hits:
            if GENERIC_REJECT_RE.match(h):
                continue
            if overlaps(h):
                resolved = wiki_page_exists(h) or h
                if not GENERIC_REJECT_RE.match(resolved):
                    return resolved

    return None


def wiki_pageimage(title):
    """Return (filename, thumb_url) for the article's main image, or (None, None)."""
    res = http_get(API_BASE, {
        "action": "query", "prop": "pageimages", "titles": title,
        "piprop": "name", "format": "json",
    })
    if not res:
        return None
    pages = res.get("query", {}).get("pages", {})
    for page in pages.values():
        name = page.get("pageimage")
        if name:
            return f"File:{name}"
    return None


def wiki_page_images(title, limit=40):
    """Return list of File:... names used on the article (in order)."""
    res = http_get(API_BASE, {
        "action": "query", "prop": "images", "titles": title,
        "imlimit": limit, "format": "json",
    })
    if not res:
        return []
    pages = res.get("query", {}).get("pages", {})
    images = []
    for page in pages.values():
        for img in page.get("images", []):
            images.append(img["title"])
    return images


def wiki_imageinfo(filename):
    """Return imageinfo dict with `url`, `width`, `height`, `size` for a File:..."""
    res = http_get(API_BASE, {
        "action": "query", "prop": "imageinfo", "titles": filename,
        "iiprop": "url|size|mime", "format": "json",
    })
    if not res:
        return None
    pages = res.get("query", {}).get("pages", {})
    for page in pages.values():
        info_list = page.get("imageinfo", [])
        if info_list:
            return info_list[0]
    return None


# --------------------------- Image selection ---------------------------

def acceptable_filename(filename):
    """Reject icons/ui-chrome/audio; require image extension."""
    name = filename.lower().replace("file:", "").strip()
    if REJECT_RE.search(name):
        return False
    if not ALLOWED_EXT_RE.search(name):
        return False
    return True


def pick_images(article_title, max_n=3):
    """Return up to max_n (File:name, info) tuples ranked by likely relevance.

    Strategy: the article's main image goes first (when present), then we walk
    `prop=images` (page-order) and keep the first acceptable, sufficiently
    large ones until we hit max_n.
    """
    chosen = []
    seen = set()

    def big_enough(info, name):
        """Vector images: dimensions decide. Raster: dimensions OR bytes."""
        w, h = info.get("width", 0), info.get("height", 0)
        size = info.get("size", 0)
        mime = (info.get("mime") or "").lower()
        is_vector = "svg" in mime or name.lower().endswith(".svg")
        if w and h:
            # both axes ≥ 150 px (admits narrow strip diagrams), and larger axis ≥ 250 px
            if min(w, h) < 150 or max(w, h) < 250:
                return False
            return True
        # No dimensions (rare) → require ≥ 8 KB for raster, ≥ 500 B for vector
        return size >= (500 if is_vector else 8000)

    main = wiki_pageimage(article_title)
    if main and acceptable_filename(main):
        info = wiki_imageinfo(main)
        if info and big_enough(info, main):
            chosen.append((main, info))
            seen.add(main)

    # Restrict to the first ~10 images on the article — Wikipedia's editorial
    # ordering puts the most topically-relevant pictures at the top, and going
    # deeper picks up tangential figures (etymology paintings, footer
    # navigation icons, related-topic galleries, etc).
    images = wiki_page_images(article_title, limit=10)
    for img in images:
        if len(chosen) >= max_n:
            break
        if img in seen or not acceptable_filename(img):
            continue
        info = wiki_imageinfo(img)
        if not info or not big_enough(info, img):
            continue
        # Skip pathologically large raster files (we'd downscale, but >25 MB
        # often means science-mosaic / high-res scan we don't want anyway).
        if info.get("size", 0) > 25_000_000:
            continue
        chosen.append((img, info))
        seen.add(img)

    return chosen


# --------------------------- Page parsing/editing ---------------------------

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
WIKI_MARKER = "<!-- wiki-images: yes -->"


def parse_frontmatter(text):
    """Return dict-ish frontmatter; only fields we care about."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {"type": None, "aliases": [], "title": None}
    fm = m.group(1)
    out = {"type": None, "aliases": [], "title": None}
    aliases = []
    in_aliases = False
    for line in fm.splitlines():
        if not in_aliases:
            if line.startswith("type:"):
                out["type"] = line.split(":", 1)[1].strip()
            elif line.startswith("aliases:"):
                rest = line.split(":", 1)[1].strip()
                if rest.startswith("[") and rest.endswith("]"):
                    inner = rest[1:-1]
                    aliases = [a.strip().strip("\"'") for a in inner.split(",") if a.strip()]
                else:
                    in_aliases = True
        else:
            if line.startswith("  - "):
                aliases.append(line[4:].strip().strip("\"'"))
            elif line and not line.startswith(" "):
                in_aliases = False
    out["aliases"] = aliases
    return out


def page_title(md_path, text):
    m = re.search(r"^# (.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return md_path.stem.replace("-", " ")


def already_processed(text):
    return WIKI_MARKER in text


def slugify(text, max_len=60):
    text = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text[:max_len] or "img"


def descriptor_from_filename(filename):
    """Slug from a File:Foo_bar.svg -> 'foo-bar'."""
    name = filename.replace("File:", "")
    stem = re.sub(r"\.[^.]+$", "", name)
    stem = stem.replace("_", " ")
    return slugify(stem, max_len=40)


def ext_from_url(url):
    m = re.search(r"\.(svg|png|jpe?g|gif|webp)(?:\?|#|$)", url, re.IGNORECASE)
    return m.group(1).lower() if m else "png"


def insert_visuals(md_path, blocks):
    """Add blocks under a `### From Wikipedia` subsection in `## Visuals`."""
    text = md_path.read_text(encoding="utf-8")
    wiki_section = (
        "\n\n### From Wikipedia\n\n"
        + WIKI_MARKER + "\n\n"
        + "\n\n".join(blocks)
    )

    if "## Visuals" in text:
        # Append to existing Visuals section (just before next ## or EOF).
        m = re.search(r"(## Visuals[\s\S]*?)(?=\n## |\Z)", text)
        if m:
            new_visuals = m.group(1).rstrip() + wiki_section + "\n"
            text = text[:m.start()] + new_visuals + text[m.end():]
    elif "## Source Trace" in text:
        block = "## Visuals" + wiki_section + "\n\n"
        text = text.replace("## Source Trace", block + "## Source Trace", 1)
    else:
        text = text.rstrip() + "\n\n## Visuals" + wiki_section + "\n"

    md_path.write_text(text, encoding="utf-8")


# --------------------------- Logging ---------------------------

def log_line(*fields):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not LOG_PATH.exists():
        LOG_PATH.write_text(
            "page\tstatus\tarticle\timages\tnote\tdate\n", encoding="utf-8"
        )
    with LOG_PATH.open("a", encoding="utf-8") as f:
        line = "\t".join(str(x) for x in fields) + "\n"
        f.write(line)


def already_logged(rel_path):
    if not LOG_PATH.exists():
        return False
    with LOG_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(rel_path + "\t"):
                return True
    return False


# --------------------------- Main per-page logic ---------------------------

def process_page(md_path, folder, dry_run=False):
    rel = str(md_path.relative_to(VAULT))
    if already_logged(rel):
        return ("skip", "previously processed", None, [])

    text = md_path.read_text(encoding="utf-8")
    if already_processed(text):
        log_line(rel, "skip", "-", "-", "marker present", date_today())
        return ("skip", "marker", None, [])

    fm = parse_frontmatter(text)
    if fm.get("type") in SKIP_TYPES:
        log_line(rel, "skip-type", "-", "-", f"type={fm['type']}", date_today())
        return ("skip-type", fm["type"], None, [])

    title = page_title(md_path, text)
    aliases = fm.get("aliases", [])

    # Frontier-map pages have titles like "Quantum Mechanics Map" — strip the
    # trailing "Map" so we search the underlying topic.
    if fm.get("type") == "frontier-map":
        title = re.sub(r"\s+Map$", "", title, flags=re.IGNORECASE).strip()

    article = find_article(title, aliases)

    if not article:
        log_line(rel, "no-article", "-", "-", f"title={title}", date_today())
        return ("no-article", title, None, [])

    picks = pick_images(article, max_n=3)
    if not picks:
        log_line(rel, "no-images", article, "-", "no acceptable images", date_today())
        return ("no-images", article, None, [])

    if dry_run:
        names = ",".join(p[0] for p in picks)
        log_line(rel, "dry-run", article, names, "", date_today())
        return ("dry-run", article, picks, [])

    # Download + build blocks
    blocks = []
    written = []
    for filename, info in picks:
        url = info["url"]
        ext = ext_from_url(url)
        descriptor = descriptor_from_filename(filename)
        page_slug = md_path.stem
        out_name = f"{page_slug}--wiki-{descriptor}.{ext}"
        out_dir = ATTACHMENTS / folder
        out_path = out_dir / out_name

        if not out_path.exists():
            out_dir.mkdir(parents=True, exist_ok=True)
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    data = resp.read()
                out_path.write_bytes(data)
            except Exception as e:
                print(f"  [dl-fail] {filename}: {e}", file=sys.stderr)
                continue
            # Downscale large rasters in place (macOS sips). SVGs untouched.
            if ext in {"jpg", "jpeg", "png", "gif", "webp"}:
                import subprocess
                try:
                    subprocess.run(
                        ["sips", "-Z", "1600", str(out_path)],
                        capture_output=True, timeout=30,
                    )
                except Exception:
                    pass

        rel_attach = f"_attachments/{folder}/{out_name}"
        commons_url = f"https://commons.wikimedia.org/wiki/{filename.replace(' ', '_')}"
        # human title from filename
        human = filename.replace("File:", "").replace("_", " ")
        human = re.sub(r"\.[^.]+$", "", human)

        block = (
            f"#### {human}\n\n"
            f"![[{rel_attach}]]\n"
            f"*Figure: from Wikipedia article \"{article}\".*\n"
            f"*Source: Wikimedia Commons — [{filename.replace('File:', '')}]"
            f"({commons_url}). Retrieved {date_today()}.*"
        )
        blocks.append(block)
        written.append(rel_attach)

    if blocks:
        insert_visuals(md_path, blocks)
        log_line(rel, "added", article, ",".join(written), "", date_today())
        return ("added", article, picks, written)

    log_line(rel, "download-failed", article, "-", "", date_today())
    return ("download-failed", article, picks, [])


def date_today():
    return time.strftime("%Y-%m-%d")


# --------------------------- Driver ---------------------------

def iter_pages(folders):
    for folder in folders:
        d = VAULT / folder
        if not d.exists():
            continue
        for md in sorted(d.rglob("*.md")):
            yield folder, md


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folders", nargs="*", default=FOLDERS,
                    help="Folders to process (default: all 02-12)")
    ap.add_argument("--limit", type=int, default=0,
                    help="Stop after N pages (0 = no limit)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Look up articles + images but don't download or edit")
    args = ap.parse_args()

    n = 0
    t0 = time.time()
    for folder, md_path in iter_pages(args.folders):
        rel = str(md_path.relative_to(VAULT))
        # take only top-level files in the folder + experiment subdirs
        # (we still recurse, but report cleanly)
        status = process_page(md_path, folder, dry_run=args.dry_run)
        outcome = status[0]
        article = status[1] if len(status) > 1 else "-"
        sec = time.time() - t0
        print(f"[{n+1:3d}] {sec:5.0f}s {outcome:14s} {rel}  ←  {article}",
              flush=True)
        n += 1
        if args.limit and n >= args.limit:
            break

    print(f"\nDone: {n} pages processed in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
