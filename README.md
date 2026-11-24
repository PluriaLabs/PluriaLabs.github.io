# Pluria Labs site

Static site served by GitHub Pages at https://pluriaLabs.github.io/.

- `index.html`: company page
- `pilcrow/`: Pilcrow landing, support and privacy pages
- `style.css`: shared styles (light and dark)
- `.nojekyll`: serve files as-is, no Jekyll build

Links are root-relative (`/style.css`), so preview from the repo root:
`python3 -m http.server 8000`, then open http://localhost:8000.
Publish: Settings ▸ Pages ▸ Deploy from branch ▸ `main` / root.
