---
status: superseded by ADR-0003 (Tag pages only — Category/Subcategory/feed pages below are still current)
---

# Category, Subcategory, Tag, and feed pages are committed stub files, not dynamically generated

> **Update:** Tag pages moved off this pattern — see [ADR-0003](0003-tag-pages-generated-from-data-file.md). Everything below now applies to Category, Subcategory, and RSS feed pages only.

Every Category, Subcategory, Tag page, and per-Category/Subcategory RSS feed is a physical file (`categorias/**/*.md`, `topicos/*.md`, `feed/*.xml`), auto-created by `.github/scripts/create_missing_pages.py` when a pull request touches `_posts/`, then committed to that PR's branch — rather than generated dynamically at Jekyll build time from `_data/categories.yml` and the Posts' own front matter.

## Considered Options

- **A custom Jekyll generator plugin** — technically viable: `deploy.yml` runs a full `bundle exec jekyll build` inside GitHub Actions, not GitHub Pages' restricted safe-mode build, so custom plugin Ruby code can run. A generator could emit every Category/Subcategory/Tag/feed page at build time with zero committed stubs.
- **The `jekyll-archives` plugin** — rejected: doesn't support the nested `/categorias/{cat}/{sub}/` permalink shape or the curated per-category icon lookup (`_data/categories.yml`) without writing custom code anyway, which erases most of the appeal of reaching for an off-the-shelf plugin.

## Consequences

Stub files keep every generated page as plain, reviewable markdown showing up in ordinary PR diffs — debuggable by anyone without touching Ruby, and immune to breaking silently on a Jekyll or plugin upgrade. The cost is hundreds of near-identical files and a Python script (`create_missing_pages.py`) to keep them in sync with posts' front matter.

Replacing this with a generator plugin remains a live option for a future pass, not something decided against permanently — flagged here rather than acted on.
