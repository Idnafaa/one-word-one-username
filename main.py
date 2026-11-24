#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes the entrant's own make.fun handle, exactly one word, to
/output/entry.txt for the judge to read.
"""

import os

HANDLE = "idnafa-a"
OUTPUT_PATH = "/output/entry.txt"


def entry_text() -> str:
    """Return the single-word username, trimmed to one token."""
    word = HANDLE.strip()
    assert " " not in word and 1 <= len(word) <= 30, "handle must be one word"
    return word


def main() -> None:
    text = entry_text()
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle_file:
        handle_file.write(text)
    # Confirm what landed on disk is exactly the one word, no newline.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle_file:
        assert handle_file.read() == text
    print(text)


if __name__ == "__main__":
    main()
