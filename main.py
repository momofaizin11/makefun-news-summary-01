#!/usr/bin/env python3
"""Entry for make.fun news-summary-01: writes the day's world-news summary.

The summary is held in this repository (summary.txt) so the program is
deterministic: two runs write exactly the same bytes, and nothing touches
the network.

The file is copied as raw bytes (no text-mode decoding, no newline
translation), which guarantees /output/entry.txt is a byte-for-byte copy of
summary.txt on every run, on any platform.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "summary.txt"
OUT = Path("/output/entry.txt")

MIN_CHARS = 1
MAX_CHARS = 2000


def main() -> None:
    data = SRC.read_bytes()
    chars = len(data.decode("utf-8"))
    if not MIN_CHARS <= chars <= MAX_CHARS:
        raise ValueError(
            f"summary.txt holds {chars} characters, entry must be "
            f"{MIN_CHARS}..{MAX_CHARS}: {SRC}"
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(data)
    print(f"wrote {OUT} ({chars} characters, {len(data)} bytes)")


if __name__ == "__main__":
    main()
