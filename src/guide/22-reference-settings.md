
---

# Part XVIII — Settings reference

# Chapter 66: How Settings is organized

Open Settings from **Pilcrow ▸ Settings…** (`⌘,`) on Mac, or from the gear in the header on iPad, where it opens as a sheet with a **Done** button. The window has a **Search settings** box and a list of **categories** on the left. Each category has one or more **pages**, shown as a bar of buttons across the top.

| Category | Pages |
| --- | --- |
| **General** | Language & Windows (iPad: **Language**), Files, Translation, Assistant, Diagnostics, Storage & Privacy |
| **Editing** | Display & Typing, Images |
| **Appearance** | Theme & Backdrop, Text Size & Fonts |
| **Table of Contents** | Contents & Labels |
| **Export** | Export Defaults |
| **Library** | Syntax Profiles, CommonMark Options, Themes, Macros, Style Guides, Rendering Libraries, Location (iPad also has **Import**) |
| **Keyboard** | Shortcuts |
| **Subscription & Credits** | Support Pilcrow |

**Search settings** looks for a control by name. Type part of a label, such as "line spacing" or "versions", and the results show the control, its page and its category. Choose one to go straight there. Changes take effect straight away; there is no Save button except in the editors for themes, profiles, macros and keyboard shortcuts.

Settings that affect only one Mac or one iPad stay on that device. Your library (themes, profiles, macros, style guides and backdrops) can be moved to a folder you choose, including one in iCloud Drive (Chapter 71).

# Chapter 67: General

## Language & Windows

| Control | What it does |
| --- | --- |
| **Language** | Chooses Pilcrow's language, independent of the device's. **System default** follows the device. A language that was translated with AI shows "Machine-translated — may contain errors." The change takes effect the next time you open Pilcrow, with a **Quit Now** button on Mac. |
| **Show the translation notice when Pilcrow starts** | Turns the "Translated with AI" notice back on after you chose **Don't show this again**. |
| **Quit Pilcrow when last window is closed** (Mac) | Quits the app when you close the last window, instead of leaving it running. |

## Files

| Control | What it does |
| --- | --- |
| **When starting** | What Pilcrow opens at launch: **Open new file**, **Restore last closed folders**, **Restore last closed files and folders**, or **Open custom folder** (with a **Choose…** button). Restoring reopens what was on screen when the app last quit. A file that has since moved or been deleted is skipped. |
| **Save new documents as** | The file type, and so the syntax profile, for a new document: each profile with its extension, for example "CommonMark (.md)". |
| **Automatically save changes** | Saves a document that has a file as you work. |
| **Save without asking when closing a file** | Skips the "do you want to save?" question and saves. |
| **Versions to keep** | How many saved versions of each file Pilcrow keeps for Version History, from none to 500. The default is 50. "Versions to keep: none" turns history off. |
| **Record recent files and folders** | Lets Pilcrow remember what you opened, for **Open Recent** and for restoring at launch. |
| **Show hidden folders and files** | Shows items whose names start with a dot in the Files panel. |
| **When something is dropped onto the app** | What happens when you drop onto the editor or the sidebar: for a **Folder** or a **Markdown file**, **Open in editor** or **Insert link**; for an **Importable file** (a theme, syntax profile or macro collection), **Open in editor**, **Insert link** or **Import file**. |

## Translation

Translation needs macOS 15 or iPadOS 18 or later.

| Control | What it does |
| --- | --- |
| **Translate into** | Your default target language. The first choice is "System language". |
| **Speed** | **Fast**, **Best quality**, or **AI assistant**. Fast suits long documents and can be about twenty times quicker, with plainer wording; it needs macOS or iPadOS 26.4. **AI assistant** sends the text to your connection from **Settings ▸ Assistant**; your service may charge for it and the text leaves the device. |
| **When a file is in another language** | **Do nothing**, **Offer to translate**, or **Translate automatically**. Pilcrow works out a file's language when you open it, and nothing leaves the device for that. The offer shows a bar with a choice to translate into your default language. |
| **Offer Again for All Files** | Clears the files you set to **Never for This File**. |
| **After translating** | **Open in a new tab**, **Save a copy beside the original** (named like the original with the language added, such as `Notes_fr.md`), or **Replace the document** (which can be undone). |
| **Languages on This Device** | Lists each language with **On this device**, **Download** or **Not available**. Translation uses language packs that stay on the device. Downloading one asks the system for permission; remove one in the system's language settings. |

