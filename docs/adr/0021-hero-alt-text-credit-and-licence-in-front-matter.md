---
status: accepted
---

# A Hero declares its alt text, credit and licence in the front matter, and one set of templates renders them

Until the Munich Trip every Hero was the author's own work: a hand-drawn SVG, a generated card, or a photo from the trip. The post layout therefore used the Post title as the Hero's `alt` and showed nothing under it. The Munich post is the first whose Hero is somebody else's photograph (Unsplash), and it arrived with three front matter fields nothing read: `image_alt`, `image_credit` and `image_license`. Left unrendered, the photographer went uncredited on the page and the image kept a title for an alt text, which describes the Post, not the picture.

**Five optional fields describe the Hero; `image` stays a path.**

- `image_alt` is the text alternative: what the picture shows, in the Post language, by the same editorial rule as a Gallery photo's `alt`.
- `image_credit` is who made it ("Name / Source"), and `image_license` the licence it is used under. They are for a Hero the author did not make; an own photo or an own SVG carries neither.
- `image_credit_url` and `image_license_url` turn those two texts into links (the photographer's or the photo's page; the licence text). Each is meaningless without its text.

jekyll-seo-tag can already read an alt from `image` when it is a hash (`image: { path:, alt: }`). That shape was rejected: `image` is read as a plain path by the post layout, the cards, the related-posts block, `schema.html`, `audit_blog.py` and `build_og_cards.py`, and it is a plain path in every existing post; flat sibling fields cost one line each in the templates and nothing anywhere else.

**Where they are rendered.**

- *Post page.* The Hero `<img>` takes `image_alt`, falling back to the title as before. When a credit or a licence is present, a `<figcaption class="post-cover-credit">` under the Hero reads "Foto: … · Licença: …" (labels from `_data/i18n.yml`, switched client-side like the rest of the chrome), each part linked when its URL is given. The credit sits outside `data-pagefind-body`, so it does not enter the search index (ADR-0020).
- *Social cards.* The layout emits `og:image:alt` and `twitter:image:alt` itself, right after `{% seo %}`, because the gem only writes them for the hash shape.
- *Structured data.* In the `Article` node of `schema.html` (ADR-0014), `image` becomes an `ImageObject` when any of the fields is set: `description` from the alt, `creditText` from the credit, and `license` as the licence URL, or as a named `CreativeWork` when only the name is known. `image_credit_url` is not emitted: it is an attribution link (a photographer's profile, a photo's page), and the one property that would take a URL here, `acquireLicensePage`, means a page where the licence can be obtained, which would need a field of its own. A Hero with none of the fields keeps the plain URL, so no existing post's markup changes.
- *Listings.* `post-card.html` and the home's featured block use `image_alt` for their thumbnail, with the same fallback. No credit there: the thumbnail is a link to the page that carries it.

**The audit warns, it does not block.** `audit_blog.py` flags a `*_url` that is not an absolute http(s) URL, a `*_url` without the text it links, and any of the three texts on a Post with no `image`. None of those breaks the build or the page, so they are warnings, like a drifting `reading_time`.

## Consequences

- The fields describe the Hero whichever file backs it (`cover` or `image`, CONTEXT.md's **Hero**); a Post whose on-page `cover` and social `image` were different pictures would need two alts, which no Post has and this does not model.
- Nothing is backfilled. The 62 posts without the fields render exactly as before, title-as-alt included; adding an `image_alt` to an old post is a front-matter-only edit and does not move its Updated date (ADR-0007).
- A licence is recorded as the author states it; nothing checks that the licence allows the use, or that the credit is right. That stays an editorial responsibility, as the Editorial Notes already say of sources.
- Gallery photos are unaffected: they are the author's own, placed with `photo.html` (ADR-0011), and have no credit line. A third-party photo in a Gallery would need its own decision.
- See [`CONTEXT.md`](../../CONTEXT.md)'s **Hero** term, which now names the alt text and the credit.
