#!/usr/bin/env python3
"""One Line of Wonder.

Writes a single line to /output/entry.txt and prints it.
Entry for the make.fun bounty
u-pangg7-one-line-of-wonder-ee10fcd8.
"""

import os

ENTRY = (
    "Tonight, light from a star that died before the first human opened "
    "an eye is landing on a sleeping child's eyelid."
)


def main() -> None:
    # Gate: /output/entry.txt must be 1-200 chars of UTF-8 text.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, outside the 1-200 gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
