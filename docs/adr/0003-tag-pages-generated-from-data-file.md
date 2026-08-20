---
status: accepted
---

# Tag pages are generated at build time from `_data/tags.yml`, not stub files

Tag pages no longer exist as committed files under `topicos/`. `_data/tags.yml` is now the single source of truth for which tags have a page (`name` + `slug`, plus `redirect_from` for the tags that previously lived under `/tags/...`), and `_plugins/tag_pages_generator.rb` — a Jekyll `Generator` — creates one page per entry at build time: `layout: tag`, `tag: {name}`, permalink `/topicos/{slug}/`. This is viable for the same reason noted in [ADR-0001](0001-stub-files-for-category-tag-feed-pages.md): `deploy.yml` runs a full `bundle exec jekyll build`, not GitHub Pages' restricted safe-mode, so custom plugin code runs fine.

This executes, for tags specifically, the alternative [ADR-0001](0001-stub-files-for-category-tag-feed-pages.md) flagged but deliberately left undone. It does **not** extend to Category/Subcategory pages or RSS feeds — those remain committed stub files per ADR-0001, unchanged by this decision.

## Consequences

- `.github/scripts/create_missing_pages.py` no longer writes `topicos/{slug}.md` files; it appends `{name, slug[, redirect_from]}` entries to `_data/tags.yml` instead.
- `.github/scripts/audit_blog.py` checks tag existence against `_data/tags.yml` entries rather than file existence in `topicos/`.
- `topicos/index.html` (the tag-cloud listing page) is unaffected — it already computed its tag list dynamically from `site.posts`, never from the stub files.
- This was implemented without a local Jekyll build to verify it (no Ruby/Bundler available in the authoring environment) — the first real build (CI, on the next PR touching `_posts/` or `_data/tags.yml`) is the actual verification that the generator and the carried-over `redirect_from` entries work as intended.
