
---

# Part XXI — File formats and limits

# Chapter 79: The Application Theme format

An **Application Theme** styles Pilcrow itself: its light or dark appearance, the accent colour, the sidebar, the status and formatting bars, and the editor. It is a JSON file. Rendered documents (Preview, HTML, PDF, image, print and Word) are styled separately by a **Render Theme**, which is CSS (Chapter 80). The two kinds are installed, chosen and deleted separately, and neither follows the other.

## A complete example

```json
{
  "pilcrowAppTheme": 1,
  "name": "Nord",
  "appearance": "dark",
  "colors": {
    "accent": "#88C0D0",
    "sidebar": { "background": "#2E3440", "foreground": "#D8DEE9" },
    "bars": { "background": "#3B4252", "foreground": "#D8DEE9" },
    "editor": {
      "background": "#2E3440",
      "foreground": "#ECEFF4",
      "cursor": "#88C0D0",
      "selection": "#434C5E",
      "gutterBackground": "#2E3440",
      "gutterForeground": "#4C566A"
    },
    "syntax": {
      "heading": "#88C0D0",
      "marker": "#EBCB8B",
      "code": "#A3BE8C",
      "link": "#81A1C1",
      "muted": "#7B88A1",
      "tokens": { "strong": "#D08770" }
    }
  }
}
```

## Top level

| Key | Required | Value |
| --- | --- | --- |
| `pilcrowAppTheme` | yes | The format version, `1`. |
| `name` | yes | 1–200 characters. Shown in Settings and the Themes menu. |
| `appearance` | yes | `"light"`, `"dark"` or `"automatic"`. |
| `colors` | `light` and `dark` themes | One palette (below). |
| `light`, `dark` | `automatic` themes | Two palettes: one used in the system's light appearance, one in dark. |
| `id` | no | Written by Pilcrow for its own library. Ignored on import, which always assigns a new id. |

`appearance` decides the appearance of **every** window: menus, Settings, sheets and pickers included. A `light` or `dark` theme fixes it; `automatic` follows the system.

An automatic theme must set each colour in both `light` and `dark` or in neither. A colour set for one appearance only would otherwise be drawn in the other.

## Palette

Every key is optional. A colour left out keeps Pilcrow's built-in look, so a theme can be as small as one accent colour.

| Key | Styles |
| --- | --- |
| `accent` | The app-wide tint: buttons, selected segments, toggles, links, focus rings, and the sidebar's selected row. Unset keeps the system accent. |
| `sidebar.background`, `sidebar.foreground` | The Files, Outline and Find sidebar. Secondary labels derive from the foreground. |
| `bars.background`, `bars.foreground` | The status bar, the docked formatting toolbar, and import notices. Secondary labels derive from the foreground. |
| `editor.background`, `editor.foreground` | The editor canvas and body text. |
| `editor.cursor`, `editor.selection` | The insertion point and the selection highlight. |
| `editor.gutterBackground`, `editor.gutterForeground` | The line-number gutter. The background defaults to the editor background. |
| `editor.currentLineRule` | The thin rule under the line the caret is on, when **View ▸ Current-Line Rule** is on. Defaults to the editor text colour at low strength. |
| `syntax.<group>` | Live syntax colours by group (below). |
| `syntax.tokens.<raw>` | One token by its raw value, overriding its group. |

### Syntax groups

| Group | Colours |
| --- | --- |
| `heading` | Headings (markers and text), alert markers, definition terms |
| `marker` | Emphasis, strong, strikethrough and other inline delimiters; list and task markers |
| `code` | Inline code, fenced and indented code blocks, math, HTML blocks |
| `link` | Link and image labels and destinations, autolinks |
| `muted` | Block quote markers, thematic breaks, table rows, comments, block attributes |
| `codeKeyword`, `codeString`, `codeNumber`, `codeComment` | Highlighted code inside a fence |

A group left unset takes a built-in colour chosen for the editor background: darker tones on a light canvas, lighter tones on a dark one. Token names in `syntax.tokens` use letters, digits, `_` and `-`, and cannot repeat a group name (`syntax.heading` already covers `heading`).

## Colours

Every colour is a hex string: `#RGB`, `#RGBA`, `#RRGGBB` or `#RRGGBBAA`, in sRGB. Pilcrow stores them in upper case.

## Validation

Pilcrow refuses a file rather than ignore part of it, and names the key at fault, for example `colors.editor.cursor: must be a hex colour`. It refuses:

