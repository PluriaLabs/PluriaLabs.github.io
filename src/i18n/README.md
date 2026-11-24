# Translating the Pluria Labs site

The site is English at `/…` and one copy per Pilcrow language at `/<code>/…` (23 languages, the same
ones the app ships). English is the source; everything here is a translation of `src/`.

```
src/i18n/<lang>/ui.json        buttons, menus and labels the build puts around the pages
src/i18n/<lang>/pages/…        the hand-written pages (same path and file name as src/pages/…)
src/i18n/<lang>/compare.json   the comparison table (same shape as src/data/compare.json)
src/i18n/<lang>/guide/gNN.md   the User Guide, one chunk per file (same names as src/guide/)
src/i18n/_glossary/<lang>.tsv  the app's own words for its menus, buttons and settings
```

A file that is missing is not an error: the build shows the English file inside the translated site, with a
notice. So a language can be translated one file at a time.

## Rules for every translation

1. **Translate everything a reader reads, and nothing else.** Do not summarise, shorten, add or skip. Keep the tone of the English: plain, friendly, exact.
2. **Keep the structure identical.** Same number of lines, same line types (heading level, table row, list item, paragraph, blank line), same tags and attributes. Do not merge or split lines.
3. **Leave alone:** code blocks (everything between ``` lines), `inline code`, URLs, link targets, e-mail addresses, file names, keyboard shortcuts such as `⌘S`, and the names Pilcrow, Pluria Labs, Mac, iPad, macOS, iPadOS, Markdown, AsciiDoc, reStructuredText, LaTeX, Typora, 1Writer, Ulysses, Obsidian, Bear, CommonMark, GitHub.
4. **Use the app's own words for the interface.** Menu items, buttons, settings and dialog names appear in **bold** (for example **File ▸ Save**). Translate each step of a path with the wording in the glossary for your language, and keep the `▸` separators. If a term is not in the glossary, translate it in the same style. The glossary is the app's real UI text, so the reader finds exactly the labels they see on screen.
5. **Headings.** Keep `# Part I — Name` (roman numeral, space, em dash, space) and `# Chapter 12: Title` (ASCII colon) exactly in that form; only the name and title change. Keep `[TOC]`, `---` and table separator rows (`|---|:--:|`) as they are.
6. **Markdown emphasis** (`**bold**`, `*italic*`) may move to wrap the translated words, but must stay balanced.
7. **HTML pages** start with a few header lines, then a line `---`, then the body. Translate `title:` and `description:` (keep a description under about 180 characters); leave `section:` and `jsonld_file:` as they are. In the body translate visible text plus `alt`, `aria-label` and `title` attributes. Do not touch tags, classes, ids, hrefs, `lang` or `style`. Keep `<!--compare-table-->`.
8. **Numbers, dates, quotation marks and punctuation** follow the language's usual style (for example «…» in French and Spanish, 「…」 in Japanese). Keep numerals as they are in the English unless the language normally writes them differently.
9. **Arabic** is right-to-left: translate the text only; the build sets the direction. Keep code and product names as they are.
10. Words that are traditionally left in English in your language (for example technical terms people say in English) may stay, but prefer the glossary.
11. These are the app's own machine-translation conventions: the build adds the notice "Machine-translated — may contain errors." to each page, so do not add one to the text.

## Checking

```bash
python3 -I Scripts/check_i18n.py <lang>                 # every file for the language
python3 -I Scripts/check_i18n.py <lang> guide/g03.md    # one file
python3 -I Scripts/build.py --lang <lang>               # build to look at it
```

`check_i18n.py` compares each file with the English and prints what differs. Fix every message it prints.
`Scripts/glossary_for.py <lang> <english files…>` lists the glossary terms that occur in the files you are translating.
