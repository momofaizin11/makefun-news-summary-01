#!/usr/bin/env python3
"""Entry for make.fun news-summary-01: writes the day's world-news summary.

The summary is held in this repository (summary.txt) so the program is
deterministic: two runs write exactly the same bytes, and nothing touches
the network.
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path("/output/entry.txt")


def main() -> None:
    text = (HERE / "summary.txt").read_text(encoding="utf-8")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
