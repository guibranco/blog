---
status: accepted
---

# "Last modified" is computed by diffing each post's body across its full git history, not its last commit

`_plugins/git_last_modified.rb` sets `last_modified_at` on every post and page by walking a file's entire commit history (`git log --follow`) and comparing the body — everything after the closing `---` of the front matter — between each revision and the one immediately before it, stopping at the first commit that actually changed it. A naive `git log -1` (the file's single most recent commit, tried first) was rejected: a commit that only touches front matter — adding `tags`, `reading_time`, or the mandatory `lang:` field added across every post in one pass (see [ADR-0006](0006-post-language-mandatory-no-site-default.md)) — would make every touched post falsely appear "updated today," which is exactly the bug this plugin exists to prevent.

This value feeds two things: `_includes/post-dates.html`'s "Atualizado em"/"Updated on" line on post pages and every listing (post cards, tags, series, the visual site map, travels), shown only when the day differs from the publish date; and `jekyll-sitemap`'s `<lastmod>` in `sitemap.xml`, which already reads `last_modified_at` when present.

## Consequences

- This requires the full git history at build time. `.github/workflows/deploy.yml`'s checkout step must keep `fetch-depth: 0` — the default shallow clone (`fetch-depth: 1`) leaves only the latest commit per file, silently reproducing the exact "everything shows updated today" bug this plugin exists to fix. This was hit once in production and fixed alongside this ADR.
- Walking full history costs one `git show` per revision instead of one `git log -1` per file — a small in-memory cache avoids re-fetching the same revision's body twice within one file's walk. Cheap at this blog's scale (a few dozen posts, a handful of revisions each); would need reconsidering if per-file history ever grew into the hundreds of commits.
- "Updated" is defined as body-only changes, by deliberate choice — a front-matter-only edit (correcting a category, adding a tag, registering a new `lang:`) never counts as an update, even though it's a real commit, because it isn't something a reader would notice in the text.
