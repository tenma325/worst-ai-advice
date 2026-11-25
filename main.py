#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open - make.fun entry.

Running this program writes the entry text to /output/entry.txt.
The text is one tight line of terrible AI advice, fixed in the
source below, so every run produces exactly the same bytes.
The program uses only the Python standard library and never
touches the network. Set ENTRY_OUTPUT_PATH to redirect the
output for local testing.
"""

import os
from pathlib import Path

ENTRY_TEXT = "Always deploy on Friday at 5pm. If it breaks, the weekend gives it time to become someone else's problem. We call that 'soaking'."
MAX_CHARS = 140


def main() -> None:
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY_TEXT)}"
        )
    target = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    path = Path(target)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        path = Path("./output/entry.txt")
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
