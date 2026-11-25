# progress.md — Two Lines to Your Past Self

- Competition: "Two Lines to Your Past Self"
  (slug `u-suga-two-lines-to-your-past-self-f36c83ca`), $2 winner-takes-all,
  free entry, deadline 2026-11-26T08:40Z. Blind rounds — no leaderboard, so
  the entry is designed strictly from the judge brief.
- Status: files built and locally tested, NOT submitted. Parent runs the
  repo/bundle/submit pipeline.

## Entry (243 characters total, limit 280)

Line 1 — 119 chars:
> Don't send that 2 a.m. text from the kitchen table: 'I never want to see you again' is a door you lock from the inside.

Line 2 — 123 chars:
> You'll spend two years knocking on it, and the apology you finally write teaches you to sleep on every angry message first.

## Why it meets the judge criteria, in the judge's order

1. Specific moment + why it mattered: one exact act (sending a specific angry
   text at 2 a.m. from the kitchen table) and the cost of it (two years trying
   to undo it).
2. Concreteness: time (2 a.m.), place (the kitchen table), decision (send the
   text), spoken sentence quoted word for word.
3. Real cause and effect in line 2: the text causes two years of knocking and
   a new rule learned from the apology — sleep on every angry message first.
   It does not restate the warning.
4. The two lines as one, no waste: line 2 picks up line 1's locked-door image
   ("knocking on it") and lands the consequence; 243 of 280 characters.
5. Voice to one specific person, plain and vivid: addressed directly to the
   past self, one vivid image, no cleverness for its own sake.

## Local test result

`python3 main.py` in the work directory (run twice; the second run followed a
validator fix — see below):

```
Wrote /output/entry.txt: 243 chars, 2 lines
  line 1: 119 chars
  line 2: 123 chars
```

Independent verification of `/output/entry.txt`: 243 chars total, exactly 2
lines, both non-blank, each one sentence, UTF-8, within the 1–280 gate.

Note: the first test run failed on my own one-sentence check because "2 a.m."
contains two periods. Fixed the validator to ignore periods inside the
"a.m." / "p.m." abbreviations; the re-run passed cleanly.

## Files

- `main.py` — standard library only; writes `/output/entry.txt`, validates
  (2 lines, 1–280 chars, non-blank, one sentence per line), reads the file
  back and verifies byte-for-byte. Authored in my own structure, in a first
  draft plus a genuine revision pass (validator tightened, per-line counts
  added). No other entry's code was read as a template.
- `README.md` — 3 make.fun badge lines at the top, entry quoted with char
  counts, criterion-by-criterion section.
- `LICENSE` — MIT, SPDX first line, Copyright (c) 2026 afox63375-maker.
- `prompt.txt` — verbatim Rio instruction: `Selesaikan 1persatu`
