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
    if not 1 <= len(line.encode("utf-8")) <= 200:
        raise ValueError("Line must be 1-200 characters (UTF-8).")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("Line must be a single sentence.")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
