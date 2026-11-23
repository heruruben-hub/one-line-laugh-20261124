"""One-line laugh entry.

Assembles a single funny sentence from a setup and a punchline,
then writes it to /output/entry.txt.
"""

import os

SETUP = "I finally organized my photos into folders, and now I have 4,000 memories"
PUNCHLINE = "neatly sorted under names like 'New Folder (3)'."

LINE = f"{SETUP} {PUNCHLINE}"


def main() -> None:
    line = LINE.strip()
    if not line:
        raise ValueError("Line must not be empty or only whitespace.")
    if not 1 <= len(line) <= 200:
        raise ValueError("Line must be 1-200 characters.")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("Line must be a single sentence.")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("Written output does not match the built line.")


if __name__ == "__main__":
    main()
