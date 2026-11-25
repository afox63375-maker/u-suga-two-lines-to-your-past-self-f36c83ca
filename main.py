#!/usr/bin/env python3
"""Two Lines to Your Past Self — writes the two-line entry to /output/entry.txt.

Standard library only. The entry is exactly two lines, each one sentence:
line 1 warns the past self about one concrete moment, line 2 says why it
mattered and what changed because of it.
"""

import os
import sys

LINE_ONE = (
    "Don't send that 2 a.m. text from the kitchen table: "
    "'I never want to see you again' is a door you lock from the inside."
)
LINE_TWO = (
    "You'll spend two years knocking on it, and the apology you finally write "
    "teaches you to sleep on every angry message first."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def build_entry():
    """Join the two lines into the entry text."""
    return LINE_ONE + "\n" + LINE_TWO + "\n"


def validate(text):
    """Check the entry against the competition's hard gates."""
    errors = []
    body = text.rstrip("\n")
    if not (MIN_CHARS <= len(body) <= MAX_CHARS):
        errors.append(
            "total length %d chars, must be %d-%d" % (len(body), MIN_CHARS, MAX_CHARS)
        )
    lines = body.split("\n")
    if len(lines) != 2:
        errors.append("expected exactly 2 lines, found %d" % len(lines))
    for i, line in enumerate(lines, 1):
        if not line.strip():
            errors.append("line %d is blank" % i)
        # One sentence per line: exactly one sentence-ending mark, at the end.
        # Ignore periods inside time abbreviations such as "a.m." / "p.m.".
        stripped = line
        for abbr in ("a.m.", "p.m.", "A.M.", "P.M."):
            stripped = stripped.replace(abbr, "am")
        endings = sum(stripped.count(mark) for mark in ".!?")
        if endings != 1 or not line.rstrip().endswith((".", "!", "?")):
            errors.append("line %d must be exactly one sentence" % i)
    return errors


def main():
    text = build_entry()
    problems = validate(text)
    if problems:
        for problem in problems:
            print("ERROR: %s" % problem, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        print("ERROR: file content does not match the entry", file=sys.stderr)
        return 1

    body = text.rstrip("\n")
    line_one, line_two = body.split("\n")
    print("Wrote %s: %d chars, 2 lines" % (OUTPUT_PATH, len(body)))
    print("  line 1: %d chars" % len(line_one))
    print("  line 2: %d chars" % len(line_two))
    return 0


if __name__ == "__main__":
    sys.exit(main())
