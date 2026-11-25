#!/usr/bin/env python3
"""Build the Pluria Labs site.

Usage:  python3 -I Scripts/build.py [--policies DIR] [--guide FILE]

Reads  src/pages/**/*.html   (a small header, a line of three dashes, then the body),
the privacy policies (Markdown, one per language) from the Policies repo, and the
Pilcrow User Guide (Markdown files in src/guide/, joined in file-name order), and writes plain HTML
next to them in the repo root, plus sitemap.xml, robots.txt and the guide's search index.
GitHub Pages serves the result as it is; there is no other build step.
"""
import argparse
import html
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "pages"
HOME = pathlib.Path.home() / "Projects"
POLICIES = HOME / "Policies and Licenses" / "Pilcrow"
GUIDE = ROOT / "src" / "guide"
SITE = "https://plurialabs.github.io"
EMAIL = "support@plurialabs.com"

# Shipped languages (Pilcrow/App/AppLanguage.swift), code -> native name.
LANGS = [
    ("en", "English"), ("es", "Español"), ("fr", "Français"), ("de", "Deutsch"), ("it", "Italiano"),
    ("pt-BR", "Português (Brasil)"), ("nl", "Nederlands"), ("ru", "Русский"), ("ja", "日本語"),
    ("ko", "한국어"), ("zh-Hans", "简体中文"), ("zh-Hant", "繁體中文"), ("ar", "العربية"), ("da", "Dansk"),
    ("hi", "हिन्दी"), ("id", "Bahasa Indonesia"), ("nb", "Norsk bokmål"), ("pl", "Polski"),
    ("sv", "Svenska"), ("th", "ไทย"), ("tr", "Türkçe"), ("uk", "Українська"), ("vi", "Tiếng Việt"),
]
RTL = {"ar"}
I18N = ROOT / "src" / "i18n"
CODES = [c for c, _ in LANGS]
NATIVE = dict(LANGS)
_UI = {}


def ui(lang: str) -> dict:
    """Interface strings for a language, with English filling any gap."""
    if lang not in _UI:
        data = json.loads((I18N / "en" / "ui.json").read_text(encoding="utf-8"))
        f = I18N / lang / "ui.json"
        if lang != "en" and f.exists():
            data.update(json.loads(f.read_text(encoding="utf-8")))
        _UI[lang] = data
    return _UI[lang]


def prefix(lang: str, path: str) -> str:
    """The URL of an English-site path in another language: /pilcrow/ becomes /es/pilcrow/."""
    return path if lang == "en" else f"/{lang}{path}"


def privacy_url(code: str) -> str:
    return "/pilcrow/privacy.html" if code == "en" else f"/pilcrow/privacy/{code}.html"


def localize(markup: str, lang: str) -> str:
    """Point root-relative links at the language's own copy of the site."""
    if lang == "en":
        return markup

    def fix(m):
        url = m.group(2)
        if url.startswith("//") or url.startswith(("/assets/", "/pilcrow/assets/", "/pilcrow/privacy")):
            return m.group(0)
        if url.split("#")[0] == "/pilcrow/privacy.html":
            return m.group(1) + privacy_url(lang) + url[len("/pilcrow/privacy.html"):] + m.group(3)
        return m.group(1) + prefix(lang, url) + m.group(3)

    return re.sub(r'(href=")(/[^"]*)(")', fix, markup)


LAYOUT = """<!doctype html>
<html lang="{lang}"{dir}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
{alternates}<meta name="theme-color" content="#f6f1e7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121819" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Pluria Labs">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{locale}">
<meta property="og:image" content="{site}/pilcrow/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/pilcrow/assets/favicon.svg">
<link rel="icon" type="image/png" href="/pilcrow/assets/favicon.png">
<link rel="apple-touch-icon" href="/pilcrow/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/site.css">
{jsonld}</head>
<body>
<a class="skip" href="#main">{skip}</a>
{header}
<main id="main">
{notice}{body}
</main>
{footer}
<script src="/assets/site.js" defer></script>
{extra}</body>
</html>
"""

GLOBE = ('<svg class="globe" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" '
         'stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/>'
         '<path d="M3 12h18M12 3c2.6 2.7 3.9 5.7 3.9 9s-1.3 6.3-3.9 9c-2.6-2.7-3.9-5.7-3.9-9s1.3-6.3 3.9-9z"/></svg>')


