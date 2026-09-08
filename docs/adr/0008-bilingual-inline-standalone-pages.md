---
status: accepted
---

# Standalone pages (Journey, Editorial Notes) are bilingual-inline; Posts are single-language

A Post carries exactly one language, declared via the mandatory `lang` front matter field — there is no translated counterpart elsewhere in the blog. That's deliberate: maintaining a full translation of every Post would be more effort than the audience split justifies, and which language a given Post is written in is itself an editorial choice (who it targets, where/how the underlying story happened), not a constraint to work around.

Journey and Editorial Notes don't follow that model. Both are single, curated, site-level pages rather than entries in a growing collection — there's exactly one Journey and one Editorial Notes, ever. Each is authored as one file holding both `pt` and `en` copy per section (`_data/journey.yml`, `_data/editorial.yml`), with the reader's language switched client-side. Splitting them into separate-language files the way Posts are separated would fork content that's meant to always say the same thing in both languages, for no benefit — there's no editorial reason to publish one language's version of "why this blog exists" without the other.

## Consequences

- Any future page of this shape (singular, site-level, not a content entry in a growing collection) should default to the bilingual-inline pattern, not the Post per-language pattern.
- A future Post-like collection (if one is ever added) should default to the Post pattern (one language per entry) unless there's a specific editorial reason to do otherwise.
- See [`CONTEXT.md`](../../CONTEXT.md)'s **Post language**, **Journey**, and **Editorial Notes** terms for the domain definitions this decision formalized.
