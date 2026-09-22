---
status: accepted
---

# The cost-of-living Calculator seeds a dated, sourced basket the reader overrides, and compares what is left rather than what is spent

Part 2 of "Trabalhar fora sem ilusão" argues that a salary only means something against local costs — "compare o que sobra depois da moradia" — and backs it with the author's rents in Dublin and Dubai. The net-salary Calculator (ADR-0015) does the first subtraction, tax; nothing did the second. A cost-of-living Calculator does not fit ADR-0015's shape exactly: there is no official table to render, and a rent or a grocery basket is an estimate about a market, not a rate a reviewer can check against Revenue.

**Every baseline is a dated market reference with a basis note and a source, kept in `_data/calculators/cost-of-living.yml` and printed next to the field's fallback table.** Dublin and São Paulo each carry the same seven lines for one adult — housing, bills, groceries, public transport, health insurance, childcare per child, leisure — plus an `as_of` month for the set. Where a series exists it is used (Daft.ie for rents, TFI and SPTrans fares, the NCS subsidy, the DIEESE cesta básica, the HIA average premium); where none does (bills, a meal out, a health plan, a crèche place) the reference is a crowd-sourced or trade figure and the note says so. The `basis` note is copy, per Post language, and carries the derivation with its figures — "44 fares of €2", "35 m² at R$ 91.14/m² plus the average condomínio" — so a reader sees why the number is what it is. Changing a baseline therefore means changing its note.

**The form starts filled with the baselines, and every field can be overridden.** A housing select — a room in a shared home, or a studio or one-bed of one's own — re-fills rent and bills for both cities, because the same type of home has to be compared on both sides; São Paulo's housing line is rent plus condomínio, since a Brazilian listing quotes them apart and a Dublin one does not. Childcare is a per-child cost times a count that defaults to zero, so the childless majority's result is not distorted and parents get a sourced number. A reset button brings the references back. An empty field counts as nothing; a negative value or a non-positive rate is refused with a message, never computed.

**Income is the net pay the reader types, so the Calculator composes with the salary Calculator instead of duplicating its tax model.** The two sit one after the other in Part 2: the first turns a gross into a net, the second takes that net. The defaults are what the salary Calculator gives for its own defaults. The result per city is the month's total and what the net leaves — printed as a shortfall, in the warm accent, when it is negative — and the headline is the equivalence: the net pay one city would need to leave what the other leaves, that city's basket plus the other's surplus at the rate given, floored at zero. The proportional "same share of income" figure that cost-of-living indices publish is not shown, because it assumes everything is spent; the Post's argument is about what is not.

**The default EUR→BRL rate moves to `_data/calculators/shared/fx-eur-brl.yml`.** Two Calculators on one page now offer a rate, and ADR-0017 says a figure more than one reads lives once; it is the ECB reference rate of a stated day, rounded to the form's two decimals, with its source listed after each Calculator's own.

## Consequences

- The basket is the same in both cities so the comparison holds; the standard of living it buys is not, and the page says so. Clothes, trips, remittances, the cost of keeping a foot in Brazil and savings are out; taxes are already out of the net.
- The references age: `as_of` and each `verified` date are printed, and refreshing them is a data edit — value, note, source date — with no logic touched.
- A baseline drawn from a crowd-sourced or trade source is weaker than a tax band; the note names the source so the reader can weigh it and, more to the point, replace it.
- The equivalence is deliberately about surplus, not proportion; a reader wanting the index-style number can compute it from the two totals the cards print.
- The Calculator is embedded in Part 2 of "Trabalhar fora sem ilusão" only; the Dublin Post links to it rather than carrying a third Calculator.
- The net-salary include changed two Liquid assigns to read the shared rate; its calculation is untouched.
- See [`CONTEXT.md`](../../CONTEXT.md)'s **Calculator** term, extended for a Baseline.