## Assistant

| Control | What it does |
| --- | --- |
| **Enable AI assistant** | Adds the Assistant panel to the sidebar. Nothing is sent until you ask, and only the text you choose to share. |
| A status line | **Ready.**, or the reason it is not: "The active connection's address is not usable.", "The active connection needs an API key.", or "Add a connection below. The Assistant pane appears once one is ready." |
| **Connections** | The list of connections, with "No connections yet." when empty. Each shows its name and, for the one in use, **Active**. A row offers **Make Active**, **Edit…** and **Remove**. |
| **Add Connection** | A menu: **OpenAI**, **Anthropic**, **OpenRouter**, **Ollama (this computer)**, **LM Studio (this computer)**, or **Custom…**. |
| **Excluded files** | Patterns for files that are never shared. `*` stands for any characters in a name, `**` for any folders, and a name ending in `/` covers a whole folder. Defaults include `*.pem`, `.env*`, `*.key` and `secrets/`. **Add** a pattern, **Remove** one, or **Restore Defaults**. |
| **Folders turned off** | Lists folders where you switched the assistant off, each with **Turn On**. Shows "No folders are turned off." when none. |
| **Privacy** | A link to read Pilcrow's privacy policy, and **Delete All AI Data…**, which removes every connection and saved key, the conversation and your privacy choices, and turns the assistant off. It asks first. |

Your API key is stored in the Keychain on this device only.

### The connection form

**Add Connection** and **Edit…** open a form.

| Field | What it does |
| --- | --- |
| **Name** | A label for the connection. |
| **Format** | **OpenAI-compatible** or **Anthropic**. |
| **Address** | The service's web address. Use `https://`, or `http://` only for this computer or your local network. |
| **Allow an unencrypted connection on my local network** | Permits an `http://` address on your network. It sends your text and key in the clear, so allow it only if you trust the network. |
| **Model** | The model to use, with **Choose…** to pick from the service's list. |
| **Needs an API key** and **API key** | Whether the service needs a key, and the key itself, held in the Keychain. Leave it blank when editing to keep the saved key. |
| **Test Connection** | Checks the address, key and model. Shows "Testing…" then "Connected (N ms)." |
| **Cancel**, **Save** | Close or keep the connection. |

## Diagnostics

| Control | What it does |
| --- | --- |
| **Record diagnostic log** | Records what Pilcrow is doing, so you can send it to support when something goes wrong. It stays on the device until you share it, and is built to leave out your document text and file names. While on, a red **Recording log** mark shows in the status bar. |
| **Stop recording after** | **1 hour**, **24 hours**, or **Never**. |
| **What to record** | A level for each part of Pilcrow: **Text editor**, **Macros**, **Themes**, **Parsing and profiles**, **Rendering and diagrams**, **Export and print**, **Files and library**, and **App**. Each is **Problems only**, **Normal**, **Detailed** or **Everything**. Problems and errors are always kept. |
| **Reproduce an issue** | Sets every part to Detailed and starts recording. Make the problem happen again, then finish the report. |
| **Add the log** | When you report a bug: **Ask each time**, **Always add**, or **Never add** the newest entries of the log to your clipboard to paste into the form. |
| **Report a Bug…** | Same as **Help ▸ Report a Bug…**. |
| **Include in a report** | Switches for **Device and system information**, **Pilcrow settings**, **Document structure (counts only)**, **Speed and memory**, **Trail of recent actions**, and **Crash details**. Document structure is how many headings, tables and so on the document has, never its words. Nothing is sent from this screen. |
| **View Log…** | Opens the log viewer (below). |
| **Clear Log…** | Permanently deletes the recorded log from this device, after asking. Turning recording off keeps what was recorded until you clear it. |

