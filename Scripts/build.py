#!/usr/bin/env python3
"""Build the Pluria Labs site.

Usage:  python3 -I Scripts/build.py ["/path/to/Policies and Licenses/Pilcrow"]

Reads  src/pages/**/*.html   (a small header, a line of three dashes, then the body)
and the privacy policies (Markdown, one per language) from the Policies repo, and
writes plain HTML next to them in the repo root, plus sitemap.xml and robots.txt.
GitHub Pages serves the result as it is; there is no other build step.
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "pages"
POLICIES = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.home() / "Projects" / "Policies and Licenses" / "Pilcrow"
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
</body>
</html>
"""

HEADER_PILCROW = """<header class="site-header">
<div class="wrap">
<a class="brand" href="/pilcrow/" aria-label="Pilcrow home"><span class="mark" aria-hidden="true">¶</span>Pilcrow</a>
<nav class="nav" aria-label="Main">
<a href="/pilcrow/#features">Features</a>
<a href="/pilcrow/#syntax">Syntax</a>
<a href="/pilcrow/#privacy">Privacy</a>
<a class="keep" href="/pilcrow/support.html"{cur_support}>Support</a>
<a class="btn btn-primary btn-sm" href="/pilcrow/#get">Get Pilcrow</a>
</nav>
</div>
</header>"""

HEADER_LABS = """<header class="site-header">
<div class="wrap">
<a class="brand" href="/" aria-label="Pluria Labs home">Pluria Labs</a>
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
<a class="brand" href="/"><span class="mark" aria-hidden="true">¶</span>Pluria Labs</a>
<p style="margin-top:.8rem;max-width:26rem">Software for people who write. Made with care, and with no tracking.</p>
</div>
<div>
<h4>Pilcrow</h4>
<ul>
<li><a href="/pilcrow/">Overview</a></li>
<li><a href="/pilcrow/#features">Features</a></li>
<li><a href="/pilcrow/support.html">Support</a></li>
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
        cur_support=' aria-current="page"' if path == "/pilcrow/support.html" else "")
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
    )


def write(rel: str, text: str) -> None:
    out = ROOT / rel.lstrip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


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
        if page.get("jsonld_file"):
            data = (ROOT / "src" / page["jsonld_file"]).read_text(encoding="utf-8")
            page["jsonld"] = '<script type="application/ld+json">' + data.strip() + "</script>\n"
        write(out, render(page))
        if rel != "404.html":
            urls.append(url)
    return urls


# ---------------------------------------------------------------- privacy policies

def inline(text: str, code: str) -> str:
    text = html.escape(text, quote=False)
    spans = []

    def keep(m):
        spans.append("<code>" + m.group(1) + "</code>")
        return f"\0{len(spans) - 1}\0"

    text = re.sub(r"`([^`]+)`", keep, text)

    def link(m):
        label, url = m.group(1), m.group(2)
        n = re.fullmatch(r"privacy-policy(?:\.([A-Za-z-]+))?\.md", url)
        if n:
            url = privacy_url(n.group(1) or "en")
        return f'<a href="{url}">{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
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
            "path": privacy_url(code), "lang": code, "title": f"{title} · Pilcrow",
            "description": desc or "How Pilcrow handles your information.",
            "body": page_body, "alternates": alternates,
        }
        write(privacy_url(code), render(page))
        urls.append(privacy_url(code))
    return urls


def main() -> None:
    urls = build_pages() + build_privacy()
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"<url><loc>{SITE}{u}</loc></url>" for u in sorted(set(urls))]
    sm.append("</urlset>")
    write("/sitemap.xml", "\n".join(sm) + "\n")
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print(f"built {len(urls)} pages")


if __name__ == "__main__":
    main()
