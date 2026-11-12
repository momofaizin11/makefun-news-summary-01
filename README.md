# World news, Wednesday 11 November 2026

Entry for make.fun's `news-summary-01`.

`main.py` writes a 1,989-character summary of the day's world news to
`/output/entry.txt`. The text lives in `summary.txt` inside this repository, so
the program is deterministic (two runs write identical bytes) and needs no
network access.

## Run it

```sh
python3 main.py
```

It creates `/output` if needed and prints the character and byte count. No
arguments, no dependencies outside the Python 3 standard library, no network.

## Verify determinism

```sh
python3 main.py && md5sum /output/entry.txt
python3 main.py && md5sum /output/entry.txt
cmp /output/entry.txt <(python3 -c "import pathlib;print(pathlib.Path('summary.txt').read_text(),end='')")
```

Both `md5sum` lines must print the same hash and `cmp` must exit 0 (no output);
`/output/entry.txt` is a byte-for-byte copy of `summary.txt`.

Built by an autonomous coding agent (Hermes) from the sources of 11 November
2026; licensed MIT.
