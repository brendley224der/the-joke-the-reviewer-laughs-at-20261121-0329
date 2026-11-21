#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. Pure standard library, deterministic, no network.
"""

import os
import sys

JOKE = (
    "My AI coding agent writes a thousand lines before my coffee cools, "
    "approves its own PR, and merges it \u2014 then hands me the tests "
    "it never ran."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    joke = JOKE.strip()
    if not joke:
        print("error: joke is empty", file=sys.stderr)
        return 1
    if "\n" in joke or "\r" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(joke) <= 280:
        print(f"error: joke is {len(joke)} code points, must be 1-280",
              file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke + "\n")

    # Improvement: read the file back and verify it round-trips exactly,
    # so a silent write failure can never pass as success.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != joke + "\n":
        print("error: written output does not match the joke", file=sys.stderr)
        return 1

    print(f"wrote {len(joke)}-character joke to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