def lang_menu(lang: str, key: str) -> str:
    """The language chooser: a plain <details> list, so it needs no script. key is the English path."""
    items = []
    for code, native in LANGS:
        url = privacy_url(code) if key.startswith("/pilcrow/privacy") else prefix(code, key)
        cur = ' aria-current="true"' if code == lang else ""
        items.append(f'<li><a href="{url}" hreflang="{code}" lang="{code}" data-lang="{code}"{cur}>{native}</a></li>')
    return (f'<details class="lang-menu"><summary aria-label="{html.escape(ui(lang)["lang_menu"], quote=True)}">{GLOBE}'
            f'<span lang="{lang}">{NATIVE[lang]}</span></summary><ul>{"".join(items)}</ul></details>')


def header(lang: str, key: str, section: str) -> str:
    t = ui(lang)
    cur = ' aria-current="page"'
    menu = lang_menu(lang, key)
    if section == "labs":
        return localize(f"""<header class="site-header">
<div class="wrap">
<a class="brand" href="/" aria-label="{html.escape(t['labs_aria'], quote=True)}">Pluria Labs</a>
<div class="hdr-end"><nav class="nav" aria-label="{html.escape(t['nav_aria'], quote=True)}">
<a class="keep" href="/pilcrow/">Pilcrow</a>
<a href="/pilcrow/support.html">{t['nav_support']}</a>
<a href="https://github.com/PluriaLabs">{t['nav_github']}</a>
</nav>MENU</div>
</div>
</header>""", lang).replace("MENU", menu)
    return localize(f"""<header class="site-header">
<div class="wrap">
<a class="brand" href="/pilcrow/" aria-label="{html.escape(t['brand_aria'], quote=True)}"><img class="mark" src="/assets/logo-mark.svg" alt="" width="32" height="38">Pilcrow</a>
<div class="hdr-end"><nav class="nav" aria-label="{html.escape(t['nav_aria'], quote=True)}">
<a href="/pilcrow/#features">{t['nav_features']}</a>
<a class="keep" href="/pilcrow/guide/"{cur if key.startswith("/pilcrow/guide/") else ""}>{t['nav_guide']}</a>
<a href="/pilcrow/compare.html"{cur if key == "/pilcrow/compare.html" else ""}>{t['nav_compare']}</a>
<a href="/pilcrow/#privacy">{t['nav_privacy']}</a>
<a class="keep" href="/pilcrow/support.html"{cur if key == "/pilcrow/support.html" else ""}>{t['nav_support']}</a>
<a class="keep" href="/pilcrow/story.html"{cur if key == "/pilcrow/story.html" else ""}>{t['nav_story']}</a>
<a class="btn btn-primary btn-sm" href="/pilcrow/#get">{t['nav_get']}</a>
</nav>MENU</div>
</div>
</header>""", lang).replace("MENU", menu)


def footer(lang: str) -> str:
    t = ui(lang)
    return localize(f"""<footer class="site-footer">
<div class="wrap">
<div class="foot-grid">
<div>
<a class="brand" href="/">Pluria Labs</a>
<p style="margin-top:.8rem;max-width:26rem">{t['foot_tag']}</p>
</div>
<div>
<h4>Pilcrow</h4>
<ul>
<li><a href="/pilcrow/">{t['foot_overview']}</a></li>
<li><a href="/pilcrow/#features">{t['nav_features']}</a></li>
<li><a href="/pilcrow/guide/">{t['nav_guide']}</a></li>
<li><a href="/pilcrow/compare.html">{t['foot_compare']}</a></li>
<li><a href="/pilcrow/support.html">{t['nav_support']}</a></li>
<li><a href="/pilcrow/story.html">{t['nav_story']}</a></li>
<li><a href="/pilcrow/privacy.html">{t['foot_privacy']}</a></li>
</ul>
</div>
<div>
<h4>Pluria Labs</h4>
<ul>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><a href="https://github.com/PluriaLabs">GitHub</a></li>
<li><a href="https://github.com/PluriaLabs/Support/issues/new/choose">{t['foot_bug']}</a></li>
</ul>
</div>
</div>
<div class="legal"><span>{t['foot_copyright']}</span><span>{t['foot_trademark']}</span></div>
</div>
</footer>""", lang)


def alternates_for(key: str, langs: list) -> str:
    """hreflang links for the languages that really have this page (English is x-default)."""
    if len(langs) < 2:
        return ""
    out = "".join(f'<link rel="alternate" hreflang="{c}" href="{SITE}{prefix(c, key)}">\n' for c in langs)
    return out + f'<link rel="alternate" hreflang="x-default" href="{SITE}{key}">\n'


