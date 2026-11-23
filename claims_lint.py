#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""claims_lint — no number without a command, a date and an N.

Flags a line that states a measured number (%, ms, pass rate, x faster, n=) unless somewhere
within +-4 lines there is a reproducer (a command), a date, an explicit N, a "Source:",
or the line already says the number is not reproducible.

Usage: python3 claims_lint.py README.md [more.md ...] [--strict]
Exit: 0 clean, 1 findings (only with --strict), always prints findings.
"""
import re
import sys

NUM = re.compile(r"(\d[\d.,]*\s*%|\d[\d.,]*\s*(ms|µs|us|s)\b|\bpass rate\b|\d+\s*x\s*(faster|brže)|\bn\s*=\s*\d+|accuracy|hit rate)", re.I)
PROOF = re.compile(r"(`[^`]*(python|make|\./|bash|pytest|curl|gh |sbatch)[^`]*`|```|Source:|source:|izmjereno|measured on|\b20\d\d-\d\d-\d\d\b|\bn\s*=\s*\d+|not reproduc|nije reproduc)", re.I)


def check(path, window=4):
    out = []
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    for i, line in enumerate(lines):
        if not NUM.search(line):
            continue
        lo, hi = max(0, i - window), min(len(lines), i + window + 1)
        if PROOF.search("\n".join(lines[lo:hi])):
            continue
        out.append((i + 1, line.strip()[:150]))
    return out


def main(argv):
    strict = "--strict" in argv
    files = [a for a in argv if not a.startswith("-")]
    total = 0
    for f in files:
        found = check(f)
        total += len(found)
        if found:
            print(f"\n### {f}  ({len(found)} bez dokaza)")
            for ln, txt in found:
                print(f"  {ln}: {txt}")
    print(f"\nukupno: {total} linija bez komande/datuma/N u {len(files)} fajlova")
    return 1 if (strict and total) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
