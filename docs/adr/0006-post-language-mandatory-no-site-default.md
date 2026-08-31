---
status: accepted
---

# Post language is mandatory per-post; there is no site-wide default anymore

`_config.yml` previously declared a top-level `lang: "pt-BR"`, used as a build-time fallback wherever a post or page's own language wasn't set (`page.lang | default: site.lang`), plus a matching `lang: "pt-BR"` default in the posts collection's `defaults:` block. Every Post now declares its own `lang: en` or `lang: pt-BR` explicitly — enforced as a blocking check in `audit_blog.py` — so that fallback chain became dead code by construction, not just redundant. Both config entries were removed rather than left in place as an unused safety net.

Pages that have no post behind them (home, search, topics, travels, the visual site map) still need a base UI language to render their chrome in — they now hardcode `"pt-BR"` directly, matching the already-hardcoded `<html lang="pt-BR">` those same pages carried before this change, rather than reading a config value that no longer represented anything real. The site's actual default-language *experience* for a first-time visitor comes from `assets/js/lang-switcher.js`'s browser-language detection (`navigator.languages`), which already ran before this change and is unaffected by it — removing `site.lang` only removed a build-time fallback that mandatory per-post `lang:` had made obsolete.

## Consequences

- `jekyll-feed`'s `/feed.xml` template reads `site.lang` for its `xml:lang`/`hreflang` attributes and omits them gracefully when absent (the gem's own template guards with `{% if site.lang %}`) — the main feed's `<feed>` element now carries no language attribute. Accepted as a minor, non-breaking regression.
- Any future page added without a post behind it must hardcode its base language explicitly (as the existing standalone pages now do) — there's no config-level default to fall back to.
- See [`CONTEXT.md`](../../CONTEXT.md)'s **Post language** term for the domain definition this decision formalized.
