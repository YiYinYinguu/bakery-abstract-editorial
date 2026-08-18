# Panel prompt pattern

Generate only the lower abstract panel. Replace bracketed text with facts observed in the source.

```text
Use case: stylized-concept
Asset type: lower panel for a vertical bakery editorial diptych
Input image: sole source of subject facts and palette; do not reproduce the photograph in the output

Create one landscape abstract editorial panel on a perfectly flat neutral ivory background.

Bakery or dough-based item: [family or subtype]
Recognition contract:
1. [overall mass or outline]
2. [distinctive construction cue]
3. [material or color cue]
4. [optional structural accent]

Abstraction level: [relation | balanced | recognizable].
Primary mark family: [dry brush | broken organic masses | bands | arcs].
Supporting marks: [zero to two families].

Express identity through structure rather than realistic surface. At thumbnail size the baked good must be recognizable without the title. At full size the motif must remain an abstract arrangement of handmade marks.

Use only muted colors sampled from the source. Keep the motif medium-small, fully visible, and surrounded by generous whitespace. Preserve irregular pressure, unequal spacing, pauses, broken edges, and asymmetry when supported by the chosen mark family.

Text verbatim: "[TITLE]". Render it once in a restrained editorial serif below or beside the motif.

Avoid: realistic pores, crumbs, gloss, photographic texture, detailed 3D volume, cast shadow, smooth closed icon, perfect symmetry, regular spacing, gradient fill, logo styling, plate, utensils, steamer basket, loose ingredients, decoration, border, bars, seams, extra text, logo, price, watermark.
```

## Targeted revision clauses

Use only one clause per iteration.

- Recognition: `Strengthen only [cue]; keep abstraction, mark texture, scale, title, and whitespace unchanged.`
- Too realistic: `Remove only surface realism; preserve the recognition contract and construction cues.`
- Too icon-like: `Break the contour and regularity; retain bakery identity through interrupted handmade marks.`
- Too large: `Reduce only the motif scale; keep its internal proportions and title unchanged.`
- Wrong item count: `Show exactly one coherent baked good; remove all duplicates and supporting objects.`