def render(page: dict) -> str:
    """page: key (the English path), lang, translated (False when English stands in), title, description, body."""
    key, lang = page["key"], page.get("lang", "en")
    t = ui(lang)
    url = page.get("url") or prefix(lang, key)
    translated = page.get("translated", True)
    notice, body = "", page["body"]
    if lang != "en" and not key.startswith("/pilcrow/privacy"):
        english = f'<a href="{key}" hreflang="en" lang="en">{html.escape(t["mt_original"])}</a>'
        if translated:
            notice = f'<p class="mt-note" role="note">{html.escape(t["mt_note"])} {english}</p>\n'
        else:
            msg = html.escape(t["fb_note"].format(language=NATIVE[lang]))
            notice = f'<p class="mt-note" role="note">{msg}</p>\n'
            body = f'<div lang="en" dir="ltr">\n{body}\n</div>'
    canonical = SITE + (url if translated else key)
    return LAYOUT.format(
        lang=lang,
        dir=' dir="rtl"' if lang in RTL else "",
        title=html.escape(page["title"]),
        description=html.escape(page["description"], quote=True),
        canonical=canonical,
        alternates=page.get("alternates", ""),
        locale=lang.replace("-", "_"),
        site=SITE,
        jsonld=page.get("jsonld", ""),
        skip=html.escape(t["skip"]),
        header=header(lang, key, page.get("section", "pilcrow")),
        notice=notice,
        body=localize(body, lang),
        footer=footer(lang),
        extra=page.get("extra", ""),
    )


def write(rel: str, text: str) -> None:
    out = ROOT / rel.lstrip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------- comparison table

def compare_cell(code: str, t: dict) -> str:
    """One cell of the comparison table: y, n, ? (not verified), with an optional note after a colon."""
    kind, _, note = code.partition(":")
    note_html = f'<small>{html.escape(note)}</small>' if note else ""
    if kind == "y":
        return f'<td class="y"><span class="mk" aria-hidden="true">✓</span><span class="sr-only">{html.escape(t["compare_yes"])}</span>{note_html}</td>'
    if kind == "?":
        return f'<td class="u"><span class="mk" aria-hidden="true">?</span><span class="sr-only">{html.escape(t["compare_unverified"])}</span></td>'
    return f'<td class="n"><span class="mk" aria-hidden="true">–</span><span class="sr-only">{html.escape(t["compare_no"])}</span></td>'


def render_compare(lang: str) -> str:
    t = ui(lang)
    f = I18N / lang / "compare.json"
    if lang == "en" or not f.exists():
        f = ROOT / "src" / "data" / "compare.json"
    data = json.loads(f.read_text(encoding="utf-8"))
    cols = data["columns"]
    us = ' class="us"'
    head = "".join(f'<th scope="col"{us if i == 0 else ""}>{html.escape(c)}</th>' for i, c in enumerate(cols))
    out = [
        f'<div class="compare-wrap" tabindex="0" role="region" aria-label="{html.escape(t["compare_aria"], quote=True)}">',
        f'<table class="compare"><caption class="sr-only">{html.escape(t["compare_caption"])}</caption>',
        f'<thead><tr><th scope="col" class="feat-h">{html.escape(t["compare_feature"])}</th>{head}</tr></thead>',
    ]
    for g in data["groups"]:
        out.append(f'<tbody><tr class="grp"><th scope="colgroup" colspan="{len(cols) + 1}">{html.escape(g["name"])}</th></tr>')
        for row in g["rows"]:
            cells = "".join(compare_cell(c, t) for c in row[1:])
            out.append(f'<tr><th scope="row">{html.escape(row[0])}</th>{cells}</tr>')
        out.append("</tbody>")
    out.append("</table></div>")
    return "\n".join(out)

# ---------------------------------------------------------------- hand-written pages

def parse_source(path: pathlib.Path) -> dict:
    head, _, body = path.read_text(encoding="utf-8").partition("\n---\n")
    meta = {}
    for line in head.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    meta["body"] = body.strip("\n")
    return meta


def page_sources() -> list:
    """Every hand-written page: (path of the English source, English URL path)."""
    out = []
    for src in sorted(SRC.rglob("*.html")):
        rel = src.relative_to(SRC).as_posix()
        out.append((rel, "/" + rel.removesuffix("index.html") if rel.endswith("index.html") else "/" + rel))
    return out


def translated_langs(rel: str) -> list:
    return ["en"] + [c for c in CODES[1:] if (I18N / c / "pages" / rel).exists()]