- a missing or different `pilcrowAppTheme` version;
- an unknown key at any level (usually a typo);
- a palette key that does not match the appearance (`colors` in an automatic theme, `light` and `dark` in a light or dark one);
- a colour that is not hex;
- an automatic theme whose `light` and `dark` palettes set different colours.

## What an Application Theme does not change

The window title bar and toolbar (the system's glass, which takes only the accent), menus, Settings, sheets and pickers keep their native look apart from appearance and accent. Fonts are not themed: the editor font and size are set in **Settings ▸ Appearance ▸ Text Size & Fonts**.

## Installing and sharing

- **Import** a `.json` file from **Settings ▸ Library ▸ Themes**, **File ▸ Import ▸ Theme** on the Mac, or **Settings ▸ Library ▸ Import** on iPad. Dropping the file on Pilcrow works too.
- A `.zip` theme package may hold Application Themes beside Render Themes (Chapter 80).
- The share button beside a theme saves its `.json` file, or the whole package when the theme came from one.

Pilcrow includes three Application Themes: **Automatic**, **Light** and **Dark**. They set the editor and syntax colours and leave the chrome at its built-in look.

# Chapter 80: The Render Theme CSS reference

A **Render Theme** is CSS. It styles Preview, HTML, PDF, image and print output, and the Word styles listed at the end of this chapter. A Render Theme may be a single `.css` file or part of a ZIP package with local assets. Syntax profiles define how source text becomes the document; Render Themes only style the result. CSS never styles the app or the editor; that is the Application Theme (Chapter 79).

## The cascade

Pilcrow applies styles in this order:

1. Pilcrow's structural reset;
2. the selected theme CSS;
3. one-off CSS from the export panel (**Advanced options ▸ Custom CSS**);
4. required print and rendering corrections.

Later rules win according to the normal CSS cascade. Theme JavaScript, remote resources, `file:` URLs and `@import` are not supported.

## Resources

Pilcrow reads theme CSS with a standard CSS tokenizer, so escapes are decoded before anything is checked: `u\72 l(…)` is a `url()` and `@im\70 ort` is an `@import`. Every place a browser would load from is checked: `url(…)`, `url("…")`, `src("…")`, and strings inside `image-set()`. Each must be one of:

- a package-relative path (`fonts/Body.woff2`, `./paper.png`). A `?query` or `#fragment` is allowed and ignored when the file is looked up;
- a `data:` URL of type PNG, JPEG, GIF, WebP, SVG (`image/svg+xml`), TTF, OTF, WOFF or WOFF2;
- a fragment reference such as `url(#shadow)`, which names an element in the page.

Anything with a scheme other than `data:` (`https:`, `file:`, `blob:`) or starting with `//` is refused, as is a path that starts with `/` or contains `..`.

## Render properties

The built-in reset reads these properties, and supplies fallbacks:

| Group | Properties |
| --- | --- |
| Colour | `--pt-background`, `--pt-foreground`, `--pt-secondary-background`, `--pt-secondary-foreground`, `--pt-accent`, `--pt-link-color`, `--pt-border-color` |
| Code | `--pt-code-background`, `--pt-code-foreground`, `--pt-code-keyword`, `--pt-code-string`, `--pt-code-number`, `--pt-code-comment` |
| Type | `--pt-body-font-family`, `--pt-mono-font-family`, `--pt-base-font-size`, `--pt-line-height` |
| Spacing | `--pt-paragraph-spacing`, `--pt-blockquote-indent`, `--pt-list-indent`, `--pt-code-padding`, `--pt-heading-top`, `--pt-heading-bottom` |
| Tables | `--pt-table-header-background`, `--pt-table-stripe-background` |
| Alerts | `--pt-admonition-note-color`, `--pt-admonition-tip-color`, `--pt-admonition-important-color`, `--pt-admonition-warning-color`, `--pt-admonition-caution-color` |

## Public element classes

These fixed classes are public:

```text
pt-document pt-heading pt-paragraph pt-blockquote pt-thematic-break
pt-list pt-list-item pt-code-block pt-code pt-literal-block pt-html-block
pt-raw-block pt-text pt-line-break pt-soft-break pt-emphasis pt-strong
pt-link pt-image pt-html-inline pt-raw-inline pt-table pt-table-section
pt-table-row pt-table-cell pt-definition-list pt-definition-item
pt-definition-term pt-definition-description pt-footnote-reference
pt-footnote-definition pt-admonition pt-sidebar pt-example pt-details
pt-strikethrough pt-underline pt-mark pt-superscript pt-subscript
pt-abbreviation pt-insertion pt-deletion pt-substitution pt-keyboard
pt-sample-output pt-variable pt-math-block pt-math-inline pt-citation
pt-bibliography-entry pt-cross-reference pt-anchor pt-index-term pt-video
pt-audio pt-figure pt-diagram pt-metadata-block pt-attribute-definition
pt-title-block pt-include pt-conditional pt-macro pt-comment
pt-table-of-contents
```

Public modifiers include `pt-heading-1` through `pt-heading-6`, `pt-list--ordered`, `pt-list--unordered`, `pt-definition-list--side-by-side`, `pt-code-block--wrap`, `pt-code-block--numbered`, the five standard `pt-admonition--*` values, and parameterized classes for language, raw format, math notation, diagram format, table-section type, conditional type and macro name. Parameterized suffixes come from the active syntax profile or document and must be CSS-escaped when they contain punctuation.

Pilcrow may add classes and attributes in an update. Avoid selectors that depend on undocumented wrapper depth, generated IDs, or the absence of additional classes.

## A minimal theme

```css
:root {
  color-scheme: light;
  --pt-background: #ffffff;
  --pt-foreground: #202124;
  --pt-secondary-background: #f5f6f7;
  --pt-secondary-foreground: #5f6368;
  --pt-accent: #0b57d0;
  --pt-link-color: var(--pt-accent);
  --pt-border-color: #dadce0;
  --pt-code-background: #f1f3f4;
  --pt-code-foreground: #202124;
  --pt-body-font-family: system-ui, -apple-system, sans-serif;
  --pt-mono-font-family: ui-monospace, "SF Mono", monospace;
  --pt-base-font-size: 16px;
  --pt-line-height: 1.6;
}

.pt-document { max-width: 72ch; }
.pt-heading-1 { letter-spacing: -0.025em; }
```

## ZIP packages

A ZIP package can hold Render Themes (`.css`) and Application Themes (`.json`) together; each is listed with its own kind in Settings. A ZIP with at most one CSS file and at most one Application Theme needs no manifest. Anything more needs `pilcrow-theme.json`, which lists every theme under `variants[].file`. The file's extension decides its kind:

```json
{
  "id": "com.example.paper",
  "name": "Paper",
  "version": "1.0.0",
  "author": "Example Author",
  "license": "MIT",
  "cssAPIVersion": 1,
  "variants": [
    { "id": "app", "name": "Paper", "file": "Paper.json", "appearance": "automatic" },
    { "id": "light", "name": "Paper Light", "file": "Paper-Light.css", "appearance": "light" },
    { "id": "dark", "name": "Paper Dark", "file": "Paper-Dark.css", "appearance": "dark" }
  ]
}
```

The manifest describes the package and its themes. It never contains style values: those are in the CSS and Application Theme files.

- The package `id` names the install folder. It must not start with `.` or have leading or trailing spaces. Installing a package whose `id` is already installed replaces it.
- A ZIP made with Finder's **Compress** works as is. Pilcrow skips `__MACOSX/`, `._*`, `.DS_Store` and `Thumbs.db`, and when every file sits inside one top-level folder, that folder is treated as the package root.
- Deleting one theme removes it from the package and keeps the others along with the shared assets. Deleting the last theme removes the package. A deleted theme that was selected returns that selection to its kind's default: Automatic for the Application Theme, Light for the Render Theme.
- CSS may reference packaged PNG, JPEG, GIF, WebP, TTF, OTF, WOFF and WOFF2 files with relative `url(...)` paths. Pilcrow verifies their signatures and embeds referenced assets as data URLs so rendering and exported HTML remain offline and self-contained. ZIP paths cannot escape the package, collide by case, or point to links. Archive size, entry count, individual size and compression ratio are bounded.

## Word

Word export uses the light (base) `:root` values and maps these semantic properties into named Word styles: `--pt-foreground`, `--pt-background`, `--pt-accent`, `--pt-link-color`, `--pt-code-background`, `--pt-code-foreground`, `--pt-body-font-family`, `--pt-mono-font-family`, `--pt-base-font-size` and `--pt-line-height`. Browser selectors and layout rules have no general Word equivalent. Preview, HTML, PDF and image output use the complete stylesheet; Word uses this subset while preserving document structure, diagrams, math pictures, links and media. The export panel shows this limitation whenever Word is selected.

Pilcrow includes two Render Themes, **Light** and **Dark**, which are complete starting points.

# Chapter 81: Files, encodings and limits

## Files Pilcrow opens

Pilcrow edits plain-text and markup files. The usual extensions are `txt`, `md`, `markdown`, `adoc`, `asciidoc`, `rst` and `tex`, and any extension a profile you add claims. Pilcrow detects a file's text encoding when it opens it.

| Item | Type |
| --- | --- |
| Syntax profile, macro collection, style guide, Application Theme | `.json` |
| Render Theme | `.css` |
| Theme package | `.zip` |
| Book project manifest | `manifest.pilcrow` |
| Backdrop | HEIC, PNG, JPEG, SVG, MP4, MOV, M4V |
| Typing sound clip | WAV, AIFF, MP3, M4A, CAF |

## Text encodings

Pilcrow reads UTF-8, UTF-16, UTF-32 and ISO 8859-1 (Latin-1) text. You can convert a document with **Document Information ▸ Encoding ▸ Convert To…** to any of the following; the file is converted when it is next saved:

UTF-8, UTF-8 (BOM), UTF-16 LE, UTF-16 LE (BOM), UTF-16 BE, UTF-16 BE (BOM), UTF-32 LE, UTF-32 LE (BOM), UTF-32 BE, UTF-32 BE (BOM).

A Latin-1 file can be converted to any of these without loss. Converting to Latin-1 is not offered, because it can destroy content.

## Export formats

| Format | Extension |
| --- | --- |
| HTML, HTML (without Styles) | `.html` |
| PDF | `.pdf` |
| Word (.docx) | `.docx` |
| Image | `.png` |
| PDF Archive | `.zip` |

## Limits and numbers

Where Pilcrow stops, or where a choice has a range:

| Where | Limit |
| --- | --- |
| Search panel | Stops at 500 matches. |
| Preview find | Counts up to 2,000 matches. |
| Replace in Folder | Changes at most 2,000 files at a time. |
| Check Links | Checks up to 50,000 links. |
| Compare | Shows up to 5,000 changed lines. |
| Versions to keep | None to 500 (default 50). |
| Long lines | Lines of 20,000 characters or more always wrap. |
| Font size | 9 to 32 points. |
| Tab width | 2 to 8 spaces. |
| Text width | 50% to 100%. |
| Zoom | 50% to 200%, in ten steps. |
| Reading speed | 60 to 2,000 words per minute. |
| Navigator width | 180 to 420 points. |
| Typing sound clip | At most 2 seconds and 3 MB. |
| Diagnostic report log text | The newest entries, up to 60,000 characters, when added to a GitHub issue description. |
| Very large files | Open and edit without being read into memory whole. Line and word counts, and the outline, are completed in the background and may be partial until then. PDF export of a very large document needs much more memory than editing or HTML and Word export; PDF Archive splits it into bounded parts. |

## Where Pilcrow keeps things

| What | Where |
| --- | --- |
| Your documents | Wherever you saved them. |
| Library (themes, profiles, macros, style guides, backdrops) | In the app's private storage, or in a folder named "Pilcrow Library" inside a folder you choose (**Settings ▸ Library ▸ Location**). |
| Preferences, API keys, recovery copies, version history | On the device, in the app's private storage and Keychain. Review and delete them in **Settings ▸ General ▸ Storage & Privacy**. |
| Diagnostic log | On the device, until you clear it. |

# Chapter 82: Messages, banners and empty states

This chapter explains the short messages Pilcrow shows, so none of them is a mystery.

## In the editor and preview

| Message | What it means |
| --- | --- |
| **Nothing to preview yet. Start writing and it will appear here.** (or "Switch to Edit and start writing.") | The document is empty, so there is nothing to draw in Preview. |
| **Preview couldn't render: …** with **Show Source** and **Retry** | Preview failed. **Show Source** switches to Edit. **Retry** tries again. |
| A failed equation or diagram, with a **Show Source** link | One block could not be drawn. Click **Show Source** to jump to that block's source and fix it. |
| **Couldn't save** with **Retry** and a dismiss button | Saving failed. The document stays open and unsaved. Fix the cause (disk space, permissions, a file that moved) and choose **Retry**. |
| **File Changed on Disk** | Another app modified the file. **Reload** reads the new version; **Keep Current Version** keeps what you have. |
| **Parsing warning** | A line where a construct is probably not what you meant (Chapter 68). |
| **Replace Existing File?** | The name you chose is already in use at that place. |
| **Fill-in fields remain** | You are printing or exporting with unfilled fields (Chapter 63). |
| **Pane divider** (VoiceOver hint: "Drag to resize the editor and the preview. Double-tap to reset.") | The handle between source and preview in Side by Side. |
| **Words: N** | The word count in the status bar. |

## In dialogs and panels

| Where | Message | Meaning |
| --- | --- | --- |
| Command palette | **Type a command** | The field's hint. "No matching commands" appears when nothing fits. |
| Open Quickly | **Type a filename** | The field's hint. |
| Carets in a Column | **Lines (for example 3-17)**, **Column (for example 100, or 100-105 to select)** | Field hints. A single column places carets; a range selects those characters on each line. |
| Search panel | **Type to search this folder.**, **No matches in this folder.**, **Search cancelled.** | The state of a folder search. |
| Files panel | **You can also drop a folder here.** | Drag a folder onto the panel to open it. |
| Replace in Folder | **Nothing to replace.** | The search has no matches. |
| Compare | Tooltips on the buttons: **Accept** ("Make this change in the open document"), **Reject** ("Leave this change out of the open document"), **Take Back** ("Put the older lines back in the document for this change only"). | What each does. |
| Translate | **The translation could not be completed.** | Try again, or choose another speed. |
| Translate | **Estimated time: less than a minute** | An estimate for the AI assistant speed; the time depends on your AI service. After a translation, **Open in New Tab** opens the result. |
| Assistant | **No document is open.**, **No document text is sent.** | The panel has nothing to share, so nothing is sent. |
| Model chooser | **Loading models…**, **No models match.** | The list is loading, or your search found nothing. |
| Style review | **No findings.** and **The reply could not be read as findings. Try again.** | The review found nothing, or the AI's reply was not in the expected form. |
| Style review | **Apply All** tooltip: "Makes every fix that has one, as a single change you can undo." | One Undo reverses them all. |
| Project panel | **Your name**, **Add Variable** | The Author field's hint, and the button for a project variable. |
| Assistant permission | **Read Pilcrow's privacy policy** | Opens the privacy policy. |

## In Settings

| Where | Message | Meaning |
| --- | --- | --- |
| Keyboard | **Press the new shortcut, then click Save.** and **Press any key…** | While recording a shortcut. |
| Library ▸ Location | **Library location**, **Moving your library…** | The page title, and the progress while a library moves. |
| Assistant connection | **Leave blank to keep the saved key.** | When editing, a blank key field keeps the key already in the Keychain. |
| Macro editor | **Trigger — e.g. /sig** | The trigger field's hint. |
| Profile editor | **Advanced profile JSON**, **Sample and results** | The JSON editor's title, and the area under Test Sample that shows the nodes a sample produces. |
| Diagnostics | **All parts** (in the log viewer), **No entries match.** | The unfiltered log, and a filter that matches nothing. |
| Status bar | A red **Recording log** mark; its tooltip **Show Diagnostics Settings** | A log is being recorded. Click it for the Diagnostics page. **Stop recording and finish the bug report** is the tooltip on **Reproducing — Finish Report**. |
| Status bar | **Choose the syntax profile for this document** | The tooltip on the syntax menu. |
| Title control | **Open documents and document actions** | The tooltip on the document title. |

## Sections on the Settings pages

For reference, the sections that group the controls in Chapter 67 to Chapter 71:

| Page | Sections |
| --- | --- |
| Files | **On Launch**, **Default file type**, **Save & recover**, **File tree / library**, **When something is dropped onto the app** |
| Images | **When inserting an image**, **Images in Preview and exports**, **Preferred image syntax** |
| Display & Typing | **Display**, **Typing**, **Typing sounds**, **Your own sounds**, **Spelling**, **Diagnostics** |
| Theme & Backdrop | **Appearance**, **Editor Background**, **Editor size and word count** |
| Text Size & Fonts | **Text**, **Fonts** |
| Export Defaults | **Default output style**, **Page**, **Header, footer, and metadata** |
| CommonMark Options | **Syntax support**, **Additional syntax**, **Smart punctuation**, **Code fences** |
| Contents & Labels | **Contents**, **Heading labels**, **Title**, **Depth**, **Indentation**, **Links** |
| Storage & Privacy | **Documents**, **File Access**, **Private & Support Data** |
| Translation | **Default Language**, **Document Translation**, **Files in Another Language**, **Languages on This Device** |
| Assistant | **Connections**, **Excluded files**, **Folders turned off**, **Privacy** |
