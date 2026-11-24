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
| `pilcrow/assets/` | Icons, social image, banner and the app screenshots |
| `.nojekyll` | Tells Pages to skip Jekyll |

## Edit and rebuild

```bash
python3 -I Scripts/build.py                      # uses ~/Projects/Policies and Licenses/Pilcrow
python3 -I Scripts/build.py "/path/to/Pilcrow"   # or name the policies folder
python3 -m http.server 8000                      # preview at http://localhost:8000
```

Do not edit the generated `.html` files at the top level or under `pilcrow/`; edit `src/` and
rebuild. The privacy pages are generated from `PluriaLabs/Policies-and-Licenses`, so change the
policy there and rebuild here.

## Before the App Store launch

- Replace the two "Coming soon to the App Store" buttons in `src/pages/pilcrow/index.html` with the
  App Store link, and drop "coming" from the closing section.
- Rebuild after the privacy policy's effective date is updated in the Policies repo.

## Publishing

GitHub Pages ▸ Deploy from branch ▸ `main` / root.
