from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "bakery-abstract-editorial"
EXAMPLES_DIR = ROOT / "examples"
COMPOSE_SCRIPT = SKILL_DIR / "scripts" / "compose_editorial.py"


class SkillTests(unittest.TestCase):
    def test_skill_frontmatter(self) -> None:
        content = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")

        frontmatter = yaml.safe_load(match.group(1))
        self.assertIsInstance(frontmatter, dict)
        self.assertEqual(frontmatter["name"], SKILL_DIR.name)
        self.assertRegex(frontmatter["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(frontmatter["name"]), 64)
        self.assertTrue(frontmatter["description"].strip())
        self.assertLessEqual(len(frontmatter["description"]), 1024)
        self.assertNotRegex(frontmatter["description"], r"[<>]")
        self.assertEqual(
            set(frontmatter) - {"name", "description", "license", "allowed-tools", "metadata"},
            set(),
        )
        self.assertNotIn("[TODO:", content)

    def test_openai_metadata(self) -> None:
        metadata = yaml.safe_load(
            (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
        )
        interface = metadata["interface"]
        self.assertGreaterEqual(len(interface["short_description"]), 25)
        self.assertLessEqual(len(interface["short_description"]), 64)
        self.assertIn("$bakery-abstract-editorial", interface["default_prompt"])

    def test_references_linked_from_skill_exist(self) -> None:
        content = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        links = re.findall(r"\[[^]]+\]\((references/[^)]+)\)", content)
        self.assertTrue(links)
        for link in links:
            self.assertTrue((SKILL_DIR / link).is_file(), link)


class ExampleTests(unittest.TestCase):
    def test_examples_are_complete_and_sanitized(self) -> None:
        folders = sorted(EXAMPLES_DIR.glob("[0-9][0-9]-*"))
        self.assertEqual(len(folders), 14)

        for folder in folders:
            source = folder / "source.jpg"
            panel = folder / "abstract-panel.png"
            editorial = folder / "editorial.webp"
            for artifact in (source, panel, editorial):
                self.assertTrue(artifact.is_file(), artifact)

            with Image.open(source) as image:
                self.assertEqual(len(image.getexif()), 0, source)
                self.assertTrue(image.info.get("icc_profile"), source)
                for private_key in ("xmp", "XML:com.adobe.xmp", "photoshop", "iptc"):
                    self.assertNotIn(private_key, image.info, source)

            with Image.open(panel) as image:
                self.assertEqual(image.size, (1536, 1024), panel)
                self.assertEqual(len(image.getexif()), 0, panel)

            with Image.open(editorial) as image:
                self.assertEqual(image.size, (1024, 1536), editorial)
                self.assertEqual(len(image.getexif()), 0, editorial)

    def test_use_case_screenshots_are_sanitized(self) -> None:
        screenshots = EXAMPLES_DIR / "use-cases"
        expected = {
            "baking-timeline.png": (1292, 1350),
            "baking-calendar.png": (1856, 1530),
        }

        self.assertEqual(
            {path.name for path in screenshots.glob("*.png")}, set(expected)
        )
        for filename, size in expected.items():
            screenshot = screenshots / filename
            with Image.open(screenshot) as image:
                self.assertEqual(image.size, size, screenshot)
                self.assertEqual(len(image.getexif()), 0, screenshot)


class CompositionTests(unittest.TestCase):
    def test_composes_real_example(self) -> None:
        example = EXAMPLES_DIR / "01-rustic-loaf"
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "editorial.png"
            result = subprocess.run(
                [
                    sys.executable,
                    str(COMPOSE_SCRIPT),
                    "--source",
                    str(example / "source.jpg"),
                    "--panel",
                    str(example / "abstract-panel.png"),
                    "--out",
                    str(output),
                ],
                capture_output=True,
                check=False,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            with Image.open(output) as image:
                self.assertEqual(image.format, "PNG")
                self.assertEqual(image.size, (1024, 1536))
                self.assertEqual(image.mode, "RGB")


if __name__ == "__main__":
    unittest.main()
