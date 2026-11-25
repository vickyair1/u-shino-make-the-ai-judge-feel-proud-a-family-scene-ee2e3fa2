"""Write one short family scene to /output/entry.txt.

The scene is built from two parts, the way the moment itself is built:
a setup (the yearly ritual) and a punchline (the year the child
measures Dad back). A warm, funny, heartfelt domestic moment about
growing up and a father quietly proud of it.

Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters,
not only whitespace. The entry is validated before it is written.
"""

import os
import sys

# Setup: the ritual, repeated every birthday.
SETUP = (
    "Dad marks my height on the kitchen doorframe every birthday; "
    "this year I marked his \u2014 an inch lower \u2014 and he just smiled: "
)

# Punchline: the turn — Dad is shrinking, the child is grown, and
# Dad is delighted about it, because now the child can do the job
# only the tall one in the house could do.
PUNCHLINE = "'Good. Now you can reach the top shelf for me.'"

ENTRY = SETUP + PUNCHLINE

MAX_CHARS = 280


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, TypeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
