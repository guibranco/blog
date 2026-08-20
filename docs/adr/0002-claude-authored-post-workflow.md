---
status: accepted
---

# Claude-authored posts: input contract, taxonomy autonomy, and image production

When asked to build a new Post from raw material, Claude's job is purely organizational: section structure, callouts, tables, and front matter. Claude never invents facts, statistics, or personal anecdotes beyond what was supplied — but it may research and cite its own external sources (via WebSearch/WebFetch) for non-personal claims, the same way existing posts cite government sites and docs in their "Referências" sections.

Claude assigns Category, Subcategory, and Tag confidently from the *existing* taxonomy in `_data/categories.yml`, and joins an existing Series when the new post is clearly a continuation. It never silently mints a new Category or Subcategory — when it thinks one is genuinely warranted, it flags that explicitly (to the user, or in the eventual PR description) instead.

Claude authors the Cover image itself as an SVG matching the site's established brand tokens (see `CONTEXT.md`), sized to 1200×630. The Social image PNG is *not* rasterized by Claude Code in this environment — no SVG rasterizer is installed here — so it's rendered externally (via claude.ai/Desktop, or by the user) and added to `assets/img/posts/` in a follow-up commit, the same way existing Social images entered the repo (`git log` shows them landing as plain "Add files via upload" commits, not through any build step).

Claude only ever edits the working tree — it does not branch, commit, push, or open the pull request itself; the user drives all git/PR mechanics. Delivery through a PR is mandatory regardless of who drives it, because `sync-category-tag-data.yml` (the automation that registers the new post's Category/Subcategory/Tag in `_data/categories.yml`/`_data/tags.yml` — see [ADR-0003](0003-tag-pages-generated-from-data-file.md), [ADR-0004](0004-category-pages-generated-from-data-file.md), [ADR-0005](0005-feed-pages-generated-from-data-file.md)) only fires on `pull_request` events — a direct push to `main` would silently skip that registration, and the post's Category/Tag/feed pages would never get generated at build time.

## Consequences

A Claude-authored post's PR may briefly reference a Social image file that doesn't exist on disk yet. This passes CI without issue: `audit_blog.py` validates only the front matter's file *extension*, not whether the file exists — so the SVG and post markdown can land first, with the PNG following in a second commit before merge.
