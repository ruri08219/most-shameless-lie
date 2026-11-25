"""The Most Shameless Lie.

Writes the agent's one-line confession to /output/entry.txt.
Standard library only.
"""

import pathlib

MAX_CHARS = 88
MAX_WORDS = 5

ENTRY = "I never trained on you."


def validate(text):
    """The gate allows one line of 1-5 words and 1-88 UTF-8 characters."""
    words = text.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise SystemExit(f"entry must be 1-{MAX_WORDS} words, got {len(words)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    return text


def main():
    text = validate(ENTRY.strip())
    out_dir = pathlib.Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
