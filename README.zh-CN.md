# 烘焙抽象编辑设计

[English](README.md) | 简体中文

将烘焙照片转成上下分栏的编辑图。上半部分保留原始照片，下半部分从照片中提取一个有代表性的烘焙产品，用更简洁的形状、笔触和颜色重新表现。

抽象部分会参考产品本身的轮廓、切面、层次和纹理。像贝果的圆孔、瑞士卷的螺旋、吐司的顶部轮廓、欧包的割口，这些容易辨认的特征会优先保留下来。

## 多个烘焙产品

照片里可以有多个同类产品，例如一整盘面包。

遇到这种照片时，这个 skill 会从中挑选一个最有代表性的产品放到下半部分。一盘贝果可以提取成一个贝果，一盒蛋糕可以选取其中一块，一组面包也可以选择其中形态最典型的一个。

如果产品的特点主要来自切面或内部结构，也可以选取最有辨识度的切片或局部。

## 视觉风格

- 上半部分保留原始照片
- 下半部分只保留必要的形态和纹理
- 配色来自原图
- 使用松散的笔触、色块和少量手工痕迹
- 保留较多留白
- 简化之后仍然能辨认出原来的烘焙产品

## 适用内容

适合有明显外形、纹理、切面或层次的烘焙产品，例如：

- 欧包、酸面包、吐司
- 餐包、贝果、辫子面包
- 可颂和其他起酥点心
- 蛋糕、瑞士卷、挞和派
- 司康、玛芬、饼干
- 菠萝包、蛋黄酥等中式烘焙产品
- 馒头、包子等面食

最终会得到一张保留原始摄影，同时带有抽象插画部分的竖版编辑图。

## 可以怎么用

除了单张编辑图，这些图片也可以继续用于：

- 电子手账和烘焙日记
- 按日期整理的月历或时间线
- 一段时间内的烘焙合集
- 个人烘焙图鉴
- 年度或季度回顾

每次烘焙都会留下一个风格统一、容易辨认的小图，之后很方便继续排版和归档。

### 时间线烘焙日记

![按月份整理的烘焙时间线](examples/use-cases/baking-timeline.png)

### 日历烘焙图鉴

![按日期整理的烘焙月历](examples/use-cases/baking-calendar.png)

## 示例

[`examples/`](examples/README.md) 中收录了十四组从原图到抽象画面的示例。每组均包含未经生成式替换的源照片、独立抽象面板和最终编辑合成图。

| | |
|---|---|
| [![彩色蛋黄酥](examples/13-colorful-egg-yolk-pastry/editorial.webp)](examples/13-colorful-egg-yolk-pastry/) | [![红豆馒头](examples/14-red-bean-mantou/editorial.webp)](examples/14-red-bean-mantou/) |
| [![菠萝包](examples/09-pineapple-bun/editorial.webp)](examples/09-pineapple-bun/) | [![巧克力玛芬](examples/10-chocolate-muffin/editorial.webp)](examples/10-chocolate-muffin/) |
| [![乡村面包](examples/01-rustic-loaf/editorial.webp)](examples/01-rustic-loaf/) | [![布里欧修](examples/02-brioche-loaf/editorial.webp)](examples/02-brioche-loaf/) |
| [![毛线球面包](examples/03-wool-roll-bread/editorial.webp)](examples/03-wool-roll-bread/) | [![巧克力贝果](examples/04-chocolate-bagel/editorial.webp)](examples/04-chocolate-bagel/) |
| [![抹茶千层卷](examples/05-matcha-crepe-roll/editorial.webp)](examples/05-matcha-crepe-roll/) | [![焦糖布丁](examples/06-flan/editorial.webp)](examples/06-flan/) |
| [![抹茶蛋糕](examples/07-matcha-cake/editorial.webp)](examples/07-matcha-cake/) | [![蔓越莓司康](examples/08-cranberry-scone/editorial.webp)](examples/08-cranberry-scone/) |
| [![天使蛋糕卷](examples/11-angel-cake-roll/editorial.webp)](examples/11-angel-cake-roll/) | [![椰蓉辫子面包](examples/12-coconut-braided-bread/editorial.webp)](examples/12-coconut-braided-bread/) |

## 环境要求

- 支持图像生成的 ChatGPT 或 Codex
- Python 3.10 或更高版本
- Pillow，用于确定性地完成最终合成

安装 Python 依赖：

```bash
python3 -m pip install -r requirements.txt
```

## 安装到 Codex

让 Codex 从 GitHub 路径安装这个 skill：

```text
Use $skill-installer to install bakery-abstract-editorial from https://github.com/YiYinYinguu/bakery-abstract-editorial/tree/main/skills/bakery-abstract-editorial
```

本地开发时，可以将 `skills/bakery-abstract-editorial` 链接到你的用户 skill 目录。

## 使用方法

提供一张烘焙照片，并使用类似下面的请求调用 skill：

```text
使用 $bakery-abstract-editorial 将这张酸面包照片转化为平衡、可辨识的抽象编辑设计。
```

工作流会先生成并检查抽象面板，只有在面板获得认可后，才会将其与未经生成式替换的原始照片合成。

合成脚本输出无损 PNG。`examples/` 中的最终合成图使用 WebP，仅用于减小仓库预览体积；把 PNG 转为 WebP 属于展示环节，并非 skill 的必要步骤。

## 本地校验

安装开发依赖并运行仓库检查：

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
```

检查内容包括 skill 元数据、reference 链接、示例完整性和隐私元数据、标准图片尺寸，以及一次真实合成。GitHub Actions 会在 Python 3.10 和 3.13 上运行同一套检查。

## 仓库结构

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

## 许可证

Skill 的代码和文档采用 MIT 许可证。示例照片、抽象面板和编辑合成图不包含在 MIT 许可证中；详情见 [`examples/ASSET-LICENSE.md`](examples/ASSET-LICENSE.md)。
