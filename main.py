#!/usr/bin/env python3
"""Entry for make.fun news-summary-01: writes the day's world-news summary.

The summary is held in this repository (summary.txt) so the program is
deterministic: two runs write exactly the same bytes, and nothing touches
the network.

The file is copied as raw bytes (no text-mode decoding, no newline
translation), which guarantees /output/entry.txt is a byte-for-byte copy of
summary.txt on every run, on any platform.

The text is validated before anything is written: it must hold at least one
character of text and at most MAX_CHARS characters. A summary that is empty
(or whitespace only) or too long is refused with a SystemExit, so a bad
summary can never overwrite a good /output/entry.txt.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "summary.txt"
OUT = Path("/output/entry.txt")

MIN_CHARS = 1
MAX_CHARS = 2000


def build_entry(src: Path = SRC, out: Path = OUT) -> Path:
    """Validate ``src`` and copy it byte for byte to ``out``.

    Returns the path that was written. Raises SystemExit (without touching
    ``out``) when the text is empty or longer than MAX_CHARS characters.
    """
    data = src.read_bytes()
    text = data.decode("utf-8")
    chars = len(text)

    if not text.strip():
        raise SystemExit(
            f"refusing to write {out}: {src} is empty (no text), entry must "
            f"hold {MIN_CHARS}..{MAX_CHARS} characters"
        )
    if chars > MAX_CHARS:
        raise SystemExit(
            f"refusing to write {out}: {src} holds {chars} characters, entry "
            f"must hold {MIN_CHARS}..{MAX_CHARS} characters"
        )

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    print(f"wrote {out} ({chars} characters, {len(data)} bytes)")
    return out


def main() -> Path:
    """Write the day's entry and return the path of the file written."""
    return build_entry()


if __name__ == "__main__":
    main()
