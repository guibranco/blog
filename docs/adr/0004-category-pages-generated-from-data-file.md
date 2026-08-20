---
status: accepted
---

# Category and Subcategory pages are generated at build time from `_data/categories.yml`

Category and Subcategory pages no longer exist as committed files under `categorias/`. `_data/categories.yml` — already the source of truth for name/slug/icon — now also carries `redirect_from` at both the category and subcategory level, and `_plugins/category_pages_generator.rb` (a Jekyll `Generator`, same pattern as [ADR-0003](0003-tag-pages-generated-from-data-file.md)'s tag generator) creates one page per entry at build time: `layout: category`, `category`/`subcategory`, and the right permalink. Top-level Category pages additionally get a `pagination: {enabled: true, category: <name>}` block for `jekyll-paginate-v2`; Subcategory pages deliberately don't — `_layouts/category.html` filters subcategory posts via plain Liquid, not the paginator (`site.posts | where_exp` against `post.subcategories`), a design already in place before this change.

This further executes the alternative flagged in [ADR-0001](0001-stub-files-for-category-tag-feed-pages.md). RSS feeds were still committed files at the time this ADR was written; [ADR-0005](0005-feed-pages-generated-from-data-file.md) completed the migration immediately after, moving feeds onto the same `_data/categories.yml`-driven generation and removing the feed-file architecture entirely — ADR-0001 is now fully superseded.

## Migration findings worth recording

- Four legacy stub files (`categorias/devops.md`, `categorias/telecomunicacoes.md`, `categorias/testing.md`, `categorias/travel-places.md`) used `redirect_to` — a different mechanism than `redirect_from` — to redirect old flat-namespace URLs. They were dropped, not migrated: their targets were already fully covered by `redirect_from` entries on the real destination pages, and production traffic was verified (via live fetch) to already resolve through `redirect_from`, not `redirect_to` — one of them (`categorias/devops.md`) even pointed at a stale, no-longer-correct destination, so it was already dead weight.
- `categorias/coding/architecture.md` carried a leftover `pagination.where_condition` block that no other subcategory file had. It's dead configuration — `_layouts/category.html` never reads `paginator` for subcategory pages — so it was not reproduced in `_data/categories.yml` or the generator.
- `_data/categories.yml`'s hand-rolled parser/serializer (`parse_categories_yaml`/`serialize_categories_yaml` in `create_missing_pages.py`) was extended to round-trip `redirect_from` at both levels. Without this, the next automated sync (adding a brand-new category) would have silently dropped every existing `redirect_from` entry on write — verified this doesn't happen with a live test before considering the migration done.

## Consequences

- `create_missing_pages.py` no longer writes `categorias/**/*.md` files. `sync_categories_data` (already existing, now extended for `redirect_from`) is the only mechanism that keeps `_data/categories.yml` in sync with what posts declare. At the time of this change, the script's `create_pages` function still handled RSS feed files — [ADR-0005](0005-feed-pages-generated-from-data-file.md) removed that function entirely once feeds moved to the same generator pattern.
- `audit_blog.py`'s "missing category page" check now reads `_data/categories.yml` instead of scanning a directory. Subcategory registration was already checked against `_data/categories.yml` before this change (the `invalid_subcategories` check), so no new check was needed there.
- Same caveat as ADR-0003: no local Jekyll build available to verify this before committing — first real verification is CI on the next PR, plus a live production check of a redirected legacy URL (e.g. `/categorias/devops/`) after deploy, the same way ADR-0003's tag migration was verified.