def build_pages(lang: str) -> list:
    urls = []
    for rel, key in page_sources():
        if rel == "404.html" and lang != "en":
            continue  # GitHub Pages serves a single 404 page
        mine = I18N / lang / "pages" / rel
        translated = lang == "en" or mine.exists()
        page = parse_source(mine if lang != "en" and translated else SRC / rel)
        page.update(key=key, lang=lang, translated=translated)
        if "<!--compare-table-->" in page["body"]:
            page["body"] = page["body"].replace("<!--compare-table-->", render_compare(lang if translated else "en"))
        if page.get("jsonld_file"):
            data = (ROOT / "src" / page["jsonld_file"]).read_text(encoding="utf-8")
            page["jsonld"] = '<script type="application/ld+json">' + data.strip() + "</script>\n"
        if rel != "404.html":
            page["alternates"] = alternates_for(key, translated_langs(rel))
        url = prefix(lang, key)
        out = url + "index.html" if url.endswith("/") else url
        write(out, render(page))
        if rel != "404.html":
            urls.append(url)
    return urls


# ---------------------------------------------------------------- privacy policies

KEYCAP_CHARS = set("⌘⌃⌥⇧↑↓←→⏎⇥⌫⌦⎋")


def inline(text: str, code: str, guide: bool = False) -> str:
    text = html.escape(text, quote=False)
    spans = []

    def keep(m):
        body = m.group(1)
        tag = "kbd" if guide and any(ch in KEYCAP_CHARS for ch in body) else "code"
        spans.append(f"<{tag}>{body}</{tag}>")
        return f"\0{len(spans) - 1}\0"

    text = re.sub(r"`([^`]+)`", keep, text)

    def link(m):
        label, url = m.group(1), m.group(2)
        n = re.fullmatch(r"privacy-policy(?:\.([A-Za-z-]+))?\.md", url)
        if n:
            url = privacy_url(n.group(1) or "en")
        return f'<a href="{url}">{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    def strong(m):
        cls = ' class="menu"' if guide and "▸" in m.group(1) else ""
        return f"<strong{cls}>{m.group(1)}</strong>"

    text = re.sub(r"\*\*(.+?)\*\*", strong, text)
    text = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<em>\1</em>", text)
    return re.sub(r"\0(\d+)\0", lambda m: spans[int(m.group(1))], text)


def markdown(md: str, code: str):
    """Tiny converter for the subset these policies use. Returns (title, description, html)."""
    title, desc, out = "", "", []
    para, items, quote = [], [], []

    def flush():
        nonlocal desc
        if para:
            joined = " ".join(para)
            if "privacy-policy." in joined and joined.startswith("*"):
                para.clear()  # the language list: replaced by our own bar
                return
            out.append(f"<p>{inline(joined, code)}</p>")
            if not desc and not joined.startswith("**") and not joined.startswith("*"):
                desc = re.sub(r"<[^>]+>", "", inline(joined, code))
            para.clear()
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(i, code)}</li>" for i in items) + "</ul>")
            items.clear()
        if quote:
            out.append("<blockquote><p>" + inline(" ".join(quote), code) + "</p></blockquote>")
            quote.clear()

    for line in md.splitlines():
        if not line.strip():
            flush()
        elif line.startswith("# "):
            flush()
            title = line[2:].strip()
        elif line.startswith("### "):
            flush()
            out.append(f"<h3>{inline(line[4:].strip(), code)}</h3>")
        elif line.startswith("## "):
            flush()
            out.append(f"<h2>{inline(line[3:].strip(), code)}</h2>")
        elif line.startswith("- "):
            if para or quote:
                flush()
            items.append(line[2:].strip())
        elif line.startswith("> "):
            if para or items:
                flush()
            quote.append(line[2:].strip())
        else:
            if items or quote:
                flush()
            para.append(line.strip())
    flush()
    if len(desc) > 190:
        desc = desc[:187].rsplit(" ", 1)[0] + "…"
    return title, desc, "\n".join(out)


