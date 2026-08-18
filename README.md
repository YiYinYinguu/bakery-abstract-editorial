# Bakery Abstract Editorial

English | [简体中文](README.zh-CN.md)

Turn bakery photos into two-panel editorial compositions. The original photo stays in the upper panel, while the lower panel isolates one representative baked good and reimagines it with simpler shapes, brushwork, and color.

The abstraction draws from the product's silhouette, cross-section, layers, and texture. Distinctive features—like a bagel's center hole, a Swiss roll's spiral, a sandwich loaf's crown, or the scoring on a rustic loaf—take priority because they keep the subject recognizable.

## Photos with multiple baked goods

A source photo can include several examples of the same product, such as a full tray of bread.

When that happens, the skill selects the strongest representative for the lower panel. A tray of bagels can become a single bagel, a box of cake slices can be represented by one slice, and a group of loaves can be distilled to the one with the clearest form.

If the product's identity comes mainly from its cross-section or interior structure, the skill can focus on the most distinctive slice or detail instead.

## Visual style

- The original photo remains in the upper panel
- The lower panel keeps only the essential form and texture
- The color palette comes from the source photo
- Loose brushwork, broad color fields, and subtle handmade marks
- Plenty of breathing room
- Simplified enough to feel abstract, but still recognizable

## Works well with

This approach is best suited to baked goods with a distinctive silhouette, texture, cross-section, or layered construction, including:

- Rustic loaves, sourdough, and sandwich bread
- Dinner rolls, bagels, and braided loaves
- Croissants and other laminated pastries
- Cakes, Swiss rolls, tarts, and pies
- Scones, muffins, and cookies
- Chinese bakery items such as pineapple buns and egg-yolk pastries
- Steamed buns and breads, including mantou and bao

The result is a vertical editorial composition that pairs the original food photography with a complementary abstract illustration.

## Ways to use it

These images do not have to stop at a single editorial piece. They also work well in:

- Digital planners and baking journals
- Calendars and timelines organized by date
- Baking collections from a particular season or period
- Personal baking catalogs
- Quarterly and annual recaps

Each bake leaves behind a recognizable image in a consistent visual language, making the collection easy to arrange, revisit, and build on over time.

### A baking journal organized as a timeline

![A baking journal arranged by month](examples/use-cases/baking-timeline.png)

### A visual baking catalog organized as a calendar

![A baking catalog arranged by date](examples/use-cases/baking-calendar.png)

## Examples

Fourteen source-to-abstraction examples are included in [`examples/`](examples/README.md). Each case contains the unchanged source photograph, the standalone abstract panel, and the final editorial composite.

| | |
|---|---|
| [![Colorful egg-yolk pastry](examples/13-colorful-egg-yolk-pastry/editorial.webp)](examples/13-colorful-egg-yolk-pastry/) | [![Red-bean mantou](examples/14-red-bean-mantou/editorial.webp)](examples/14-red-bean-mantou/) |
| [![Pineapple bun](examples/09-pineapple-bun/editorial.webp)](examples/09-pineapple-bun/) | [![Chocolate muffin](examples/10-chocolate-muffin/editorial.webp)](examples/10-chocolate-muffin/) |
| [![Rustic loaf](examples/01-rustic-loaf/editorial.webp)](examples/01-rustic-loaf/) | [![Brioche loaf](examples/02-brioche-loaf/editorial.webp)](examples/02-brioche-loaf/) |
| [![Wool roll bread](examples/03-wool-roll-bread/editorial.webp)](examples/03-wool-roll-bread/) | [![Chocolate bagel](examples/04-chocolate-bagel/editorial.webp)](examples/04-chocolate-bagel/) |
| [![Matcha crepe roll](examples/05-matcha-crepe-roll/editorial.webp)](examples/05-matcha-crepe-roll/) | [![Flan](examples/06-flan/editorial.webp)](examples/06-flan/) |
| [![Matcha cake](examples/07-matcha-cake/editorial.webp)](examples/07-matcha-cake/) | [![Cranberry scone](examples/08-cranberry-scone/editorial.webp)](examples/08-cranberry-scone/) |
| [![Angel cake roll](examples/11-angel-cake-roll/editorial.webp)](examples/11-angel-cake-roll/) | [![Coconut braided bread](examples/12-coconut-braided-bread/editorial.webp)](examples/12-coconut-braided-bread/) |

## Requirements

- ChatGPT or Codex with image-generation capability
- Python 3.10 or later
- Pillow, for deterministic final composition

Install the Python dependency with:

```bash
python3 -m pip install -r requirements.txt
```

## Install in Codex

Ask Codex to install the skill from its GitHub path:

```text
Use $skill-installer to install bakery-abstract-editorial from https://github.com/YiYinYinguu/bakery-abstract-editorial/tree/main/skills/bakery-abstract-editorial
```

For local development, link `skills/bakery-abstract-editorial` into your user skill directory.

## Use

Invoke the skill with a bakery photograph and a request such as:

```text
Use $bakery-abstract-editorial to turn this sourdough photo into a balanced abstract editorial.
```

The workflow first generates and reviews the abstract panel. It only composes the unchanged photograph with an approved panel afterward.

The composition script writes a lossless PNG. Final composites in `examples/` are stored as WebP only to keep repository previews lightweight; converting the PNG to WebP is a presentation step and is not required by the skill.

## Validate locally

Install the development dependencies and run the repository checks:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
```

The checks cover skill metadata, reference links, example completeness and privacy metadata, standard image dimensions, and a real composition run. GitHub Actions runs the same suite on Python 3.10 and 3.13.

## Repository layout

```text
skills/bakery-abstract-editorial/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── bakery-cues.md
│   └── prompt-pattern.md
└── scripts/compose_editorial.py
examples/
└── 01-rustic-loaf/ ... 14-red-bean-mantou/
```

## License

The skill code and documentation are MIT licensed. Example photographs, abstract panels, and editorial composites are not covered by the MIT license; see [`examples/ASSET-LICENSE.md`](examples/ASSET-LICENSE.md).
