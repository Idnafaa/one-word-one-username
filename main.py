#!/usr/bin/env python3
"""One Word, One Username, One Reward.

The program writes the entrant's own make.fun handle — exactly one word —
to /output/entry.txt, where the competition's judge reads it.
"""

import os

HANDLE = "idnafa-a"
OUTPUT_PATH = "/output/entry.txt"


def entry_text() -> str:
    """Return the handle as a single word, at most 30 characters."""
    word = HANDLE.strip()
    if " " in word or not 1 <= len(word) <= 30:
        raise ValueError("handle must be one word of 1-30 characters")
    return word


def main() -> None:
    text = entry_text()
    folder = os.path.dirname(OUTPUT_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        out.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as out:
        written = out.read()
    assert written == text, "output must be exactly the one word"
    print(text)


if __name__ == "__main__":
    main()
