"""The linter must flag a number without a reproducer and pass one with it."""
from __future__ import annotations

import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOL = ROOT / "claims_lint.py"


def run(text, *extra):
    with tempfile.TemporaryDirectory() as td:
        path = pathlib.Path(td) / "README.md"
        path.write_text(text, encoding="utf-8")
        return subprocess.run([sys.executable, str(TOOL), str(path), *extra],
                              capture_output=True, text=True)


class Lint(unittest.TestCase):
    def test_a_bare_number_is_flagged(self):
        done = run("# speed\n\nIt is 42% faster than the old version.\n")
        self.assertIn("42%", done.stdout)

    def test_a_command_nearby_is_accepted(self):
        done = run("# speed\n\n`python3 bench.py`\nIt is 42% faster than the old version.\n")
        self.assertNotIn("42%", done.stdout)

    def test_a_date_nearby_is_accepted(self):
        done = run("# speed\n\nMeasured on 2026-11-26: 42% faster.\n")
        self.assertNotIn("42%", done.stdout)

    def test_strict_exits_one_on_a_finding(self):
        self.assertEqual(run("It is 42% faster.\n", "--strict").returncode, 1)