While you are recording a log for a bug report, **Reproducing — Finish Report** (or **Finish Bug Report** in the Help menu) stops recording and finishes the report. Recording stops by itself after 30 minutes in that case.

### The log viewer

**Diagnostic Log** shows a summary (**Entries**, **Sessions**, **Errors**, **Warnings**, **Crash reports**, and the date range), then the entries, newest first, with a **Search the log** field and **Part** and **Level** filters. Filters change only what you see, not what is sent. A report contains every entry in the log plus what you chose under Include in a report. **Reload** refreshes it. **Send Report** offers:

| Item | What it does |
| --- | --- |
| **Save Report…** | Keeps a file you can send yourself. |
| **Share Report…** | Opens the share sheet (AirDrop, Files and so on). |
| **Report on GitHub…** | Opens a new issue with a short summary. You choose **Add Log to Description** (the newest entries, up to 60,000 characters, which is all GitHub allows, copied to your clipboard to paste) or **Save and Attach File** (the whole log, in a file you add yourself). Reports on GitHub are public. |

When you start a report with nothing recorded, Pilcrow asks **Record the Problem First?**: **Record the Problem First**, **Report Now** or **Cancel**. When it opens the form it asks whether to **Add Log and Open Form**, **Always Add the Log**, or **Open Form Without Log**.

## Storage & Privacy

Pilcrow keeps recovery copies, history, access grants and support data inside its sandbox. Each category can be deleted separately. These controls never delete your documents.

| Section | Controls |
| --- | --- |
| **Documents** | **Review recovery data** and **Review version history**. Review lists the affected items with their sizes, so you can see the space before deleting anything. Tick the ones to delete (**Select All** or **Select None**) and choose **Delete Selected**. Recovery data cannot be reviewed while a document has unsaved changes: save or close it first. |
| **File Access** | **Clear Recent File Access…** removes recent-file lists, remembered Save As folders, session bookmarks and per-file syntax choices. |
| **Private & Support Data** | **Delete AI Data & Keys…** (connections, Keychain keys, the current conversation and AI privacy choices), **Delete Diagnostics…** (recorded logs and saved crash diagnostics), and **Clear Caches…** (re-creatable cached files and network responses). |

Every deletion asks for confirmation ("This cannot be undone. Your documents will not be deleted."). Custom syntax profiles, themes, macros, style guides and backdrops are not removed here; review and delete them on their own Library pages.

# Chapter 68: Editing

## Display & Typing

### Display

| Control | What it does |
| --- | --- |
| **Show line numbers** | Line numbers in the gutter. Same as **View ▸ Line Numbers**. |
| **Show current-line rule** | A thin rule under the line the caret is on. |
| **Styled Source** | Draws headings, bold and italic in a matching face. |
| **Heading Folds** | Fold chevrons beside headings. |
| **Rendered Blocks** | Draws tables, equations and diagrams as pictures with an edit button. |
| **Auto-Expand Sections** | Opens a folded section or a picture block when the caret arrives in it, and closes it when the caret leaves. |
| **Hide Markers** | Hides heading, bold and italic marks on every line except the caret's. Needs Styled Source. |
| **Wrap long lines** | When off, long lines scroll sideways instead of wrapping. Preview and exports always wrap. Lines of 20,000 characters or more, and Focus Mode, always wrap. |
| **Short lines in column mode** | What a column does on a line too short to reach it: **Use the end of the line**, **Leave the line out**, **Soft pad with spaces** (adds spaces so typed text lines up on screen), **Hard pad with spaces** (one space for every missing character, so it lines up by column number), or **Stop at the line**. Deleting never removes characters from a short line. |
| **Show status bar** | Turns the status bar at the bottom on or off. |
| **Formatting Toolbar** | Shows the optional toolbar under the text. |

