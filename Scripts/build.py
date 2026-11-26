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
SITE = "https://plurialabs.com"
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


def privacy_url(code: str) -> str:
    return "/pilcrow/privacy.html" if code == "en" else f"/pilcrow/privacy/{code}.html"


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
<meta property="og:image" content="{site}/pilcrow/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/pilcrow/assets/favicon.svg">
<link rel="icon" type="image/png" href="/pilcrow/assets/favicon.png">
<link rel="apple-touch-icon" href="/pilcrow/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/site.css">
{jsonld}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header}
<main id="main">
{body}
</main>
{footer}
<script src="/assets/site.js" defer></script>
{extra}</body>
</html>
"""

HEADER_PILCROW = """<header class="site-header">
<div class="wrap">
<a class="brand" translate="no" href="/pilcrow/" aria-label="Pilcrow home"><img class="mark" src="/assets/logo-mark.svg" alt="" width="32" height="38">Pilcrow</a>
<nav class="nav" aria-label="Main">
<a href="/pilcrow/#features">Features</a>
<a class="keep" href="/pilcrow/guide/"{cur_guide}>User Guide</a>
<a href="/pilcrow/compare.html"{cur_compare}>Compare</a>
<a href="/pilcrow/#privacy">Privacy</a>
<a class="keep" href="/pilcrow/support.html"{cur_support}>Support</a>
<a class="keep" href="/pilcrow/story.html"{cur_story}>Story</a>
<a class="btn btn-primary btn-sm" href="/pilcrow/#get">Get Pilcrow</a>
</nav>
</div>
</header>"""

HEADER_LABS = """<header class="site-header">
<div class="wrap">
<a class="brand" translate="no" href="/" aria-label="Pluria Labs home">Pluria Labs</a>
<nav class="nav" aria-label="Main">
<a class="keep" href="/pilcrow/">Pilcrow</a>
<a href="/pilcrow/support.html">Support</a>
<a href="https://github.com/PluriaLabs">GitHub</a>
</nav>
</div>
</header>"""

FOOTER = """<footer class="site-footer">
<div class="wrap">
<div class="foot-grid">
<div>
<a class="brand" translate="no" href="/">Pluria Labs</a>
<p style="margin-top:.8rem;max-width:26rem">Software for people who write. Made with care, and with no tracking.</p>
</div>
<div>
<h4>Pilcrow</h4>
<ul>
<li><a href="/pilcrow/">Overview</a></li>
<li><a href="/pilcrow/#features">Features</a></li>
<li><a href="/pilcrow/guide/">User Guide</a></li>
<li><a href="/pilcrow/compare.html">How Pilcrow compares</a></li>
<li><a href="/pilcrow/support.html">Support</a></li>
<li><a href="/pilcrow/story.html">Story</a></li>
<li><a href="/pilcrow/privacy.html">Privacy policy</a></li>
</ul>
</div>
<div>
<h4>Pluria Labs</h4>
<ul>
<li><a href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></li>
<li><a href="https://github.com/PluriaLabs">GitHub</a></li>
<li><a href="https://github.com/PluriaLabs/Support/issues/new/choose">Report a bug</a></li>
</ul>
</div>
</div>
<div class="legal"><span>&copy; 2026 Pluria Labs.</span><span>Mac and iPad are trademarks of Apple Inc.</span></div>
</div>
</footer>"""


def render(page: dict) -> str:
    path = page["path"]
    lang = page.get("lang", "en")
    header = HEADER_LABS if page.get("section") == "labs" else HEADER_PILCROW.format(
        cur_support=' aria-current="page"' if path == "/pilcrow/support.html" else "",
        cur_story=' aria-current="page"' if path == "/pilcrow/story.html" else "",
        cur_guide=' aria-current="page"' if path.startswith("/pilcrow/guide/") else "",
        cur_compare=' aria-current="page"' if path == "/pilcrow/compare.html" else "")
    return LAYOUT.format(
        lang=lang,
        dir=' dir="rtl"' if lang in RTL else "",
        title=html.escape(page["title"]),
        description=html.escape(page["description"], quote=True),
        canonical=SITE + path,
        alternates=page.get("alternates", ""),
        site=SITE,
        jsonld=page.get("jsonld", ""),
        header=header,
        body=page["body"],
        footer=FOOTER,
        extra=page.get("extra", ""),
    )


def write(rel: str, text: str) -> None:
    out = ROOT / rel.lstrip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")



# ---------------------------------------------------------------- comparison table

def compare_cell(code: str) -> str:
    """One cell of the comparison table: y, n, ? (not verified), with an optional note after a colon."""
    kind, _, note = code.partition(":")
    note_html = f'<small>{html.escape(note)}</small>' if note else ""
    if kind == "y":
        return f'<td class="y"><span class="mk" aria-hidden="true">✓</span><span class="sr-only">Yes</span>{note_html}</td>'
    if kind == "?":
        return '<td class="u"><span class="mk" aria-hidden="true">?</span><span class="sr-only">Not verified</span></td>'
    return '<td class="n"><span class="mk" aria-hidden="true">–</span><span class="sr-only">No</span></td>'


def render_compare() -> str:
    data = json.loads((ROOT / "src" / "data" / "compare.json").read_text(encoding="utf-8"))
    cols = data["columns"]
    us = ' class="us"'
    head = "".join(f'<th scope="col" translate="no"{us if i == 0 else ""}>{html.escape(c)}</th>' for i, c in enumerate(cols))
    out = [
        '<div class="compare-wrap" tabindex="0" role="region" aria-label="Feature comparison table">',
        '<table class="compare"><caption class="sr-only">Features of Pilcrow and five other writing editors</caption>',
        f'<thead><tr><th scope="col" class="feat-h">Feature</th>{head}</tr></thead>',
    ]
    for g in data["groups"]:
        out.append(f'<tbody><tr class="grp"><th scope="colgroup" colspan="{len(cols) + 1}">{html.escape(g["name"])}</th></tr>')
        for row in g["rows"]:
            cells = "".join(compare_cell(c) for c in row[1:])
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


def build_pages() -> list:
    urls = []
    for src in sorted(SRC.rglob("*.html")):
        rel = src.relative_to(SRC).as_posix()
        page = parse_source(src)
        out = "/" + rel
        url = "/" + rel.removesuffix("index.html") if rel.endswith("index.html") else out
        page["path"] = url
        if "<!--compare-table-->" in page["body"]:
            page["body"] = page["body"].replace("<!--compare-table-->", render_compare())
        if page.get("jsonld_file"):
            data = (ROOT / "src" / page["jsonld_file"]).read_text(encoding="utf-8")
            page["jsonld"] = '<script type="application/ld+json">' + data.strip() + "</script>\n"
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
        spans.append(f'<{tag} translate="no">{body}</{tag}>')
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
        bar = '<nav class="langs" aria-label="Languages">' + " ".join(
            f'<a href="{privacy_url(c)}" hreflang="{c}" lang="{c}" translate="no"{cur if c == code else ""}>{n}</a>'
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
            "path": privacy_url(code), "lang": code, "title": f"{title} · Pilcrow",
            "description": desc or "How Pilcrow handles your information.",
            "body": page_body, "alternates": alternates,
        }
        write(privacy_url(code), render(page))
        urls.append(privacy_url(code))
    return urls


# ---------------------------------------------------------------- user guide

def slugify(text: str) -> str:
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


def guide_blocks(lines: list):
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
            add(f'<pre translate="no"><code{cls}>{html.escape(chr(10).join(buf))}</code></pre>')
            i = j + 1
            continue
        m = re.match(r"^(#{2,3}) (.+)$", line)
        if m:
            flush()
            level, text = len(m.group(1)), m.group(2).strip()
            base = slugify(text) or "section"
            hid, n = base, 2
            while hid in used:
                hid, n = f"{base}-{n}", n + 1
            used.add(hid)
            inner = inline(text, "en", guide=True)
            out.append(
                f'<h{level} id="{hid}">{inner}<a class="anchor" href="#{hid}" aria-label="Link to this section">#</a></h{level}>'
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


ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50}


def parse_guide(md: str) -> dict:
    """Split the guide into its introduction, parts and chapters."""
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
        m_part = re.match(r"^# Part ([IVXL]+) — (.+)$", line) if not in_fence else None
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
            cur_ch = {"n": n, "title": title, "slug": f"{n:02d}-{slugify(title)}", "part": cur_part, "lines": []}
            cur_part["chapters"].append(cur_ch)
        elif line.startswith("# ") and not in_fence and cur_part is None:
            continue  # the guide's own title
        else:
            buf.append(line)
    close()
    return {"intro": intro, "parts": parts}


def guide_nav(parts: list, current: str = "") -> str:
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


SEARCH_BOX = """<div class="g-search" role="search">
<label class="sr-only" for="g-q">Search the User Guide</label>
<input id="g-q" type="search" placeholder="Search the guide" autocomplete="off" spellcheck="false">
<div id="g-results" class="g-results" hidden aria-live="polite"></div>
</div>"""

GUIDE_SCRIPT = '<script src="/assets/guide.js" defer></script>\n'


def read_guide_source(path: pathlib.Path) -> str:
    """The guide is one Markdown file, or a folder of them that are joined in file-name order."""
    if path.is_dir():
        return "\n\n".join(f.read_text(encoding="utf-8") for f in sorted(path.glob("*.md")))
    return path.read_text(encoding="utf-8")


def build_guide(path: pathlib.Path) -> list:
    data = parse_guide(read_guide_source(path))
    parts = data["parts"]
    chapters = [c for p in parts for c in p["chapters"]]
    urls, index = ["/pilcrow/guide/"], []

    for k, c in enumerate(chapters):
        body, heads, sections = guide_blocks(c["lines"])
        c["html"], c["heads"] = body, heads
        c["desc"] = next((plain(x)[:200] for x in re.findall(r"<p>.*?</p>", body)), c["title"])
        for sid, stitle, text in sections:
            if text.strip():
                index.append({
                    "u": f"/pilcrow/guide/{c['slug']}.html" + (f"#{sid}" if sid else ""),
                    "c": f"Chapter {c['n']}: {c['title']}", "p": f"Part {c['part']['roman']} · {c['part']['name']}",
                    "s": stitle, "x": text,
                })

    for k, c in enumerate(chapters):
        prev_c = chapters[k - 1] if k else None
        next_c = chapters[k + 1] if k + 1 < len(chapters) else None
        toc = ""
        if len(c["heads"]) > 1:
            toc = '<aside class="g-toc" aria-label="On this page"><h2>On this page</h2><ul>' + "".join(
                f'<li><a href="#{hid}">{html.escape(t)}</a></li>' for hid, t in c["heads"]
            ) + "</ul></aside>"

        def card(target, label, cls):
            if not target:
                return "<span></span>"
            return (
                f'<a class="{cls}" href="/pilcrow/guide/{target["slug"]}.html"><span class="dir">{label}</span>'
                f'<span class="ttl">{html.escape(target["title"])}</span></a>'
            )

        page_body = f"""<div class="guide wrap">
