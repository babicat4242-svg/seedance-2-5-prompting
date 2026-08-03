from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class RevisionContractTests(unittest.TestCase):
    def test_skill_requires_canonical_recompile(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("## Multi-turn revision compiler", skill)
        self.assertIn("latest user instruction", skill)
        self.assertIn("never append revision history", skill)
        self.assertIn("one complete replacement prompt", skill)

    def test_revision_reference_defines_all_operations(self) -> None:
        reference = (
            ROOT / "references" / "revision-workflow.md"
        ).read_text(encoding="utf-8")

        for operation in (
            "ADD",
            "REPLACE",
            "DELETE",
            "REORDER",
            "RETIME",
            "PRESERVE",
            "RESET",
        ):
            self.assertIn(f"`{operation}`", reference)

    def test_revision_reference_covers_dependency_cleanup(self) -> None:
        reference = (
            ROOT / "references" / "revision-workflow.md"
        ).read_text(encoding="utf-8")

        self.assertIn("## Dependency cleanup", reference)
        self.assertIn("## Camera recompile", reference)
        self.assertIn("## Worked revision cases", reference)

    def test_prompt_patterns_exposes_revision_recompilation(self) -> None:
        patterns = (
            ROOT / "references" / "prompt-patterns.md"
        ).read_text(encoding="utf-8")

        self.assertIn("## Revision recompilation pattern", patterns)
        self.assertIn("Retired values", patterns)
        self.assertIn("Canonical active brief", patterns)


if __name__ == "__main__":
    unittest.main()