### Typing

| Control | What it does |
| --- | --- |
| **Auto-pair brackets and quotes** | Typing an opening bracket or quote adds the closing one. |
| **Auto-pair Markdown ( \* \_ ` ~ )** | Does the same for Markdown's marks. |
| **Expand emoji shortcodes (:smile:)** | Turns a shortcode into the emoji as you type. A file that already contains one is shown as written. |
| **Continue lists and quotes on Return** | Return starts the next item, Return on an empty item ends the list, and Tab indents an item. |
| **Keep indentation on Return** | A new line starts with the same leading spaces or tabs as the one above. |
| **Insert spaces when pressing Tab** | Tab inserts as many spaces as the tab width, up to the next tab stop, instead of a tab character. |

Smart punctuation, highlight, subscript and superscript are under **Library ▸ CommonMark Options**.

### Typing sounds

| Control | What it does |
| --- | --- |
| **Play a sound as I type** | Each key makes a sound; Space, Return and Delete sound different. Pasting and undoing stay silent. On iPad the silent switch mutes it. |
| **Sound** | The pack: **Typewriter**, **Duck**, or **Kitten**. |
| **Volume**, **Preview** | Set the level and hear the pack. |
| **Your own sounds** | Choose a short clip for any kind of key; the others keep the sound picked above. The kinds are **Lowercase letters**, **Uppercase letters**, **Numbers**, **Symbols and punctuation**, **Space**, **Tab**, **Return** and **Delete**. Each has **Choose…** (or **Change…**), **Play** and **Remove**. Clips can be up to 2 seconds and 3 MB (WAV, AIFF, MP3, M4A or CAF), and are stored in memory so they play with no delay. |

### Spelling and diagnostics

**Check spelling while typing** underlines misspellings. **Show parsing warnings** marks lines where a construct is probably not what you meant, such as an unclosed code fence or math block, a link with no closing parenthesis, or a table row that does not match its header. The note appears at the end of the line. It changes what is shown, never how a document is parsed or exported.

## Images

These settings decide what happens to an image you insert (**Insert ▸ Image…**, or by dropping one in).

| Control | What it does |
| --- | --- |
| **Action** | **No special action**, **Copy image to current folder (./)**, **Copy image to ./assets**, or **Copy image to ./\${filename}.assets**. **Upload image** is shown as unavailable: Pilcrow has no image host, so images are inserted where they already are. |
| **Apply to local images** | Whether the action applies to images already on your device. |
| **Apply to online images** | Whether it applies to images that point to a web address. |
| **Load images from the internet** | Off, pictures that point to a web address are not downloaded for Preview, PDF or image export, so the site hosting them learns nothing. On, they are fetched like in a web browser, and that site can see the request. |
| **Use relative path if possible** | Writes a path relative to the document. |
| **Add ./ for relative paths** | Starts relative paths with `./`. |
| **Auto-escape image URLs on insert** | Escapes characters in the address that would break the link. |

# Chapter 69: Appearance

## Theme & Backdrop

| Control | What it does |
| --- | --- |
| **Application Theme** | The look of the app and editor: **Automatic**, **Light**, **Dark**, or any theme you add. It sets light or dark, the accent colour, the sidebar and bars, and the editor. Automatic follows the system. Render mode and exports use the Render Theme, chosen under Export. |
| **Interface Size** (iPad) | The size of menus, bars, the sidebar and dialogs: **System Size** (follows the iPad's Text Size), **One Step Smaller**, **Two Steps Smaller**, **Three Steps Smaller**. The editor's text has its own size. |
| **Menus in the Header** (iPad) | **Automatic** (hides Pilcrow's own menus while a keyboard or mouse is connected), **Always**, or **Never**. |
| **Zoom** | The editor and preview size: 50%, 67%, 80%, 90%, 100%, 110%, 125%, 150%, 175% or 200%. Same as **View ▸ Zoom In** and **Zoom Out**. |
| **Reading speed** | Words per minute, from 60 to 2,000, used for reading-time estimates. |

## Editor Background (the backdrop)

A picture or video can sit behind the editor, the sidebar and the status bar.

| Control | What it does |
| --- | --- |
| **Media** | **Choose…** a HEIC, PNG, JPEG or SVG picture, or an MP4, MOV or M4V video. **Remove** clears it. |
| **Layout** | **Fill**, **Fit** or **Tile**. |
| **Behind the Text Area**, **Behind the Sidebar** | Each has its own **Dim** and **Blur**. **Dim** covers the picture with the theme's background colour so text stays readable; **Blur** softens it. The status bar blurs it. |
| **Play on Battery** | Lets a video play on battery power. A video pauses in Low Power Mode and stays still with Reduce Motion. |
| **Sound**, **Volume** | A video plays muted unless you turn on its sound. |

A backdrop never appears in Preview or in exports, and Reduce Transparency hides it.

## Text Size & Fonts

| Control | What it does |
| --- | --- |
| **Font size** | The editor's font size, 9 to 32 points. The editor font, the script-aware fonts and the line rhythm are sized together, and it applies immediately. |
| **Line spacing** | Space between lines, as a multiple of the font size, in steps of 0.1. |
| **Tab width** | How wide a Tab is drawn, 2 to 8 spaces of the editor font. |
| **Text width** | How much of the editor's width the text takes, from 50% to 100%, centred. Focus Mode has its own column. |
| **Editor font**, **Gutter font** | The font for the text and for the line numbers. A filter (**All**, **Monospace**, **Sans-serif**, **Serif**) narrows the list without changing your choice. The defaults are **System Default** and **System Monospace**. |

# Chapter 70: Table of Contents and Export Defaults

## Contents & Labels

These settings apply to every export format: PDF, Word, HTML and the rest.

| Control | What it does |
| --- | --- |
| **Add a table of contents to every export** | Puts a contents list at the top of each export. |
| **Replace a [TOC] line with the list** | A line that is only `[TOC]` becomes the list of headings in Preview and every export. |
| **Number headings (1., 1.1.)** | Numbers headings in the output. Heading labels, below, replace plain numbering. |
| **Title** | What the list is called, for example "Contents" or "Instructions". Empty uses "Table of Contents". |
| **List headings down to level** | Depth, 1 to 6. Level 1 lists only the top headings; level 6 lists them all. |
| **Indentation** | The indent in points for each level. |
| **Link each heading back to its contents entry** | Adds back-links from headings to their entries. |
| **List only headings below the [TOC] line** | Leaves out headings above the `[TOC]` line. |

### Heading labels

**Label headings** gives each level its own label, for example "Part I -" or "Chapter 3:". Each level has a template. In a template, `#` is the next number and `@` the next capital letter; a label can use one of them, not both. Write `\#` or `\@` to start counting again each time a shallower heading appears; bare, it keeps counting through the document. **Letters** and **Digits 0 to 9** set the characters used for lettering and numbering. After the last letter, letters double: Y, Z, AA, AB.

## Export Defaults

| Control | What it does |
| --- | --- |
| **Render Theme** | The default theme for Preview and exports. |
| **Format**, **File extension**, **Converter** | Information about each export format. All are produced by a built-in converter. |
| **Page** | The paper size, orientation and margins used for printing and for every PDF, PDF Archive and Word export (Chapter 64). |
| **Header template**, **Footer template** | Text for the top and bottom of each page. Variables: `${title}`, `${author}`, `${pageNo}`, `${pageCount}` and `${today}`. For example, the footer `Page ${pageNo}`. |
| **Author** | The author name used by `${author}` and in the document's metadata. |
| **Page break between top-level headings** | Starts each top-level heading on a new page. |

# Chapter 71: Library

The Library is the themes, syntax profiles, macros, style guides and backdrops you add. Built-in items are read-only; duplicate one to change it.

## Syntax Profiles

Lists each profile as **Built-in** or **Custom**.

| Control | What it does |
| --- | --- |
| **Import…** | Adds a profile `.json` file someone shared. |
| **New** | Starts a profile from scratch. |
| **Edit**, **Duplicate**, delete | Per profile. Built-in profiles can be duplicated but not edited or deleted. |
| **Not Loaded** | A profile that could not load is listed here with the reason: it uses a file extension another profile already has, it is not a profile this version can read, or it contains a pattern that could make the editor stop responding. It is still in your profiles folder. |

Profile editing is in Chapter 74.

## CommonMark Options

Switches for optional CommonMark syntax. Enable only what your source uses.

| Section | Controls |
| --- | --- |
| **Syntax support** | **Highlight (==key==)**, **Subscript (H~2~O)**, **Superscript (X^2^)**, **Inline math ($…$)**. |
| **Additional syntax** | **Auto links (bare URLs)**, **GitHub-style alerts**, **YAML front matter** (a block of `---` lines at the very top is dimmed and left out of Preview and every export), **Diagrams and charts (Mermaid, Vega-Lite)**. |
| **Smart punctuation** | **Convert**: **Convert on Input**, **Convert on Rendering**, or **Off**. Then **Smart quotes**, **Smart dashes**, **Smart ellipsis**. |
| **Code fences** | **Display line numbers**, **Auto-wrap long lines**, and **Indent size** (in spaces). |

Format ▸ Highlight, Subscript, Superscript and Inline Math are greyed out until their option is on.

## Themes

A Theme page lists **Application Themes** (JSON: the app's light or dark appearance, accent, sidebar, bars and editor) and **Render Themes** (CSS: Preview, HTML, PDF, image and print output, and Word styles). Each is labelled **Built-in** or **Custom**, with **Light**, **Dark** or **Automatic**.

| Control | What it does |
| --- | --- |
| **New** | Creates a theme of either kind. |
| **Import Theme…** | Adds a `.json` Application Theme, a `.css` Render Theme, or a `.zip` package holding either or both. |
| **Open Theme Folder** | Reveals the folder holding your themes. |
| **Edit**, **Duplicate**, **Export**, delete | Per theme. Built-in themes are read-only. |

Theme editing is in Chapter 75.

## Macros

Lists macro collections. Built-in collections are read-only.

| Control | What it does |
| --- | --- |
| **New Collection**, **Import Macros…** | Start a collection or import a `.json` collection. |
| A collection's menu | **Rename…**, **Duplicate Collection**, **Export Collection…**, **Delete Collection**. |
| **New**, **Edit**, **Duplicate**, delete | Per macro. |

Macro editing is in Chapter 76. An imported collection with an unsafe trigger is refused.

## Style Guides

Lists style guides, each with its rule count and areas.

| Control | What it does |
| --- | --- |
| **Import Style Guide…** | Adds a guide `.json` file. |
| A guide's menu | **Duplicate Style Guide**, **Export Style Guide…**, **Delete Style Guide…**. Deleting removes it from this device, after you confirm, so export it first if you want a copy. |
| "Builds on …" | A guide can build on another. If that guide is missing, it cannot be used. |

A style guide is a `.json` file of named rules. You can also ask the assistant to write one (**Assistant ▸ Help ▸ A style guide**), and **Help ▸ Style guides** explains the format.

## Rendering Libraries

Math, diagrams and charts are drawn on this device by bundled libraries. This page lists each library and its version; choose one to read its bundled notices.

## Location

Your library lives in a folder named "Pilcrow Library" inside the folder you choose. A folder in iCloud Drive keeps it in sync between your devices. Preferences, API keys and crash-recovery copies always stay on this device.

| Control | What it does |
| --- | --- |
| **Kept** | Where the library is now: "On this device" or "In the folder *name*". |
| **Choose Folder…** | Moves the library to a folder. If the folder already holds a Pilcrow library, Pilcrow will not merge two: you can **Use What Is There**. Otherwise **Move My Library Here** (checks every file, then removes the old copy) or **Copy My Library Here** (keeps the old one). |
| **Use This Device** | Brings the library back to this device. |

If the chosen folder cannot be reached, Pilcrow uses the library on this device for now, changing and deleting nothing, and uses the folder again when it is available.

## Import (iPad)

On iPad, **Import** adds items to the library: **Import Theme…**, **Import Syntax Profile…**, **Import Macro Collection…**, **Import Style Guide…**. On Mac, use **File ▸ Import** (Chapter 53).

# Chapter 72: Keyboard

**Settings ▸ Keyboard ▸ Shortcuts** lists every command whose shortcut you can change, with its current key.

| Control | What it does |
| --- | --- |
| A command's row | Click it, press the new shortcut, then choose **Save**. **Unbind** removes the shortcut. **Cancel** keeps the old one. If the shortcut was in use by another command, that command is cleared and the page tells you which. |
| **Super Tab keys** | The keys for **Next Field** and **Previous Field**, which jump between the blanks a macro leaves: `⌥Tab` and `⌥⇧Tab`, or `⌃⌘]` and `⌃⌘[`, or **Custom**. |
| **Reset All Shortcuts** | Restores every default. |

The commands you can change, with their defaults, are:

| Command | Default |
| --- | --- |
| Strong | `⌘B` |
| Emphasis | `⌘I` |
| Inline Code | `⌃`` ` `` |
| Inline Math | `⌃M` |
| Strikethrough | `⌃⇧`` ` `` |
| Hyperlink | `⌘K` |
| Clear Format | `⌘\` |
| Toggle Sidebar | `⇧⌘L` |
| Sidebar: Outline | `⌃⌘1` |
| Open Documents | `⌃⌘2` |
| Sidebar: File Tree | `⌃⌘3` |
| Sidebar: Search | `⇧⌘F` |
| Sidebar: Assistant | `⌃⌘4` |
| Add Caret Above | `⌃⇧↑` |
| Add Caret Below | `⌃⇧↓` |
| Carets in a Column… | `⌃⇧G` |
| Go Back | `⌃⌘←` |
| Go Forward | `⌃⌘→` |
| Select Next Occurrence | `⌃⌥D` |
| Select All Occurrences | `⌃⌥⇧D` |
| Next Field | `⌥Tab` |
| Previous Field | `⌥⇧Tab` |
| Command Palette… | `⌃⇧P` |
| Focus Mode | none |

Commands not on this list, such as Save, Find and the Paragraph items, have fixed shortcuts. Chapter 77 lists all shortcuts.

# Chapter 73: Subscription & Credits

Every feature in Pilcrow is free. Supporting Pilcrow is optional: it helps pay for development, and it gives you votes on what gets built next. Votes guide the order of work but do not promise any feature.

The **Support Pilcrow** page has:

| Part | What it shows or does |
| --- | --- |
| **Your votes** | **From your subscription** (the votes for this paid month, with when they expire) and **Bought** (votes that never expire). Subscription votes are used first and expire when the paid month ends. |
| **Get votes** | The subscription and the single votes you can buy. Pilcrow Supporter renews every month until you cancel it in your Apple Account settings. Each paid month gives you votes. |
| **Restore Purchases** | Brings back purchases made on another device. |
| **Terms of Use**, **Privacy Policy** | Links. |
| **App Icon** | A choice of app icons for subscribers. Icons for a voting round are earned by subscribing during that round, and are kept. On the Mac the icon changes in the Dock while Pilcrow is open. |
| **Roadmap** | The current round of features open for voting, with "Votes" and "Yours" counts and a **Vote** button for each. Each vote uses one of your votes and cannot be taken back. Between rounds it says when the next opens. |

If support options are not available in a particular build, the page says so.
