#!/usr/bin/env python3
"""
fetch_wikipedia_images_postpass.py

Post-pass for the main sweep. For each (page, override_article) entry:
  1. Delete that page's `### From Wikipedia` subsection.
  2. Delete the corresponding `--wiki-*` image files in _attachments.
  3. Delete the page's row from `.state/wiki-image-fetch.tsv`.
  4. Re-run the main script with `--page <path> --article <override>`.

Run after fetch_wikipedia_images.py to fix wrong-article matches.
"""

import re
import sys
import time
import urllib.request
from pathlib import Path

# Import everything we need from the main script
sys.path.insert(0, str(Path(__file__).parent))
from fetch_wikipedia_images import (  # noqa: E402
    VAULT, ATTACHMENTS, LOG_PATH, WIKI_MARKER,
    pick_images, descriptor_from_filename, ext_from_url,
    insert_visuals, date_today, USER_AGENT,
)

# Page -> Wikipedia article overrides.
# Each fix is keyed by vault-relative md path.
OVERRIDES = {
    # — Common-sense pages where short "Why X" titles confused search
    "02_Foundations/Everyday-Physics/Why-Seatbelts-Matter.md": "Seat belt",
    "02_Foundations/Everyday-Physics/Why-Objects-Keep-Moving-in-Space.md": "Newton's laws of motion",
    "02_Foundations/Everyday-Physics/Why-Metal-Feels-Colder-Than-Wood.md": "Thermal conduction",
    "02_Foundations/Everyday-Physics/Why-Sound-Needs-a-Medium.md": "Sound",
    "02_Foundations/Everyday-Physics/Why-Ice-Floats.md": "Properties of water",
    "02_Foundations/Everyday-Physics/Why-Sky-Is-Blue.md": "Rayleigh scattering",

    # — Genuinely wrong matches found in main sweep
    "04_Concepts/Atomic-Structure.md": "Atom",
    "04_Concepts/Superposition.md": "Superposition principle",
    "04_Concepts/Vectors-and-Scalars.md": "Euclidean vector",
    "08_Representations/Force-Extension-Graph.md": "Hooke's law",
    "06_Models/Wavefront-Model.md": "Wavefront",
    "04_Concepts/Breaking-Stress.md": "Ultimate tensile strength",

    # — Article was right, but no images extracted (broaden search via override)
    "03_Physical-Quantities/Acoustic-Impedance.md": "Acoustic impedance",
    "03_Physical-Quantities/Charge.md": "Electric charge",
    "03_Physical-Quantities/Magnetic-Flux-Linkage.md": "Faraday's law of induction",
    "03_Physical-Quantities/Wave-Speed.md": "Phase velocity",
    "04_Concepts/Binding-Energy.md": "Nuclear binding energy",
    "04_Concepts/Critical-Angle.md": "Total internal reflection",
    "04_Concepts/Elastic-Strain-Energy.md": "Hooke's law",
    "04_Concepts/Internal-Resistance.md": "Electromotive force",
    "04_Concepts/Mass-Defect.md": "Nuclear binding energy",
    "04_Concepts/Mean-Drift-Velocity.md": "Drift velocity",
    "04_Concepts/Measurement-Uncertainty.md": "Uncertainty",
    "04_Concepts/Path-Difference.md": "Wave interference",
    "04_Concepts/The-Nuclear-Atom.md": "Rutherford scattering experiments",
    "02_Foundations/Everyday-Physics/Why-Metal-Feels-Colder-Than-Wood.md": "Heat transfer",
    "04_Concepts/Work-Function.md": "Photoelectric effect",
    "06_Models/Internal-Resistance-Model.md": "Electromotive force",
    "06_Models/Ohmic-Conductor-Model.md": "Ohm's law",
    "08_Representations/Line-of-Best-Fit-Graph.md": "Linear regression",
}


def reset_page(rel_path):
    """Delete wiki section, log line, and wiki-* image files for one page."""
    md = VAULT / rel_path
    text = md.read_text(encoding="utf-8")
    # Strip the wiki subsection (and the marker)
    new_text = re.sub(
        r"\n\n### From Wikipedia\n[\s\S]*?(?=\n## |\Z)", "", text
    )
    if new_text != text:
        md.write_text(new_text, encoding="utf-8")

    # Delete wiki-* image files for this page slug
    page_slug = md.stem
    folder = rel_path.split("/")[0]
    attach_dir = ATTACHMENTS / folder
    if attach_dir.exists():
        for f in attach_dir.glob(f"{page_slug}--wiki-*"):
            f.unlink()

    # Remove from log
    if LOG_PATH.exists():
        lines = LOG_PATH.read_text(encoding="utf-8").splitlines(keepends=True)
        new_lines = [ln for ln in lines if not ln.startswith(rel_path + "\t")]
        LOG_PATH.write_text("".join(new_lines), encoding="utf-8")


def log_line(*fields):
    if not LOG_PATH.exists():
        LOG_PATH.write_text(
            "page\tstatus\tarticle\timages\tnote\tdate\n", encoding="utf-8"
        )
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write("\t".join(str(x) for x in fields) + "\n")


def process_with_override(rel_path, article):
    """Re-run image-pick + page-edit for one page using a fixed article."""
    md = VAULT / rel_path
    folder = rel_path.split("/")[0]
    picks = pick_images(article, max_n=3)
    if not picks:
        log_line(rel_path, "no-images-postpass", article, "-", "override empty", date_today())
        return ("no-images", article, [])

    blocks = []
    written = []
    for filename, info in picks:
        url = info["url"]
        ext = ext_from_url(url)
        descriptor = descriptor_from_filename(filename)
        page_slug = md.stem
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
            # Skip GIFs (sips flattens animation to one frame) and only
            # resample other rasters when they exceed the cap (sips would
            # otherwise upsample small images). See main script for context.
            if ext in {"jpg", "jpeg", "png", "webp"}:
                import subprocess
                try:
                    probe = subprocess.run(
                        ["sips", "-g", "pixelWidth", "-g", "pixelHeight",
                         str(out_path)],
                        capture_output=True, text=True, timeout=10,
                    )
                    dims = re.findall(
                        r"pixel(?:Width|Height):\s+(\d+)", probe.stdout
                    )
                    if dims and max(int(x) for x in dims) > 1600:
                        subprocess.run(
                            ["sips", "-Z", "1600", str(out_path)],
                            capture_output=True, timeout=30,
                        )
                except Exception:
                    pass

        rel_attach = f"_attachments/{folder}/{out_name}"
        commons_url = f"https://commons.wikimedia.org/wiki/{filename.replace(' ', '_')}"
        human = filename.replace("File:", "")
        human = re.sub(r"\.[^.]+$", "", human).replace("_", " ")
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
        insert_visuals(md, blocks)
        log_line(rel_path, "added-postpass", article, ",".join(written), "override", date_today())
        return ("added", article, written)

    log_line(rel_path, "download-failed-postpass", article, "-", "", date_today())
    return ("download-failed", article, [])


def main():
    t0 = time.time()
    for i, (rel, article) in enumerate(OVERRIDES.items(), 1):
        if not (VAULT / rel).exists():
            print(f"[{i:3d}] MISSING {rel}", flush=True)
            continue
        reset_page(rel)
        outcome, art, written = process_with_override(rel, article)
        print(f"[{i:3d}] {time.time()-t0:5.0f}s {outcome:8s} {rel}  ←  {article}  ({len(written)})",
              flush=True)
    print(f"\nDone: {len(OVERRIDES)} pages in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
