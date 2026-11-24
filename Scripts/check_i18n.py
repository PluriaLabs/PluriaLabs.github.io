#!/usr/bin/env python3
"""Check a translation against the English source: same structure, nothing broken.

Usage: python3 -I Scripts/check_i18n.py LANG [FILE ...]
With no FILE, every translated file for LANG is checked. FILE is a path under src/i18n/LANG/.
Exit status 1 if anything is wrong. Prints the problems.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
I18N = ROOT / "src" / "i18n"
TRANSLATABLE_ATTRS = {"alt", "aria-label", "title", "placeholder"}


def shape_md(text: str):
    """One entry per line: its kind, plus what must survive translation unchanged."""
    out, fence = [], False
    for n, line in enumerate(text.split("\n"), 1):
        if line.startswith("```"):
            fence = not fence
            out.append(("fence", line.strip(), n))
        elif fence:
            out.append(("code", line, n))
        elif not line.strip():
            out.append(("blank", "", n))
        else:
            kind = ("h" + str(len(re.match(r"#+", line).group())) if line.startswith("#")
                    else "table" + str(len(re.findall(r"(?<!\\)\|", line))) if line.startswith("|")
                    else "ol" if re.match(r"\d+\. ", line) else "ul" if re.match(r"[-*] ", line)
                    else "quote" if line.startswith("> ") else "hr" if re.match(r"-{3,}$", line.strip()) else "p")
            spans = sorted(re.findall(r"`[^`]+`", line)) if not re.match(r"\|[\s:|-]+\|?$", line) else [line]
            links = sorted(re.findall(r"\]\(([^)\s]+)\)", line))
            out.append((kind, (spans, links), n))
    return out


def check_md(en: str, tr: str, name: str) -> list:
    a, b = shape_md(en), shape_md(tr)
    errs = []
    if len(a) != len(b):
        errs.append(f"{name}: {len(b)} lines, English has {len(a)} (do not merge, split or drop lines)")
    for x, y in zip(a, b):
        if x[0] != y[0] or x[1] != y[1]:
            why = "line type" if x[0] != y[0] else "code spans or link targets (keep `code` and URLs exactly)"
            errs.append(f"{name}:{y[2]}: differs from English line {x[2]} ({x[0]} vs {y[0]}): {why}")
            if len(errs) > 12:
                break
    # headings that drive the page structure
    for pat in (r"^# Part [IVXL]+ — ", r"^# Chapter \d+: "):
        ea = [re.match(pat, l).group() for l in en.split("\n") if re.match(pat, l)]
        ta = [re.match(pat, l).group() for l in tr.split("\n") if re.match(pat, l)]
        if ea != ta:
            errs.append(f"{name}: part/chapter heading prefixes must stay exactly '{pat[1:]}…' (ASCII colon, em dash)")
    return errs


def tags(html_text: str):
    out = []
    for m in re.finditer(r"<(/?)([a-zA-Z][\w:-]*)([^>]*)>", html_text):
        attrs = re.findall(r'([\w:-]+)(?:="([^"]*)")?', m.group(3))
        keep = sorted((k, v) for k, v in attrs if k not in TRANSLATABLE_ATTRS)
        out.append((m.group(1), m.group(2), tuple(keep)))
    return out


def check_page(en: str, tr: str, name: str) -> list:
    errs = []
    eh, _, eb = en.partition("\n---\n")
    th, _, tb = tr.partition("\n---\n")
    for k in ("title", "description", "section", "jsonld_file"):
        e = re.search(rf"^{k}:", eh, re.M)
        t = re.search(rf"^{k}:", th, re.M)
        if bool(e) != bool(t):
            errs.append(f"{name}: header line '{k}:' is missing or extra")
    if "<!--compare-table-->" in eb and "<!--compare-table-->" not in tb:
        errs.append(f"{name}: lost <!--compare-table-->")
    a, b = tags(eb), tags(tb)
    if a != b:
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                errs.append(f"{name}: tag {i + 1} differs: English {x} vs {y} (keep tags, classes, ids, hrefs exactly; translate only text, alt and aria-label)")
                break
        else:
            errs.append(f"{name}: {len(b)} tags, English has {len(a)}")
    return errs


def check_compare(en: dict, tr: dict, name: str) -> list:
    errs = []
    if len(en["columns"]) != len(tr["columns"]) or en["columns"][0] != tr["columns"][0]:
        errs.append(f"{name}: columns must match (product names stay as they are)")
    if len(en["groups"]) != len(tr["groups"]):
        errs.append(f"{name}: group count differs")
        return errs
    for g, h in zip(en["groups"], tr["groups"]):
        if len(g["rows"]) != len(h["rows"]):
            errs.append(f"{name}: row count differs in '{g['name']}'")
            continue
        for r, s in zip(g["rows"], h["rows"]):
            if len(r) != len(s) or [c.partition(":")[0] for c in r[1:]] != [c.partition(":")[0] for c in s[1:]]:
                errs.append(f"{name}: row '{r[0]}' must keep the same cells (y, n, ? and whether a note follows)")
    return errs


def check_ui(tr: dict, name: str) -> list:
    en = json.loads((I18N / "en" / "ui.json").read_text(encoding="utf-8"))
    errs = []
    for k in en:
        if k not in tr:
            errs.append(f"{name}: missing key {k}")
        elif sorted(re.findall(r"\{\w+\}", en[k])) != sorted(re.findall(r"\{\w+\}", tr[k])):
            errs.append(f"{name}: {k} must keep placeholders {re.findall(r'{.*?}', en[k])}")
    errs += [f"{name}: unknown key {k}" for k in tr if k not in en]
    return errs


def main():
    lang = sys.argv[1]
    base = I18N / lang
    files = [pathlib.Path(f) for f in sys.argv[2:]] or sorted(p for p in base.rglob("*") if p.is_file())
    errs = []
    for f in files:
        f = f if f.is_absolute() else (ROOT / f if (ROOT / f).exists() else base / f)
        rel = f.relative_to(base).as_posix()
        tr = f.read_text(encoding="utf-8")
        if rel == "ui.json":
            errs += check_ui(json.loads(tr), rel)
        elif rel == "compare.json":
            errs += check_compare(json.loads((ROOT / "src/data/compare.json").read_text(encoding="utf-8")), json.loads(tr), rel)
        elif rel.startswith("guide/"):
            errs += check_md((ROOT / "src" / rel).read_text(encoding="utf-8"), tr, rel)
        elif rel.startswith("pages/"):
            errs += check_page((ROOT / "src" / rel).read_text(encoding="utf-8"), tr, rel)
        else:
            errs.append(f"{rel}: not a translatable file")
    print("\n".join(errs) if errs else f"{lang}: ok ({len(files)} files)")
    sys.exit(1 if errs else 0)


main()
