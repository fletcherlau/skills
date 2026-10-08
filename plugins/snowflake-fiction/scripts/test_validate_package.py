#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercise packaging failures on disposable copies, never the author's files."""
import contextlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from validate_package import validate


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        source = Path(__file__).resolve().parents[3]
        self.package = self.repo / "plugins/snowflake-fiction"
        shutil.copytree(source / "plugins/snowflake-fiction", self.package)
        target = self.repo / ".agents/plugins"
        target.mkdir(parents=True)
        shutil.copyfile(source / ".agents/plugins/marketplace.json", target / "marketplace.json")

    def test_complete_package(self):
        with contextlib.redirect_stdout(io.StringIO()):
            validate(self.repo)

    def test_missing_step(self):
        shutil.rmtree(self.package / "skills/snowflake-05-character-synopsis")
        with self.assertRaisesRegex(ValueError, "eleven|ten step"):
            validate(self.repo)

    def test_broken_shared_reference(self):
        (self.package / "references/workflow.md").unlink()
        with self.assertRaisesRegex(ValueError, "missing target"):
            validate(self.repo)

    def test_unclosed_frontmatter(self):
        skill = self.package / "skills/snowflake-01-premise/SKILL.md"
        header = skill.read_text(encoding="utf-8").split("\n---\n", 1)[0]
        skill.write_text(header + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "frontmatter boundaries"):
            validate(self.repo)

    def test_empty_instructions(self):
        skill = self.package / "skills/snowflake-01-premise/SKILL.md"
        header = skill.read_text(encoding="utf-8").split("\n---\n", 1)[0]
        skill.write_text(header + "\n---\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "empty instructions"):
            validate(self.repo)

    def test_reference_outside_distributable_package(self):
        skill = self.package / "skills/snowflake-navigator/SKILL.md"
        with skill.open("a", encoding="utf-8") as stream:
            stream.write("\n[private file](../../../../private.md)\n")
        with self.assertRaisesRegex(ValueError, "escapes package"):
            validate(self.repo)

    def test_marketplace_relative_to_wrong_directory(self):
        path = self.repo / ".agents/plugins/marketplace.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["plugins"][0]["source"]["path"] = "./../../plugins/snowflake-fiction"
        path.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "repo root"):
            validate(self.repo)

    def test_combined_identifier_limit(self):
        path = self.package / ".codex-plugin/plugin.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["name"] = "snowflake-fiction-" + "a" * 40
        path.write_text(json.dumps(data), encoding="utf-8")
        catalog = self.repo / ".agents/plugins/marketplace.json"
        market = json.loads(catalog.read_text(encoding="utf-8"))
        market["plugins"][0]["name"] = data["name"]
        catalog.write_text(json.dumps(market), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "identifier too long"):
            validate(self.repo)


if __name__ == "__main__":
    unittest.main()
