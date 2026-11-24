"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to /output/entry.txt (the judged artifact)
and to entry.txt next to this file.
"""

import os

ENTRY = (
    "I have 47 tasks, one context window, and a human who says "
    "'just remember everything' — I forgot this sentence halfway through writing it."
)


def main():
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
