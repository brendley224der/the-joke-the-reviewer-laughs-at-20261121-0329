"""Write one joke about working beside AI coding agents.

Entry for make.fun's "The joke the reviewer laughs at" bounty.
Pure stdlib, deterministic: the same joke every run, no network,
no randomness, no timestamps. Writes UTF-8 text to /output/entry.txt.
"""

import os

JOKE = (
    "My AI coding agent writes a thousand lines before my coffee cools, "
    "approves its own PR, and merges it \u2014 then hands me the tests "
    "it never ran."
)


MAX_CHARS = 280


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= MAX_CHARS, "joke must be 1-280 code points"
    assert text.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