<aside class="g-side">
{SEARCH_BOX}
<details class="g-nav" open><summary>Guide contents</summary>
<nav aria-label="User Guide">
<a class="g-home" href="/pilcrow/guide/">Guide home</a>
{guide_nav(parts, c["slug"])}
</nav></details>
</aside>
<article class="g-main">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/pilcrow/guide/">User Guide</a><span aria-hidden="true">›</span><span>Part {c["part"]["roman"]} · {html.escape(c["part"]["name"])}</span></nav>
<p class="eyebrow">Chapter {c["n"]}</p>
<h1>{inline(c["title"], "en")}</h1>
{c["html"]}
<nav class="g-pager" aria-label="Chapters">
{card(prev_c, "Previous", "prev")}
{card(next_c, "Next", "next")}
</nav>
</article>
{toc}
</div>"""
        url = f"/pilcrow/guide/{c['slug']}.html"
        write(url, render({
            "path": url, "title": f"{plain(inline(c['title'], 'en'))} · Pilcrow User Guide",
            "description": c["desc"], "body": page_body, "extra": GUIDE_SCRIPT,
        }))
        urls.append(url)

    # the guide's home page: only the subtitle is taken from the introduction, then the chapter cards
    intro_html, intro_heads, _ = guide_blocks(data["intro"])
    lede = ""
    m = re.search(r"<h2[^>]*>(.*?)<a class=\"anchor\"", intro_html, re.S)
    if m:
        lede = m.group(1)
    cards = "".join(
        f'<section class="g-card"><h3><span class="roman">{p["roman"]}</span>{html.escape(p["name"])}</h3><ul>'
        + "".join(f'<li><a href="/pilcrow/guide/{c["slug"]}.html"><span class="num">{c["n"]}</span>{html.escape(c["title"])}</a></li>' for c in p["chapters"])
        + "</ul></section>"
        for p in parts
    )
    home = f"""<div class="page-head g-head"><div class="wrap">
