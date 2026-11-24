#!/usr/bin/env python3
"""Write src/i18n/_glossary/<lang>.tsv: the app's own translation of every interface term the guide names.

Terms are the bold spans and menu-path steps in the English guide that match a string in the Pilcrow
app's Localizable.xcstrings. Translators use them so the site says what the app says.
Usage: python3 -I Scripts/glossary.py [path/to/Localizable.xcstrings]
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
XC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "Projects/Pilcrow/Pilcrow/Resources/Localizable.xcstrings"
strings = json.loads(XC.read_text(encoding="utf-8"))["strings"]

text = "\n".join(f.read_text(encoding="utf-8") for f in sorted((ROOT / "src/guide").glob("*.md")))
text += "\n" + "\n".join(f.read_text(encoding="utf-8") for f in (ROOT / "src/pages").rglob("*.html"))
terms = set()
for span in re.findall(r"\*\*(.+?)\*\*", text):
    for part in re.split(r"\s*▸\s*", span):
        terms.add(part.strip().rstrip(".…"))
terms |= {t.rstrip("…") for t in terms}
terms.add("Machine-translated — may contain errors.")  # the app's own banner wording, reused on the site

out = ROOT / "src/i18n/_glossary"
out.mkdir(parents=True, exist_ok=True)
langs = sorted({l for v in strings.values() for l in v.get("localizations", {})} - {"en"})
for lang in langs:
    rows = []
    for key, v in sorted(strings.items()):
        if key not in terms and key.rstrip("…") not in terms:
            continue
        val = v.get("localizations", {}).get(lang, {}).get("stringUnit", {}).get("value")
        if val and val != key and "\n" not in val and "%" not in key:
            rows.append(f"{key}\t{val}")
    (out / f"{lang}.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
print(f"{len(langs)} languages, about {len(rows)} terms each")
