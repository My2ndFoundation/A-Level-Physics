# Lint Workflow

Periodic health check of the wiki layer. The lint workflow reports issues; it does not silently rewrite content.

## Checks

- detect pages missing frontmatter
- detect pages whose `type` does not match folder
- detect pages not following required template
- detect missing source trace
- detect orphan pages
- detect broken wikilinks
- detect duplicate aliases
- detect broad content pages that should be MOCs
- detect MOCs missing links to new pages
- detect pages over 800 words that may need splitting
- detect laws without units or conditions
- detect graphs without gradient/area interpretation
- detect practical pages without variables or uncertainty
- detect physical quantities without SI unit
- detect frontier pages that go too deep
- detect common-sense pages that do not link to A-Level concepts
- detect A-Level pages with no prerequisite/foundation links where such links are relevant

## Output

Produce a report grouped by issue category, with file paths and a recommended fix for each. Do not auto-fix without user direction; template/structure violations should be flagged for repair.
