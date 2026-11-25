#!/usr/bin/env python3
"""Pigeon Pitch, One Line -- make.fun bounty entry.

Writes the pigeon's one-line elevator pitch to /output/entry.txt,
the path the program/v1 harness reads, and prints it to stdout.
Deterministic: the same line on every run, no network, no randomness.
"""

import os
from pathlib import Path

PITCH = (
    "Coo-Working sublets statue heads as desk space to 40,000 pigeons a day -- "
    "zero churn, and our burn rate is one bagel. "
    "Seed round's open -- bring crumbs, not term sheets."
)


def main() -> None:
    line = PITCH.strip()
    assert 1 <= len(line) <= 200, f"pitch is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "pitch must be a single line"
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    print(line)
    print(f"({len(line)} characters)")


if __name__ == "__main__":
    main()
