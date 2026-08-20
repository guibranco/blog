---
status: superseded by ADR-0003 (Tag pages), ADR-0004 (Category/Subcategory pages), and ADR-0005 (RSS feeds) — fully superseded, kept as historical record
---

# Category, Subcategory, Tag, and feed pages are committed stub files, not dynamically generated

> **Update:** Every page type this ADR originally covered has moved off this pattern — Tag pages ([ADR-0003](0003-tag-pages-generated-from-data-file.md)), Category/Subcategory pages ([ADR-0004](0004-category-pages-generated-from-data-file.md)), and RSS feeds ([ADR-0005](0005-feed-pages-generated-from-data-file.md)). Nothing in this repo still follows the pattern described below; this ADR is kept only as a record of the original trade-off and why it was eventually reversed.

Every Category, Subcategory, Tag page, and per-Category/Subcategory RSS feed is a physical file (`categorias/**/*.md`, `topicos/*.md`, `feed/*.xml`), auto-created by `.github/scripts/create_missing_pages.py` when a pull request touches `_posts/`, then committed to that PR's branch — rather than generated dynamically at Jekyll build time from `_data/categories.yml` and the Posts' own front matter.

## Considered Options

- **A custom Jekyll generator plugin** — technically viable: `deploy.yml` runs a full `bundle exec jekyll build` inside GitHub Actions, not GitHub Pages' restricted safe-mode build, so custom plugin Ruby code can run. A generator could emit every Category/Subcategory/Tag/feed page at build time with zero committed stubs.
- **The `jekyll-archives` plugin** — rejected: doesn't support the nested `/categorias/{cat}/{sub}/` permalink shape or the curated per-category icon lookup (`_data/categories.yml`) without writing custom code anyway, which erases most of the appeal of reaching for an off-the-shelf plugin.

## Consequences

Stub files keep every generated page as plain, reviewable markdown showing up in ordinary PR diffs — debuggable by anyone without touching Ruby, and immune to breaking silently on a Jekyll or plugin upgrade. The cost is hundreds of near-identical files and a Python script (`create_missing_pages.py`) to keep them in sync with posts' front matter.

Replacing this with a generator plugin remains a live option for a future pass, not something decided against permanently — flagged here rather than acted on.
