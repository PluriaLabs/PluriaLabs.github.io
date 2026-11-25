# Pluria Labs site

Static site for GitHub Pages, served at https://plurialabs.github.io/. No framework and no
external requests: plain HTML, one stylesheet (`assets/site.css`) and a few lines of optional
JavaScript (`assets/site.js`).

## Layout

| Path | What it is |
| --- | --- |
| `src/pages/` | The hand-written pages (a few header lines, `---`, then the body HTML) |
| `src/jsonld/` | Structured data for search engines |
| `Scripts/build.py` | Builds everything below from `src/` and the privacy policies |
| `index.html`, `pilcrow/`, `404.html` | Build output. Commit it; Pages serves it as it is |
| `pilcrow/privacy.html`, `pilcrow/privacy/<lang>.html` | The privacy policy in 23 languages, built from the Policies repo |
| `pilcrow/guide/` | The User Guide: a home page plus one page per chapter, built from `Documentation/User Guide.md` in the app repo (read only) |
| `assets/guide-index.json`, `assets/guide.js` | The guide's search index (built) and its search script |
| `pilcrow/assets/` | Icons, social image, banner and the app screenshots |
| `<lang>/…` | The whole site again in each of the other 22 Pilcrow languages (`/es/`, `/fr/`, `/ja/`, `/zh-Hans/` …), built from `src/i18n/` |
| `src/i18n/` | Translations of the pages, comparison table, guide and interface strings. See `src/i18n/README.md` |
| `.nojekyll` | Tells Pages to skip Jekyll |

## Edit and rebuild

```bash
python3 -I Scripts/build.py                                  # default paths under ~/Projects
python3 -I Scripts/build.py --policies DIR --guide FILE      # or name the sources
python3 -I Scripts/check_i18n.py ja                          # check a translation against the English
python3 -m http.server 8000                      # preview at http://localhost:8000
```

Do not edit the generated `.html` files at the top level or under `pilcrow/`; edit `src/` and
rebuild. The privacy pages are generated from `PluriaLabs/Policies-and-Licenses` and the User Guide from the
app repo's `Documentation/User Guide.md`, so change the text there and rebuild here. Parts and
chapters are taken from the guide's `# Part …` and `# Chapter N: …` headings.

## Before the App Store launch

- Replace the two "Coming soon to the App Store" buttons in `src/pages/pilcrow/index.html` with the
  App Store link, and drop "coming" from the closing section.
- Rebuild after the privacy policy's effective date is updated in the Policies repo.

## Publishing

GitHub Pages ▸ Deploy from branch ▸ `main` / root.
