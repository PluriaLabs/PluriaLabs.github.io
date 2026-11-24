#!/usr/bin/env python3
"""Print the app's own wording for the interface terms that occur in the given English source files.
Usage: python3 -I Scripts/glossary_for.py LANG FILE [FILE ...]"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
lang = sys.argv[1]
text = "\n".join(pathlib.Path(f).read_text(encoding="utf-8") for f in sys.argv[2:])
for line in (ROOT / "src/i18n/_glossary" / f"{lang}.tsv").read_text(encoding="utf-8").splitlines():
    if line.split("\t")[0] in text:
        print(line)
