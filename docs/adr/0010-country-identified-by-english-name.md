---
status: accepted
---

# A Country is identified by its English name; pt-BR is a display translation

`_data/countries.yml` originally used the pt-BR name as each entry's `name` — the value a Trip's `countries:` front matter had to match and the audit validated — with `name_en` as the English label swapped in client-side when the UI language was EN. That made the Portuguese spelling the identity of a Country ("Reino Unido", "Países Baixos", "Emirados Árabes Unidos"), which is the reverse of how the rest of the site's data is keyed: slugs, tags, category slugs and code are all English/ASCII, and pt-BR is one of two UI languages, not the schema language.

The registry is now keyed the other way round. `name` is the English name and the canonical identifier — it is what a Post writes in `countries:`, what `audit_blog.py` checks, and what the travels page groups and sorts by. `name_pt` is the pt-BR translation, shown only when the UI language is pt-BR. The `slug` (used by the `/viagens/?country=` filter and as the `data-country` key for the client-side language switch) is derived from the English name too, so `reino-unido` became `united-kingdom`, `paises-baixos` became `netherlands`, and so on.

Every consumer resolves the label the same way: look up `name_<subtag>` for the active UI language and fall back to `name`. The travels page does this at build time for its base language (`pt-BR`, per ADR 0006), `travels-filter.js` does it when it rebuilds the table, and `lang-switcher.js` does it for every `[data-country]` element on a language change. Adding a third UI language later means adding a `name_<subtag>` column, nothing else.

## Consequences

- Existing Trips had their `countries:` values rewritten to English in the same change; new Trips must use the English name exactly as it appears in `countries.yml`.
- `?country=` links to `/viagens/` that used a pt-BR slug no longer match any option and silently fall back to "all countries". Accepted: the filter is recent (#207) and the URL is only filter state, never a canonical page address.
- Sorting on the travels page is by the English name in both the Liquid render and the client-side rebuild, regardless of the UI language — the order does not change when the visitor switches language.
- See [`CONTEXT.md`](../../CONTEXT.md)'s **Country** term for the domain definition this decision formalized.