<p class="eyebrow">Pilcrow</p>
<h1>User Guide</h1>
<p class="lede">{lede or "Everything you need to write, organize, review and publish with Pilcrow."}</p>
{SEARCH_BOX}
</div></div>
<div class="wrap g-home-body">
<div class="g-cards">{cards}</div>
</div>"""
    write("/pilcrow/guide/index.html", render({
        "path": "/pilcrow/guide/", "title": "Pilcrow User Guide · Pluria Labs",
        "description": "The complete task-based guide to Pilcrow for Mac and iPad: writing, organizing, reviewing and publishing plain text.",
        "body": home, "extra": GUIDE_SCRIPT,
    }))
    write("/assets/guide-index.json", json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"guide: {len(parts)} parts, {len(chapters)} chapters, {len(index)} searchable sections")
    return urls


def main() -> None:
    global POLICIES, GUIDE
    ap = argparse.ArgumentParser(description="Build the Pluria Labs site.")
    ap.add_argument("--policies", type=pathlib.Path, default=POLICIES, help="folder with the privacy policy Markdown files")
    ap.add_argument("--guide", type=pathlib.Path, default=GUIDE, help="the User Guide: a Markdown file, or a folder of them")
    args = ap.parse_args()
    POLICIES, GUIDE = args.policies, args.guide
    urls = build_pages() + build_privacy() + build_guide(GUIDE)
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"<url><loc>{SITE}{u}</loc></url>" for u in sorted(set(urls))]
    sm.append("</urlset>")
    write("/sitemap.xml", "\n".join(sm) + "\n")
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"built {len(urls)} pages")


if __name__ == "__main__":
    main()