def build_privacy() -> list:
    urls = []
    alternates = "".join(
        f'<link rel="alternate" hreflang="{c}" href="{SITE}{privacy_url(c)}">\n' for c, _ in LANGS
    ) + f'<link rel="alternate" hreflang="x-default" href="{SITE}{privacy_url("en")}">\n'
    for code, native in LANGS:
        src = POLICIES / ("privacy-policy.md" if code == "en" else f"privacy-policy.{code}.md")
        title, desc, body = markdown(src.read_text(encoding="utf-8"), code)
        cur = ' aria-current="page"'
        bar = f'<nav class="langs" aria-label="{html.escape(ui(code)["langs_aria"], quote=True)}">' + " ".join(
            f'<a href="{privacy_url(c)}" hreflang="{c}" lang="{c}"{cur if c == code else ""}>{n}</a>'
            for c, n in LANGS
        ) + "</nav>"
        note = (
            '<p class="fineprint" lang="en" dir="ltr">Translations other than English are AI translations. '
            'The <a href="/pilcrow/privacy.html">English version</a> is the clearest statement of the policy.</p>'
            if code != "en" else ""
        )
        page_body = (
            f'<div class="page-head"><div class="narrow"><p class="eyebrow">Pilcrow</p><h1>{html.escape(title)}</h1></div></div>\n'
            f'<div class="narrow prose">\n{bar}\n{note}\n{body}\n</div>'
        )
        page = {
            "key": privacy_url(code), "url": privacy_url(code), "lang": code, "title": f"{title} · Pilcrow",
            "description": desc or title,
            "body": page_body, "alternates": alternates,
        }
        write(privacy_url(code), render(page))
        urls.append(privacy_url(code))
    return urls


# ---------------------------------------------------------------- user guide

def slugify(text: str, lang: str = "en") -> str:
    if lang != "en":  # keep letters of any script, so headings in other languages get readable anchors
        text = re.sub(r"['’]", "", unicodedata.normalize("NFKC", text).lower())
        return re.sub(r"[^\w]+", "-", text).strip("-_")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"['’]", "", text.lower())
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def plain(fragment: str) -> str:
    """Text of an HTML fragment, with a space where a block ends so words do not run together."""
    spaced = re.sub(r"</(li|p|h[1-6]|tr|td|th|pre|blockquote|div)>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", spaced))).strip()


def split_cells(line: str) -> list:
    """Split a table row on pipes that are not inside a code span."""
    line = line.strip()
    line = line[1:] if line.startswith("|") else line
    line = line[:-1] if line.endswith("|") else line
    cells, cur, in_code = [], "", False
    for ch in line:
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
    cells.append(cur.strip())
    return cells


