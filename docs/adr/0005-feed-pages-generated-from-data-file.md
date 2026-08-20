---
status: accepted
---

# RSS feed pages are generated at build time from `_data/categories.yml`

`feed/*.xml` no longer exists as committed files. `_plugins/feed_generator.rb` — a Jekyll `Generator`, the same pattern as [ADR-0003](0003-tag-pages-generated-from-data-file.md) and [ADR-0004](0004-category-pages-generated-from-data-file.md) — creates one `/feed/{slug}.xml` per top-level Category and one `/feed/{cat_slug}-{sub_slug}.xml` per Subcategory in `_data/categories.yml`, at build time. The RSS body itself is still a Liquid template (`{% assign %}`/`{% for %}` filtering `site.posts`) — Jekyll renders Liquid inside generator-created page content exactly as it does for a file loaded from disk, which the tag and category page generators already proved, so this is a direct Ruby port of the Python script's old `feed_template()`/`subcategory_feed_template()` string templates.

This completes what [ADR-0001](0001-stub-files-for-category-tag-feed-pages.md) originally covered: Tag pages, Category/Subcategory pages, and now feeds have all moved off committed stub files onto build-time generation from the two `_data/*.yml` files. ADR-0001 is now fully superseded — kept only as a historical record of the original trade-off.

## Consequences

- A feed's existence is now strictly 1:1 with its category/subcategory's registration in `_data/categories.yml` — there's no longer a separate "feed missing" state to track. `create_missing_pages.py` dropped all feed-file logic (`create_pages`, `feed_template`, `subcategory_feed_template`, `FEEDS_DIR`) entirely; its only remaining job is syncing `_data/categories.yml` and `_data/tags.yml`. `audit_blog.py` dropped its `missing_feed_files` check for the same reason.
- Same verification caveat as ADR-0003/0004: no local Jekyll build available here. First real verification is CI on the next PR, plus fetching a live `/feed/{slug}.xml` URL after deploy to confirm the generated RSS actually parses and lists posts.
