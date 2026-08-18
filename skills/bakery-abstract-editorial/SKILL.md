---
name: bakery-abstract-editorial
description: Create or revise vertical bakery editorial diptychs that pair an unchanged source photograph with a poetic abstract panel whose baked or dough-based food remains minimally but clearly recognizable. Use for bread, pastries, cakes, tarts, cookies, buns, mantou, Asian bakery items, bakery product covers, photo-plus-abstraction layouts, recognizable brush abstractions, and requests to balance “too realistic” against “too abstract.”
---

# Bakery Abstract Editorial

Create bakery-focused photo-and-abstraction editorials. Preserve restraint, whitespace, and photo-derived abstraction while retaining only the structural cues needed to recognize the baked good.

Also load the `imagegen` skill before generating or editing raster imagery.

## Core principle

Apply:

`OBSERVE → CONTRACT → ABSTRACT → RECOGNIZE → COMPOSE`

Do not copy the baked good as an illustration. Do not discard so much structure that the panel becomes generic. Preserve the smallest set of cues that answers “what baked good is this?” at thumbnail size.

## Workflow

1. Inspect the source photograph. If it contains several baked goods, select one representative item unless the user explicitly requests a group.
2. Write an internal **recognition contract** containing two to four source-grounded cues:
   - overall mass or outline;
   - one distinctive construction cue such as scoring, lamination, spiral, layers, ring, or cut face;
   - one material or color cue;
   - optionally one structural accent such as a torn edge or filling boundary.
3. Read [references/bakery-cues.md](references/bakery-cues.md) for the relevant bakery family. Use only cues visible in the source.
4. Choose an abstraction level:
   - `relation`: relationships dominate and recognition is delayed; use only when requested;
   - `balanced`: default, approximately 60% abstract and 40% recognizable;
   - `recognizable`: clearer identity while remaining editorial, never photorealistic.
5. Choose one primary mark family and at most two supporting families. For `balanced`, prefer expressive dry brush, broken organic masses, restrained bands, or arcs. Choose marks that fit the baked good's construction rather than applying one universal language.
6. Generate the **lower panel only** as a landscape image. Do not ask the model to reproduce the source photograph. Include the final title in this panel only. Never pass a complete photo-plus-panel poster to the composition script.
7. Inspect the panel at two scales:
   - thumbnail: identify the bakery family without reading the title;
   - full size: observe handmade irregularity rather than realistic surface detail.
8. Revise one variable at a time. If recognition fails, strengthen one contract cue. If the panel becomes illustrative, remove one surface or volume cue.
9. After approval, compose the unchanged source photo and approved panel with `scripts/compose_editorial.py`. Never use a model-generated copy of the photo in the final.

## Panel rules

- Derive every important mark and every color from the source photograph.
- Keep the background flat neutral ivory, preferably `#F3F0E8`.
- Use generous whitespace and a medium-small motif.
- Keep brush endings, pigment skips, unequal pressure, pauses, overlap, and asymmetry when brush is the chosen mark family.
- Use incomplete or optically implied contours instead of polished closed silhouettes.
- Render one original English title, normally two to five words, once only in a restrained editorial serif.
- Exclude plates, utensils, loose ingredients, decorations, borders, bars, seams, logos, prices, and watermarks unless explicitly requested.
- Exclude realistic pores, gloss, photographic crust, detailed crumbs, simulated depth, and cast shadows.
- Exclude smooth vector geometry, perfect symmetry, regular spacing, gradient-filled icons, and logo-like silhouettes.

## Balanced recognition rule

Make the bakery item readable through **structure**, not surface realism.

For a scored rustic loaf, retain an irregular squat mass, a pale flour crown, unequal opened scores with a darker inner edge, and a short baked base cue. Render those facts as broken dry-brush masses; do not paint crust texture. Treat this as a reasoning example, not a template for other baked goods.

## Prompt construction

Use [references/prompt-pattern.md](references/prompt-pattern.md) to build the panel prompt. State the recognition contract, abstraction level, mark family, exact title, and avoid list explicitly. Do not add cues that are absent from the source.

## Preview and finalization

- Keep generated panels and composed drafts outside public website folders until the user approves them.
- Preserve rejected variants only when the user asks.
- For a project asset, copy the approved final into the project and report its path.
- Use `scripts/compose_editorial.py --help` for deterministic composition options.
- The composition script intentionally rejects portrait or square panel inputs; crop or regenerate a true landscape lower panel first.

## Validation checklist

Accept a panel only when all are true:

- The bakery family is recognizable at thumbnail size without the title.
- The exact subtype cues requested by the user remain visible.
- Full-size inspection shows abstract marks, not a realistic food illustration.
- The motif is not a smooth icon or logo.
- The background is continuous ivory with no accidental bars or seams.
- The subject is fully visible, compact, and surrounded by whitespace.
- The title is exact and appears once.
- The final upper region comes from the original file, not generated pixels.