def guide_blocks(lines: list, lang: str = "en"):
    """Convert a run of guide Markdown lines to HTML.

    Returns (html, headings, sections) where headings is [(id, text)] for each second-level
    heading and sections is [(id, title, text)] used for the search index. Text before the
    first heading is section ("", "", text).
    """
    out, heads, sections = [], [], [["", "", []]]
    used, para = set(), []
    i = 0

    def add(htmltext: str):
        out.append(htmltext)
        sections[-1][2].append(plain(htmltext))

    def flush():
        if para:
            add(f"<p>{inline(' '.join(para), 'en', guide=True)}</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            flush()
            lang = line[3:].strip()
            j = i + 1
            buf = []
            while j < len(lines) and not lines[j].startswith("```"):
                buf.append(lines[j])
                j += 1
            cls = f' class="language-{lang}"' if lang else ""
            add(f"<pre><code{cls}>{html.escape(chr(10).join(buf))}</code></pre>")
            i = j + 1
            continue
        m = re.match(r"^(#{2,3}) (.+)$", line)
        if m:
            flush()
            level, text = len(m.group(1)), m.group(2).strip()
            base = slugify(text, lang) or "section"
            hid, n = base, 2
            while hid in used:
                hid, n = f"{base}-{n}", n + 1
            used.add(hid)
            inner = inline(text, "en", guide=True)
            out.append(
                f'<h{level} id="{hid}">{inner}<a class="anchor" href="#{hid}" aria-label="{html.escape(ui(lang)["link_to_section"], quote=True)}">#</a></h{level}>'
            )
            if level == 2:
                heads.append((hid, plain(inner)))
                sections.append([hid, plain(inner), []])
            i += 1
            continue
        if line.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            head = split_cells(rows[0])
            aligns = []
            for c in split_cells(rows[1]) if len(rows) > 1 else []:
                aligns.append("right" if c.endswith(":") and not c.startswith(":") else "center" if c.startswith(":") and c.endswith(":") else "")
            def cell(tag, idx, text):
                a = aligns[idx] if idx < len(aligns) and aligns[idx] else ""
                style = f' style="text-align:{a}"' if a else ""
                return f"<{tag}{style}>{inline(text, 'en', guide=True)}</{tag}>"
            thead = "<tr>" + "".join(cell("th", k, c) for k, c in enumerate(head)) + "</tr>"
            body = "".join("<tr>" + "".join(cell("td", k, c) for k, c in enumerate(split_cells(r))) + "</tr>" for r in rows[2:])
            add(f'<div class="table-wrap"><table><thead>{thead}</thead><tbody>{body}</tbody></table></div>')
            continue
        m = re.match(r"^(\d+)\. (.*)$", line)
        if m:
            flush()
            start, items = int(m.group(1)), []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                items.append(re.sub(r"^\d+\. ", "", lines[i]))
                i += 1
                # a blank line between numbered items does not end the list
                if i < len(lines) and not lines[i].strip() and i + 1 < len(lines) and re.match(r"^\d+\. ", lines[i + 1]):
                    i += 1
            attr = f' start="{start}"' if start != 1 else ""
            add(f"<ol{attr}>" + "".join(f"<li>{inline(t, 'en', guide=True)}</li>" for t in items) + "</ol>")
            continue
        if re.match(r"^[-*] ", line):
            flush()
            items = []
            while i < len(lines) and re.match(r"^[-*] ", lines[i]):
                items.append(lines[i][2:])
                i += 1
            add("<ul>" + "".join(f"<li>{inline(t, 'en', guide=True)}</li>" for t in items) + "</ul>")
            continue
        if line.startswith("> "):
            flush()
            q = []
            while i < len(lines) and lines[i].startswith("> "):
                q.append(lines[i][2:])
                i += 1
            add(f"<blockquote><p>{inline(' '.join(q), 'en', guide=True)}</p></blockquote>")
            continue
        if not line.strip() or re.match(r"^---+$", line.strip()):
            flush()
            i += 1
            continue
        para.append(line.strip())
        i += 1
    flush()
    return "\n".join(out), heads, [(a, b, " ".join(c)) for a, b, c in sections]




def parse_guide(md: str, slugs: dict = None, lang: str = "en") -> dict:
    """Split the guide into its introduction, parts and chapters.

    slugs maps a chapter number to its page name; translations reuse the English page names."""
    lines = md.splitlines()
    parts, intro, cur_part, cur_ch, buf, in_fence = [], [], None, None, [], False
    target = intro

    def close():
        nonlocal buf
        if cur_ch is not None:
            cur_ch["lines"] = buf
        elif cur_part is not None:
            cur_part["intro_lines"] = buf
        else:
            intro[:] = buf
        buf = []

    for line in lines:
        if line.startswith("```"):
            in_fence = not in_fence
        m_part = re.match(r"^# Part ([IVXL]+) [—–-] (.+)$", line) if not in_fence else None
        m_ch = re.match(r"^# Chapter (\d+): (.+)$", line) if not in_fence else None
        if m_part:
            close()
            cur_part = {"roman": m_part.group(1), "name": m_part.group(2).strip(), "chapters": [], "intro_lines": []}
            cur_ch = None
            parts.append(cur_part)
        elif m_ch:
            close()
            n = int(m_ch.group(1))
            title = m_ch.group(2).strip()
            cur_ch = {"n": n, "title": title, "slug": (slugs or {}).get(n) or f"{n:02d}-{slugify(title)}", "part": cur_part, "lines": []}
            cur_part["chapters"].append(cur_ch)
        elif line.startswith("# ") and not in_fence and cur_part is None:
            continue  # the guide's own title
        else:
            buf.append(line)
    close()
    return {"intro": intro, "parts": parts}


def guide_nav(parts: list, current: str = "") -> str:  # links are localized when the page is rendered
    out = []
    for p in parts:
        is_open = any(c["slug"] == current for c in p["chapters"])
        cur = ' aria-current="page"'
        links = "".join(
            f'<li><a href="/pilcrow/guide/{c["slug"]}.html"{cur if c["slug"] == current else ""}>'
            f'<span class="num">{c["n"]}</span>{html.escape(c["title"])}</a></li>'
            for c in p["chapters"]
        )
        out.append(
            f'<details class="g-part"{" open" if is_open else ""}><summary><span class="roman">{p["roman"]}</span>{html.escape(p["name"])}</summary><ul>{links}</ul></details>'
        )
    return "\n".join(out)


def search_box(lang: str) -> str:
    t = ui(lang)
    q = lambda k: html.escape(t[k], quote=True)
    return (f'<div class="g-search" role="search">\n<label class="sr-only" for="g-q">{q("guide_search_label")}</label>\n'
            f'<input id="g-q" type="search" placeholder="{q("guide_search_ph")}" autocomplete="off" spellcheck="false">\n'
            f'<div id="g-results" class="g-results" data-none="{q("guide_none")}" hidden aria-live="polite"></div>\n</div>')

GUIDE_SCRIPT = '<script src="/assets/guide.js" defer></script>\n'


def read_guide_source(path: pathlib.Path, lang: str = "en") -> tuple:
    """The guide is one Markdown file, or a folder of chunks joined in file-name order.

    For another language each chunk comes from src/i18n/<lang>/guide/, or from English when it is missing.
    Returns (text, numbers of the chapters that are still English)."""
    if not path.is_dir():
        return path.read_text(encoding="utf-8"), set()
    parts, english = [], set()
    for f in sorted(path.glob("*.md")):
        mine = I18N / lang / "guide" / f.name
        if lang != "en" and mine.exists():
            parts.append(mine.read_text(encoding="utf-8"))
        else:
            text = f.read_text(encoding="utf-8")
            parts.append(text)
            english |= {int(n) for n in re.findall(r"^# Chapter (\d+):", text, re.M)}
    return "\n\n".join(parts), (english if lang != "en" else set())


def chapter_coverage(path: pathlib.Path) -> dict:
    """For each chapter number, the languages that have its chunk translated."""
    cover = {}
    for f in sorted(path.glob("*.md")):
        nums = [int(n) for n in re.findall(r"^# Chapter (\d+):", f.read_text(encoding="utf-8"), re.M)]
        langs = [c for c in CODES[1:] if (I18N / c / "guide" / f.name).exists()]
        for n in nums:
            cover[n] = langs
    return cover


COVER: dict = {}


def build_guide(path: pathlib.Path, lang: str, slugs: dict) -> tuple:
    t = ui(lang)
    text, english = read_guide_source(path, lang)
    data = parse_guide(text, slugs, lang)
    parts = data["parts"]
    chapters = [c for p in parts for c in p["chapters"]]
    root = prefix(lang, "/pilcrow/guide/")
    urls, index = [root], []
    search = search_box(lang)

    for k, c in enumerate(chapters):
        body, heads, sections = guide_blocks(c["lines"], lang)
        c["html"], c["heads"] = body, heads
        c["desc"] = next((plain(x)[:200] for x in re.findall(r"<p>.*?</p>", body)), c["title"])
        chapter_label = t["chapter"].format(n=c["n"])
        part_label = t["part"].format(roman=c["part"]["roman"])
        for sid, stitle, text_ in sections:
            if text_.strip():
                index.append({
                    "u": prefix(lang, f"/pilcrow/guide/{c['slug']}.html") + (f"#{sid}" if sid else ""),
                    "c": f"{chapter_label}: {c['title']}", "p": f"{part_label} · {c['part']['name']}",
                    "s": stitle, "x": text_,
                })

    def card(target, label, cls):
        if not target:
            return "<span></span>"
        return (
            f'<a class="{cls}" href="/pilcrow/guide/{target["slug"]}.html"><span class="dir">{label}</span>'
            f'<span class="ttl">{html.escape(target["title"])}</span></a>'
        )

    for k, c in enumerate(chapters):
        prev_c = chapters[k - 1] if k else None
        next_c = chapters[k + 1] if k + 1 < len(chapters) else None
        toc = ""
        if len(c["heads"]) > 1:
            toc = f'<aside class="g-toc" aria-label="{html.escape(t["on_this_page"], quote=True)}"><h2>{html.escape(t["on_this_page"])}</h2><ul>' + "".join(
                f'<li><a href="#{hid}">{html.escape(h)}</a></li>' for hid, h in c["heads"]
            ) + "</ul></aside>"
        chapter_label = t["chapter"].format(n=c["n"])
        part_label = t["part"].format(roman=c["part"]["roman"])
        page_body = f"""<div class="guide wrap">
<aside class="g-side">
{search}
<details class="g-nav" open><summary>{html.escape(t["guide_contents"])}</summary>
<nav aria-label="{html.escape(t["guide_nav_aria"], quote=True)}">
<a class="g-home" href="/pilcrow/guide/">{html.escape(t["guide_home"])}</a>
{guide_nav(parts, c["slug"])}
</nav></details>
</aside>
<article class="g-main">
<nav class="crumbs" aria-label="{html.escape(t["breadcrumb_aria"], quote=True)}"><a href="/pilcrow/guide/">{html.escape(t["guide_title"])}</a><span aria-hidden="true">›</span><span>{html.escape(part_label)} · {html.escape(c["part"]["name"])}</span></nav>
<p class="eyebrow">{html.escape(chapter_label)}</p>
<h1>{inline(c["title"], lang)}</h1>
{c["html"]}
<nav class="g-pager" aria-label="{html.escape(t["chapters_aria"], quote=True)}">
{card(prev_c, html.escape(t["prev"]), "prev")}
{card(next_c, html.escape(t["next"]), "next")}
</nav>
</article>
{toc}
</div>"""
        key = f"/pilcrow/guide/{c['slug']}.html"
        write(prefix(lang, key), render({
            "key": key, "lang": lang, "translated": c["n"] not in english,
            "title": f"{plain(inline(c['title'], lang))} · {t['guide_suffix']}",
            "description": c["desc"], "body": page_body, "extra": GUIDE_SCRIPT,
            "alternates": alternates_for(key, ["en"] + COVER.get(c["n"], [])),
        }))
        urls.append(prefix(lang, key))

    # the guide's home page
    intro_html, intro_heads, _ = guide_blocks(data["intro"], lang)
    lede = ""
    m = re.search(r"<h2[^>]*>(.*?)<a class=\"anchor\"", intro_html, re.S)
    if m:
        lede = m.group(1)
        intro_html = re.sub(r"<h2[^>]*>.*?</h2>\n?", "", intro_html, count=1, flags=re.S)
    intro_html = intro_html.replace("<p>[TOC]</p>", "")
    cards = "".join(
        f'<section class="g-card"><h3><span class="roman">{p["roman"]}</span>{html.escape(p["name"])}</h3><ul>'
        + "".join(f'<li><a href="/pilcrow/guide/{c["slug"]}.html"><span class="num">{c["n"]}</span>{html.escape(c["title"])}</a></li>' for c in p["chapters"])
        + "</ul></section>"
        for p in parts
    )
    home = f"""<div class="page-head g-head"><div class="wrap">
<p class="eyebrow">Pilcrow</p>
<h1>{html.escape(t["guide_title"])}</h1>
<p class="lede">{lede or html.escape(t["guide_lede"])}</p>
{search}
</div></div>
<div class="wrap g-home-body">
<div class="g-intro prose">{intro_html}</div>
<div class="g-cards">{cards}</div>
</div>"""
    write(prefix(lang, "/pilcrow/guide/index.html"), render({
        "key": "/pilcrow/guide/", "lang": lang, "translated": (I18N / lang / "guide" / "g01.md").exists() or lang == "en",
        "title": t["guide_home_title"], "description": t["guide_home_desc"], "body": home, "extra": GUIDE_SCRIPT,
        "alternates": alternates_for("/pilcrow/guide/", ["en"] + [c for c in CODES[1:] if (I18N / c / "guide" / "g01.md").exists()]),
    }))
    name = "guide-index.json" if lang == "en" else f"guide-index.{lang}.json"
    write(f"/assets/{name}", json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n")
    done = len(chapters) - len(english)
    print(f"guide {lang}: {len(parts)} parts, {len(chapters)} chapters ({done} translated), {len(index)} searchable sections")
    return urls, {c["n"]: c["slug"] for c in chapters}


def main() -> None:
    global POLICIES, GUIDE
    ap = argparse.ArgumentParser(description="Build the Pluria Labs site.")
    ap.add_argument("--policies", type=pathlib.Path, default=POLICIES, help="folder with the privacy policy Markdown files")
    ap.add_argument("--guide", type=pathlib.Path, default=GUIDE, help="the User Guide: a Markdown file, or a folder of them")
    ap.add_argument("--lang", action="append", help="build only this language (repeatable); default is all")
    args = ap.parse_args()
    POLICIES, GUIDE = args.policies, args.guide
    langs = args.lang or CODES
    COVER.update(chapter_coverage(GUIDE))
    # English first: its chapter page names are reused by every translation, and the sitemap lists all pages.
    en_urls, slugs = build_guide(GUIDE, "en", {})
    urls = build_pages("en") + build_privacy() + en_urls
    for lang in CODES[1:]:
        if lang not in langs:
            continue
        g_urls, _ = build_guide(GUIDE, lang, slugs)
        urls += build_pages(lang) + g_urls
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"<url><loc>{SITE}{u}</loc></url>" for u in sorted(set(urls))]
    sm.append("</urlset>")
    write("/sitemap.xml", "\n".join(sm) + "\n")
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"built {len(urls)} pages")


if __name__ == "__main__":
    main()
