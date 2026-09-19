---
status: accepted
---

# A per-Post currency converter takes its rate from the Post's front matter

Travel Posts quote the local currency first and the euro second, at the rate that applied during the trip — AED 3.97 to the euro in April 2022, 90 lek to the euro in June 2026 — and say so in a callout. Any figure the prose does not convert leaves the reader doing the arithmetic, and a reader who reaches for today's rate gets a number more than 10% off. ADR-0015 already listed a per-Post currency converter as a follow-up Calculator, but its rule that every number lives in `_data/calculators/<name>.yml` does not fit: the rate is a fact about one trip, not a table that changes every year.

**The `fx-converter` Calculator reads its currency pair, rate and date from the Post's front matter, and renders nothing when the Post has none.** A travel Post declares `fx: { from: AED, to: EUR, rate: 3.97, as_of: 2022-04 }` — `rate` is how many `from` one `to` bought, `as_of` the month or day it applied — and embeds `{% include calculators/fx-converter.html %}` next to its currency callout. The include exits before emitting a byte when `page.fx` is missing, so it is safe to leave in place. Its own data file, `_data/calculators/fx-converter.yml`, carries only the UI copy per Post language and the reference amounts of the fallback table; no rate ever lives there or in the include. The stylesheet and script helpers are the shared partials of ADR-0017.

**The rate is presented as historical, never as current, and the page fetches nothing.** The eyebrow, the title, the field legend and the result card all carry the `as_of` month; the intro says outright that it is not today's rate. A reader who wants today's figure types it into a second field — the label states the direction — and gets a second card with the difference to the trip's rate. The two amount fields are linked, so either currency can be typed. Without JavaScript the reader sees the same rate as a reference table (10, 50, 100, 500 and 1,000 units of the local currency) and the inverse rate.

## Consequences

- A Post's rate changes only by editing that Post; nothing in `_data/` needs touching for a new trip.
- The reference amounts and the copy are shared by every Post that embeds the converter; a Post with an unusual currency scale (yen, won) may want its own amounts, which would mean a front matter override rather than a copy of the include.
- Currency codes must be ISO 4217: both the `money` filter and `Intl.NumberFormat` take the code as given and `Intl` throws on an unknown one. Codes without a symbol print as the code (`AED 100`).
- `as_of` may be a year-month string (`2022-04`) or a full date; `localized_date` renders either as "abril de 2022" / "April 2022".
- The audit does not validate `fx`; a missing `rate` makes the include render nothing, which is the visible symptom.
