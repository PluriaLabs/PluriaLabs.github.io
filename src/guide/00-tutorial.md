# Pilcrow User Guide

## A tutorial course for writing, organizing, reviewing, and publishing plain text

This is the definitive task-based guide to Pilcrow for Mac and iPad. The tutorial chapters are not a list of buttons: each starts with a result you can achieve, walks through the work, and explains why the choices matter. The reference chapters at the end are the opposite, and list every control in the app.

Pilcrow is a professional plain-text editor whose syntax is controlled by profiles. You can use the built-in CommonMark profile, teach Pilcrow another markup language, automate repeated text with macros, review writing against a house style, and publish the same source as HTML, PDF, or Word.

The reference chapters (Parts XVI–XXI) were written from the application on **November 24, 2026**. The tutorial chapters (Parts I–XV) were first written on November 10, 2026, and their control names were checked again on November 24. Menu names describe the Mac interface; on iPad, the same commands are usually in the toolbar or **More** menu. A hardware keyboard exposes most of the same shortcuts.

No chapter requires programming unless it is explicitly labeled advanced.

---

## How to use this guide

If you are new, work through Parts I–III in order. You will create a document, learn the workspace, format without losing control of the underlying text, preview the result, and save safely. Then choose the route that fits your work:

- Writers and editors: Parts IV, V, VI, and IX.
- Researchers and technical writers: Parts IV, VII, and VIII.
- Book authors: Part X.
- People building their own syntax, themes, or automation: Parts XI–XIII.
- Administrators and privacy-conscious users: Parts XIV–XV.
- Anyone looking up a specific menu item, button, setting or dialog: Parts XVI–XXI, the reference chapters. They describe every control in the app, menu by menu and page by page.

Instructions use **Choose File ▸ Save** for a menu path and `⌘S` for a shortcut. “Source” means the plain text you edit. “Preview” means the rendered, read-only page. “Library” means Pilcrow’s collection of profiles, themes, macros, style guides, and related app data; it is not your document folder.

[TOC]
---
# Part I — Start writing

# Chapter 1: Understand Pilcrow’s four building blocks

## Tutorial: follow one sentence from source to publication

Create a blank document and type:

```text
# Field Notes

The river rose overnight.
```

Four independent parts of Pilcrow now cooperate:

1. The **document** is the plain-text file. It remains readable in any text editor.
2. The **syntax profile** says that `# Field Notes` is a heading. CommonMark is the usual profile for a `.md` file.
3. The **Application Theme** controls the app and editor. The **Render Theme** controls Preview and exports.
4. A **macro**, if you use one, can insert repeated text such as the date or a signature.

Switch to **Preview**. The leading `#` becomes a real heading because the profile supplied meaning and the Render Theme supplied presentation. Switch back to **Edit** and the source remains exactly what you typed.

This separation is the key to Pilcrow. Use a profile to change meaning, a Render Theme to change published appearance, and an Application Theme to change your writing environment. Do not add spaces or markup merely to imitate page layout in the source; express structure and let the theme handle presentation.

# Chapter 2: Create, open, and save your first document

## Create and save

1. Choose **File ▸ New Document** (`⌘N`).
2. Type a few lines.
3. Choose **File ▸ Save** (`⌘S`).
4. Pick a folder and filename. Use an extension that matches the intended syntax, such as `.md` for CommonMark.
5. Save again after another change and notice that Pilcrow now writes without asking for a location.

The first save establishes the document’s identity, folder, and extension. The folder matters because relative links and images are resolved from it. The extension helps Pilcrow choose an appropriate syntax profile.

## Open an existing file

- On Mac, choose **File ▸ Open File…** (`⌘O`), double-click a supported text file in Finder, or drag it onto Pilcrow.
- On iPad, use the file picker, Files app, or a share sheet. Pilcrow edits the chosen file in place when the provider permits it.
- To work with related files, choose **Browse Enclosing Folder…** or open a folder in the sidebar.

Pilcrow supports ordinary text and markup files and detects their text encoding. A file handed in by another app or cloud provider may need continued access; do not move or revoke the file while it is open.

## Save As and rename

Use **File ▸ Save As…** to create a separate copy in another location or encoding. Use the document-title menu’s **Rename** when you want the current document to keep its identity but gain another name. Save As is the safer choice before an experiment because the original remains unchanged.

## Close safely

Choose **File ▸ Close** (`⌘W`) for the active document or **Close All** (`⇧⌘W`) for all documents. If a document has unsaved changes, Pilcrow asks whether to save, discard, or cancel. Read the filename in that prompt; several open documents may have similar names.

# Chapter 3: Learn the workspace

Open a document and identify these areas:

- The **sidebar** changes among Outline, Files, Search, Project, and Assistant when those panels are available.
- The **document title control** shows the active file and opens the document switcher.
- The **mode control** chooses Edit, Preview, or Side by Side.
- The **editor** is the native text area. Its gutter may show line numbers and fold controls.
- The optional **formatting toolbar** provides common profile-aware formatting and insertion commands.
- The **status bar** reports words, characters, lines, cursor position, encoding, profile, background activity, and warnings.

## Practice switching panels

1. Choose **View ▸ Outline** to see headings from the active profile.
2. Choose it again to hide that panel.
3. Choose **View ▸ File Tree** to browse the open folder.
4. Choose **View ▸ Search** for folder-wide search.
5. If an assistant connection exists, choose **View ▸ Assistant**.
6. Use **View ▸ Toggle Sidebar** to hide or restore the whole sidebar.

The same command toggles a panel: choosing an already-visible panel hides the sidebar. This makes it quick to reclaim width without losing the chosen panel.

## Read the status bar

Click the encoding to convert on the next save. Click or use the profile control to change how the document is parsed. Treat **Out of sync**, parsing warnings, or a long-running activity label as actionable information. Save a copy before continuing if Pilcrow reports that its editing view and document model disagree.

# Chapter 4: Work with several documents

Open two or more files. Click the filename at the top to open **Open Documents**, then choose another document. The same menu can create, save, rename, or close documents.

Use `⌃Tab` for the next document and `⌃⇧Tab` for the previous one. Choose **View ▸ Open Documents** when you want a searchable or explicit list instead of cycling.

Each document keeps its own cursor, selection, scroll position, mode, profile choice, and find state. A folder search is a workspace operation; a document Find belongs to one document. Before closing many tabs, save each dirty document or use the prompts rather than assuming autosave has already run.

---

# Part II — Write efficiently

# Chapter 5: Move, select, and edit text

Pilcrow uses the platform text system, so ordinary cursor movement, drag selection, copy, cut, paste, and system input methods work normally.

## Select useful units

Use **Edit ▸ Selection** to select the current word, line, or paragraph. You can also jump to the top, bottom, line start, or line end. These semantic commands are useful when a wrapped screen line differs from a real file line.

Default shortcuts include `⌘D` for Select Word, `⌘L` for Select Line, and `⌥⌘P` for Select Paragraph. `⌃A` and `⌃E` jump to the start and end of the line.

## Copy and paste deliberately

- **Copy as Markdown** preserves useful source markup.
- **Copy as Plain Text** removes structural markup where possible.
- **Copy as HTML Code** places HTML source on the clipboard.
- **Paste as Plain Text** (`⇧⌘V`) discards rich formatting from the clipboard.

Choose the representation based on the destination. Plain text is safest for bringing prose from a browser or word processor into source. HTML code is useful when handing rendered structure to a web workflow.

## Undo and redo

Use `⌘Z` and `⇧⌘Z`. Complex actions such as a selected comparison change, multi-caret formatting, or a translation replacement are designed to be one undo step. After a large operation, undo immediately if the result is wrong; later unrelated edits make recovery harder to reason about.

# Chapter 6: Find, replace, and navigate

## Find in source

1. Choose **Edit ▸ Find ▸ Find…** (`⌘F`).
2. Enter a term.
3. Optionally enable Match Case, Whole Word, or Regular Expression.
4. Use Return or `⌘G` for the next match and `⇧⌘G` for the previous match.
5. Enter replacement text in Edit mode when you want to replace one or all matches.

Regular expressions are powerful but literal search is easier to audit. When using capture groups, test on one result before Replace All.

## Find in Preview

In Preview, Find searches the rendered words rather than the source markup. All matches are highlighted and the active match is distinct. Preview cannot replace because it is not editable. Matches split by formatting, or text inside code, diagrams, and equations, may not appear. Switch to Edit to search the literal source.

In Side by Side, Find searches the source and highlights corresponding rendered matches.

## Go to line and column

Choose **Edit ▸ Go to Line…** (`⌃G`). Enter `120` for line 120 or `120:8` for line 120, column 8. Values beyond the document clamp to the last valid place. File lines, not visually wrapped lines, determine the count.

## Go back and forward

When you open search results, links, or distant locations, use **Go Back** and **Go Forward** to retrace navigation. This is separate from Undo: navigation history changes where you look, not document content.

# Chapter 7: Use multiple carets and column editing

## Edit repeated occurrences

1. Select a word.
2. Choose **Select Next Occurrence** repeatedly to add matching selections.
3. Type once. Every selected occurrence changes in the same transaction.
4. Undo once if needed.

Use **Select All Occurrences** only after confirming the term is specific enough. A short word may match places you did not intend.

## Add carets vertically

Place the caret in a line, then choose **Add Caret Above** or **Add Caret Below**. Continue until each target row has a caret. Typing, deletion, and supported formatting apply to all carets.

## Place carets in a column

Choose **Carets in a Column…**, specify the line range and column, preview the placement, and confirm. This is ideal for adding a prefix to a rectangular run of lines. Short lines clamp safely rather than being padded invisibly.

Column selection is displayed with a badge. Exit multi-caret editing with Escape or by clicking a single location. Before running a destructive command, scan the document for every caret.

With several carets, Pilcrow deliberately turns off smart pairs, list continuation, and curly-quote substitution: one keystroke inserts one literal character at every caret. On iPad, use a hardware keyboard or **More ▸ Carets in a Column…**. For a touch column drag, enable **More ▸ Column Selection** and drag one finger; two fingers still scroll. With a trackpad or mouse, hold Option while dragging. A drag can cover only lines currently loaded in the editor.

# Chapter 8: Run line, case, and deletion commands

Select the lines you want, then use the line-operation commands to:

- Sort ascending or descending.
- Reverse line order.
- Remove duplicate lines.
- Remove blank lines.
- Trim trailing whitespace.
- Join lines.
- Move a row up or down (`⌥⌘↑` and `⌥⌘↓`).

Use case transforms for upper case, lower case, or capitalization. Use Delete Word, Delete Line, or Delete Paragraph when a semantic unit is easier than a drag selection.

The selection determines scope. With no useful selection, some commands operate on the current line or paragraph. For a large cleanup, save first so Version History records the earlier state, then run one operation at a time and inspect the result.

# Chapter 9: Use the command palette and customize shortcuts

Open **Command Palette…** from the Edit or navigation commands. Type part of an action, such as “fold,” “export,” or “caret,” then run it without hunting through menus. The palette is especially valuable on iPad, where menu depth and screen width are limited.

To change shortcuts:

1. Open **Settings ▸ Keyboard ▸ Shortcuts**.
2. Search or filter for an action.
3. Choose its shortcut and press the new combination.
4. Resolve any reported conflict, then save.
5. Use **Unbind** for an action you do not want assigned.

Choose a field-navigation scheme for Super Tab if offered. Use **Reset All Shortcuts** to return to defaults. Pilcrow applies supported changes live; a relaunch should not be necessary.

Avoid overriding operating-system conventions unless the productivity gain is clear. Keep related commands systematic—for example, one modifier difference between next and previous.

---

# Part III — Structure and preview

# Chapter 10: Format text through the active profile

Formatting commands write plain-text marks defined by the active syntax profile. They do not secretly store rich text.

## Tutorial: format a short note

1. Type a title and a paragraph in a `.md` document.
2. Put the caret in the title and choose a heading level from **Format**.
3. Select a phrase and choose **Strong** (`⌘B`) or **Emphasis** (`⌘I`).
4. Select a technical term and choose inline code.
5. Turn two lines into a bulleted or numbered list.
6. Switch to Preview to inspect the structure.

If a command is unavailable, the active profile does not declare a way to write that construct or Preview is active. Change profiles only when the document genuinely uses another syntax; otherwise you can reinterpret existing marks unexpectedly.

Paragraph commands include headings, lists, block quotes, code fences, tables, alerts, horizontal lines, links, references, footnotes, a table of contents marker, and YAML front matter when the profile supports them. Inline commands include strong, emphasis, strikeout, code, links, images, highlight, subscript, superscript, and other declared roles.

Use **Paragraph** to remove a block role, **Clear Format** to return selected inline content toward ordinary paragraph text, and **Increase Heading Level** or **Decrease Heading Level** to move through the profile’s heading hierarchy. Lists support unordered, ordered, and task forms; **Toggle Task Status** checks or unchecks the current task, while **Indent** and **Outdent** change nesting. Default paragraph shortcuts include `⌘0` through `⌘6`, `⌥⌘U` for unordered list, `⌥⌘O` for ordered list, `⌥⌘X` for task list, `⌥⌘Q` for block quote, and `⌥⌘C` for a code fence.

# Chapter 11: Insert tables, images, fields, and special blocks

The **Insert** menu combines shared tools with constructs supplied by the active profile.

## Insert a table

1. Choose **Insert ▸ Table…** or **Format ▸ Paragraph ▸ Table ▸ Insert Table…** (`⌥⌘T`).
2. Choose rows, columns, alignment, and header behavior as offered.
3. Confirm, then replace placeholder cells.

A source table is best for real tabular relationships. Do not use it merely to align unrelated prose; that creates poor accessible output.

With the caret in a table, use **Format ▸ Paragraph ▸ Table** to add a row above or below, delete the current row, add a column before or after, or delete the current column. Pilcrow rewrites the source table as one undoable edit. Inspect alignment markers after structural changes when the profile uses them.

## Insert an image

Choose **Insert ▸ Image…** or `⇧⌘I`, select the file, and provide useful alternative text. Pilcrow follows the image preferences described in Chapter 26: it may copy or move the file, keep it in place, and write a relative or absolute reference.

## Insert ready-made blocks

Use **Diagrams**, **Charts**, or **Equations** for an editable template. Use **Code Fence**, **Alert**, **Horizontal Line**, **Link Reference**, **Footnote**, **Table of Contents**, or **YAML Front Matter** when supported. Templates are starting source, not locked widgets; edit them directly.

## Insert a field

Choose **Insert ▸ Field** to place a named fill-in field for Super Tab. The field uses the active profile’s marks. Type its name while it is selected, then use it in a reusable macro or document template.

# Chapter 12: Use Edit, Preview, and Side by Side

## Edit

Edit shows the source and accepts changes. Use it for writing, literal search, replacements, and source-level inspection.

## Preview

Choose **View ▸ Preview** (`⇧⌘P`) or the mode control. Preview compiles the active profile’s structure with the chosen Render Theme. It is intentionally read-only. Use it to evaluate hierarchy, spacing, links, equations, diagrams, charts, and export appearance.

## Side by Side

Choose **View ▸ Side by Side** (`⌃⌘P`). Source appears beside Preview and updates as you type. Scrolling is synchronized by headings where possible, with proportional fallback. Find in the source highlights related Preview text. Go to Line moves the editor and follows in Preview.

Hide the sidebar when both panes feel narrow. A narrow window may be better served by switching between Edit and Preview.

## Diagnose an unexpected Preview

Check these in order:

1. Is the intended syntax profile active?
2. Is the source structurally valid for that profile?
3. Is the intended Render Theme selected?
4. Are optional CommonMark features enabled?
5. Is a supplemental block labeled with a supported language?

This order separates meaning problems from styling problems.

# Chapter 13: Control the reading and editing view

Use the View menu and Editing or Appearance settings to control:

- **Formatting Toolbar**: show or hide the quick-format row.
- **Focus Mode**: remove distractions around the document.
- **Actual Size, Zoom In, Zoom Out**: change the viewing scale without changing export typography.
- **Line Numbers**: show file line numbers in the gutter.
- **Current-Line Rule**: emphasize the active line.
- **Wrap Lines**: wrap long lines to the view width. Turning it off enables horizontal reading of long records.
- **Styled Source**: color and style recognized source roles.
- **Hide Markers**: reduce visible markup while Styled Source is active.
- **Rendered Blocks**: render eligible blocks within the editing experience.
- **Heading Folds**: collapse sections beneath headings.
- **Fold All / Unfold All**: change every heading fold.
- **Auto-Expand Sections**: reveal a folded section when you navigate into it.

Styled Source does not change the file. Hide Markers can make markup easier to read but may obscure the literal characters you are editing; turn it off when diagnosing syntax. Folding hides text rather than deleting it. Use Unfold All before a whole-document visual review.

When a rendered block offers editing, activate it to open **Edit Block**. Change the monospaced source, then choose **Apply** to replace that block or **Cancel** to leave it untouched. The sheet rejects an empty block. This keeps the convenient rendered view without hiding the source that will be saved.

---

# Part IV — Files, folders, and large documents

# Chapter 14: Browse a working folder

Open a folder or choose **Browse Enclosing Folder…** for the active document. The Files sidebar shows the tree without importing or moving files. Select a text file to open it. Use the folder as the shared scope for Search, book projects, and relative links.

For keyboard-first opening, choose **File ▸ Open Quickly…** (`⇧⌘O`) after a folder is open. Type any ordered portion of a filename, use Up and Down to choose a result, and press Return. Pilcrow shows shortened folder-relative paths so files with identical names can be distinguished. Open Quickly is absent or disabled when no workspace folder exists.

The sidebar represents real files. Renaming, moving, or deleting a file can break links in other documents, so run Check Links after structural changes. Cloud folders can report changes asynchronously; wait for synchronization before assuming a conflict is a Pilcrow error.

Use the launch settings to choose whether Pilcrow restores the last session, opens a particular folder, or starts elsewhere. Use file-tree preferences to tune what the library displays and how dropped items are handled.

# Chapter 15: Search and replace across a folder

## Search

1. Open the folder.
2. Choose the Search sidebar (`⇧⌘F` by default).
3. Choose **Folder** scope.
4. Enter the search term and optional Match Case, Whole Word, or Regular Expression controls.
5. Open a result to inspect it in context.

## Replace transactionally

1. Choose **Replace…** beside the result count.
2. Enter the replacement.
3. Review each affected file, match count, and before/after sample.
4. Deselect files that should remain unchanged.
5. Confirm the final match and file count.

Pilcrow skips open files, non-UTF-8 text, and files changed after the preview. This prevents a folder operation from silently overwriting newer work. A replacement affects at most 2,000 files at a time.

Afterward, use the replacement window’s **Undo** banner to restore the latest batch. A file edited since replacement is left alone. Only the most recent folder replacement has this special backup, so validate before starting another.

# Chapter 16: Work safely with very large files

Pilcrow does not load a huge document into one giant string. It keeps the original file backed by storage and materializes a window around what you see. This is why multi-gigabyte files can open quickly.

For best results:

- Wait for line counting before relying on distant line navigation.
- Expect a brief refresh when jumping far from the current viewport.
- Save before whole-file transformations.
- Prefer folder search or targeted Find over selecting an entire enormous file.
- Remember that PDF creation uses a whole rendered page model and can require much more memory than editing or streamed HTML/Word export.
- Keep the source file available while it is open. External truncation or replacement can invalidate the mapped original.

The status bar may show background lexing or parsing. You can usually keep typing. If a feature asks you to save a document over a stated sharing or review limit, save rather than forcing a temporary in-memory copy.

# Chapter 17: Use encodings, autosave, recovery, and versions

## Convert encoding

Pilcrow detects and preserves a file’s encoding. Click the encoding in the status bar and choose another encoding; the next save performs the conversion. If text looks garbled, do not edit extensively—try the correct encoding first.

## Configure autosave and recovery

In **Settings ▸ General ▸ Files**, choose whether changes save automatically and configure recovery behavior. Autosave reduces risk but is not a substitute for intentional checkpoints before bulk edits.

After an unexpected quit, Pilcrow offers recovery copies for unsaved work. Review the document name and recover or discard deliberately. Recovery can replay unsaved edits when the original file identity still matches; stale or replaced originals may fall back to the safe version available on disk.

## Use Version History

1. Save the document.
2. Make a meaningful change and save again.
3. Choose **File ▸ Version History…**.
4. Select a version.
5. Use **Open Copy** to inspect it, **Compare…** to see line changes, or **Restore…** to return to it.

Restore requires no current unsaved changes and first preserves the current state, so a restore can itself be reversed through history. Unchanged saves do not create duplicate versions. Files over 256 MB are not copied into history. Set the number retained—none to 500—in Files settings.

# Chapter 18: Compare documents and accept selected changes

## Take back one historical change

Open Version History, choose an earlier version, and compare it with the current document. Each change offers **Take Back** when the earlier version is on the old side. Use it to restore only that line group. Undo reverses the action.

## Review a colleague’s file

1. Open your working document.
2. Choose **File ▸ Compare with File…**.
3. Select the colleague’s copy.
4. Review added and removed lines.
5. Choose **Accept** for changes you want and **Reject** for those you do not.
6. Use **Reconsider** to restore a rejected option or **Accept All Remaining** after review.

Pilcrow applies a change only if the target text still matches the comparison baseline. If you edited that region in the meantime, it is skipped. Changes are line groups; accept and then edit when only part of a line is wanted. Very large individual changes are left for manual copying.

---

# Part V — Quality and language

# Chapter 19: Check links before publishing

Choose **Edit ▸ Check Links…**. Pilcrow checks relative files, images, heading fragments, cross-file fragments, and reference definitions. It skips code and does not visit web URLs.

Click a problem to jump to its source line. Correct the destination, save if the document needs a folder context, and choose **Check Again**.

Run this tutorial after renaming project files:

1. Rename a linked file.
2. Check links in the referring document.
3. Open the missing-file result.
4. Update the path.
5. Check again until no local problems remain.

A clean local check does not prove that an external website is reachable; Pilcrow deliberately avoids unsolicited network requests.

# Chapter 20: Translate a document or selection

Translation uses Apple’s on-device language models and requires macOS 15 or iOS 18 or later.

1. Choose **Edit ▸ Translate ▸ Document** or **Selection**.
2. Confirm the detected source language.
3. Choose the target language.
4. Choose whether the result opens in a new tab, saves beside the original, or replaces the source when that option is available.
5. Start translation and watch progress in the status bar.

Pilcrow preserves structural markers, code, links, and front matter. It translates selected human-language portions of math, diagram, and chart blocks where supported. Replacing a selection is one undo step; whole-document translation normally protects the original through the configured output choice.

In **Settings ▸ General ▸ Translation**, set a default language, choose whether to offer or automatically translate foreign-language files, and choose what happens afterward. Use **Never for This File** on an offer bar to suppress that document without disabling translation globally.

# Chapter 21: Review writing with a style guide

## Install or choose a guide

Open **Settings ▸ Library ▸ Style Guides**. Import a guide or use the example house style. A guide can contain variants and review areas such as terminology, mechanics, voice, or accessibility.

## Run a review

1. Open the Assistant sidebar and choose **Style Review**.
2. Choose a style guide and variant.
3. Choose review areas.
4. Choose Selection or Document scope.
5. Review the disclosure of what will be sent and where.
6. Start the review.
7. Inspect each finding, its evidence, explanation, and suggested fix.
8. Apply only findings you agree with.

Local deterministic checks can identify exact rules without sending text. Model-assisted checks require the active provider and may divide a long document into several requests. Pilcrow tells you the request count and approximate shared size before a whole-document review.

Treat findings as reviewable evidence, not commands. A style rule may be inappropriate in dialogue, quotation, code, or intentionally unusual prose. Apply fixes one at a time when meaning matters, and use Undo immediately if a fix changes intent.

## Write a style guide

Create or duplicate a guide in Style Guides settings. Give each rule a clear name, rationale, examples, scope, and severity. Prefer a precise rule that can explain itself over a vague instruction such as “write better.” Test against a short document containing both violations and legitimate exceptions.

# Chapter 22: Use speaking, spelling, and writing statistics

Use **Edit ▸ Speech ▸ Start Speaking** to hear selected text or the appropriate document text, and **Stop Speaking** to end playback. Listening reveals repeated words and missing punctuation that visual proofreading can miss.

Enable **Check spelling while typing** in Editing settings to use the platform spelling service. Spelling is a writing aid, not a syntax validator; identifiers and invented terms may be marked even when correct.

The status bar reports words, characters, and lines. Settings also include reading speed and editor word-count behavior. Pilcrow records writing sessions for aggregate statistics while documents are open and edited. These counts are useful for trends, not contractual publishing counts: profiles and export rules can interpret words differently.

---

# Part VI — Macros and fill-in fields

# Chapter 23: Use and create macros

## Use a macro

Enable a collection in **Settings ▸ Library ▸ Macros**, return to Edit, and type a macro’s trigger. Depending on its match type, it expands after the trigger, at a prefix, around a selection, or when a pattern matches.

## Create one

1. Open Macros settings.
2. Create or choose a collection.
3. Choose **New Macro**.
4. Give it a name, trigger, match type, and expansion.
5. Enable it and decide whether it must avoid code.
6. Save and test it in a disposable document.

An expansion can include variables for date, time, UUID, clipboard, selection, counter, filename, filepath, and custom values. Use variables when the structure repeats but a value changes.

Collections can be duplicated, renamed, exported, imported, enabled, disabled, and deleted. Built-in items may be promoted to editable user copies. If a macro fires unexpectedly, disable its collection, narrow its trigger, or turn on **Don’t expand inside code**.

# Chapter 24: Build reusable templates with Super Tab

Fields turn a static expansion into a guided form. A field may have a placeholder, a default, or a list of choices.

1. Create a macro for a repeated structure.
2. Add fields in the expansion, or use **Insert ▸ Field** while building source.
3. Expand the macro.
4. Type into the selected first field.
5. Use **Next Field** to advance and **Previous Field** to go back.
6. For a choice field, select from the field-choice list.

Design fields in the order a person naturally answers them. Put the final caret at the place where free writing should continue. Keep defaults harmless: a field forgotten by the user should be obvious in Preview, not silently publish misleading content.

---

# Part VII — Math, diagrams, charts, and images

# Chapter 25: Write equations, diagrams, and charts

Pilcrow includes offline rendering for MathJax equations, Mermaid diagrams, and Vega-Lite charts. The active profile still determines where the block begins and ends; the bundled library only draws its contents.

## Start from a template

1. Choose **Insert ▸ Equations**, **Diagrams**, or **Charts**.
2. Pick a template.
3. Replace the sample source.
4. Switch to Preview or Side by Side.
5. Correct any reported syntax error in the source block.

Use MathJax for mathematical notation, Mermaid for flows and relationships, and Vega-Lite for data-driven charts. Keep a textual explanation near any important visual so the document remains understandable when a renderer is unavailable and accessible to more readers.

The libraries are bundled and run without network access. Settings ▸ Library ▸ Rendering Libraries shows versions and notices. If a block does not render, confirm its language label, delimiters, optional-feature settings, and syntax before changing themes.

# Chapter 26: Manage image insertion and online-image privacy

Open **Settings ▸ Editing ▸ Images** and decide:

- Whether an inserted image is copied, moved, or left where it is.
- Whether the rule applies to local and online images.
- Whether online images may load.
- Whether paths should be relative when possible.
- Whether relative paths start with `./`.
- Whether URLs are escaped on insertion.

For a portable project, keep images inside the document folder and use relative paths. Copying is safer than moving when the original belongs to another project. Moving avoids duplicates but can break the source location.

Online images reveal the viewer’s network address to their hosts and can change or disappear. Leave network loading off when reviewing untrusted documents. For durable publication, download an authorized copy and reference it locally.

---

# Part VIII — Publish and share

# Chapter 27: Export HTML, PDF, Word, and images

1. Save the document and inspect Preview.
2. Choose Export from the toolbar or File commands.
3. Choose HTML, HTML (without Styles), PDF, Word, Image, or PDF Archive.
4. Choose the Render Theme under **Style**.
5. For PDF, PDF Archive and Word, review the **Page** options: paper size, orientation and margins.
6. Choose **Export** and select a destination, or **Share** to send the generated file directly.

HTML creates a standalone styled page. **HTML (without Styles)** emits clean structure without embedded theme CSS. Word produces a real `.docx` package with semantic document structure; supplemental equations, diagrams, and charts become pictures. **Image** creates one PNG of the rendered document. **PDF Archive** creates a ZIP containing ordered PDF segments plus a manifest, which is useful when another workflow wants bounded, separable segments. A normal large PDF is assembled through a segmented rendering path automatically, while PDF Archive preserves the segments as the deliverable.

Open **Advanced options** to add **Custom CSS** for this export only. Per-export CSS is applied after the theme and therefore wins when selectors have equal weight. Page changes affect only the current export unless you choose **Use these page settings as default**. A generated table of contents, heading numbering and heading labels are set once for every export under **Settings ▸ Table of Contents** (Chapter 70).

If output is wrong, determine whether the issue is structure or style. A missing heading is usually a profile/source problem; an unattractive heading is a Render Theme problem.

## Print the rendered document

Choose **Print…** from File or More. Printing uses the same rendered pipeline and page-layout defaults as PDF, so Preview and PDF export are the right places to diagnose structure and style first. On Mac, Page Setup edits the same shared page layout. Check paper, orientation, margins, headers, and footers in the print dialog before committing physical pages.

# Chapter 28: Set export defaults and page furniture

Open **Settings ▸ Export ▸ Export Defaults**. Choose the default Render Theme and page layout. Configure author metadata, headers, footers, and whether each top-level heading begins on a new page (**Page break between top-level headings**).

Header and footer templates can include `${title}`, `${author}`, `${pageNo}`, `${pageCount}`, and `${today}`. Keep them short enough for the page margins. Test a multi-page PDF because a header that looks fine on one page can collide with long headings or page numbers later. These polish values are stored per output format; page layout is shared by PDF, PDF Archive, Word, and printing.

CommonMark options control optional syntax such as highlight, subscript, superscript, inline math, automatic links, alerts, front matter, diagrams, smart punctuation, and code-fence presentation. Enable only the features your source actually uses. Portable CommonMark documents should not rely on extensions without documenting them.

# Chapter 29: Share source and finished output

Choose **Share…** for the source document when another person needs the editable file. A clean saved document is shared directly. An unsaved or dirty document is shared as a temporary copy of its current text; very large documents may need to be saved first.

Choose **Share** in Export when the recipient needs a finished PDF, Word document, HTML file, or image. This generates the output without requiring you to keep a separate saved export first.

Before sharing source, include dependent local images, linked documents, profiles, or themes when the recipient needs the same behavior. Before sharing finished output, check links, Preview, page breaks, alternative text, and the filename.

---

# Part IX — The assistant

# Chapter 30: Connect an AI provider safely

The Assistant is optional and uses a connection you configure. Pilcrow does not silently choose a provider.

1. Open **Settings ▸ General ▸ Assistant**.
2. Add a preset or choose **Custom…**.
3. Enter a name, base URL, wire format, and model.
4. If the provider requires an API key, enable that option and store the key when prompted. Keys are kept in the system Keychain.
5. Choose **Test Connection**.
6. Save and make the connection active.

Use **Choose Model…** in the Assistant when the provider offers model discovery. If a model disappears, choose a current one rather than repeatedly retrying an obsolete identifier.

Before first use of a connection, Pilcrow shows where text will go and asks for consent. Read the hostname. A local server and a public cloud provider have different privacy consequences even if they expose the same API format.

# Chapter 31: Ask questions with deliberate context

Open the Assistant sidebar and choose the conversational mode. The context chip begins with the smallest useful scope, normally the selection. Choose another scope only when the question requires it.

1. Select the paragraph you want help with.
2. Confirm the chip says Selection and review its summary.
3. Ask a specific question, such as “Which sentence makes the chronology unclear?”
4. Read the reply as advice, not an automatic edit.
5. Apply changes yourself or through an offered reviewed action.

Pilcrow excludes configured patterns and folders from assistant context. Manage them under Assistant settings. Use the folder control to turn assistant access off for a sensitive workspace. Clear the conversation with the trash button when it no longer belongs with the current task.

Never share a whole folder merely because a question mentions one file. Minimum necessary context improves privacy and often answer quality.

# Chapter 32: Get help authoring Pilcrow resources

Switch the Assistant to **Help** and choose Profile, Macro, or Style Guide. Pilcrow includes the relevant format reference with the conversation so follow-up instructions remain grounded.

Describe the desired behavior and provide a small example. Ask for a draft, use Preview to inspect the generated resource text, then validate it in the relevant Settings editor. Do not import or save opaque generated JSON without reading its name, triggers or patterns, and outputs.

A productive sequence is:

1. State one behavior and two examples.
2. Ask for the smallest valid resource.
3. Validate it in Pilcrow.
4. Test one success and one non-match.
5. Return the validation error for a focused correction.

# Chapter 33: Run an AI-assisted style review

This workflow extends Chapter 21:

1. Select a passage for the first trial.
2. Choose Style Review, a guide, variant, and review areas.
3. Confirm the active provider and model.
4. Start the review.
5. Sort findings by severity or area as offered.
6. Open a finding, read its quoted evidence, and inspect the source location.
7. Apply, dismiss, or leave it unresolved.

For a whole document, Pilcrow estimates bytes and request count and asks again before sending. You can stop between chunks. Review sensitive documents locally or with a provider whose handling terms you accept. Delete AI data and keys from Assistant or Storage & Privacy settings when decommissioning a connection.

---

# Part X — Book projects

# Chapter 34: Turn a folder into a book project

For a fresh project, choose **File ▸ New Book…**, enter the title and destination, and let Pilcrow create the initial folder and manifest. To adopt an existing manuscript, open its folder, choose **File ▸ Make Folder a Book Project** or the Project sidebar’s **Make It a Project**, and complete the metadata. Pilcrow creates a `manifest.pilcrow` file describing order and metadata; it does not rearrange manuscript files.

Open Project Settings and enter title, author, target word count, variables, word-count behavior, and syntax. Add existing files that are listed as **Not in the manuscript**, or create new front matter, chapters, scenes, and back matter from the plus menu.

Commit or back up `manifest.pilcrow` with the manuscript. It is the table of contents for project organization even though the source files remain ordinary text.

# Chapter 35: Plan scenes and track manuscript progress

Choose among **List**, **Synopses**, and **Cards**:

- List emphasizes manuscript order and word counts.
- Synopses adds summary, point of view, location, status, and progress.
- Cards provides a visual planning board without changing file order.

Open an item’s details to set its role, status, synopsis, point of view, location, and target words. Filter by status to focus on draft, revision, or completed work. Remove an item from the manuscript without deleting its file when it is research or a cut scene.

Reorder only while no status filter is active; a filtered subset cannot safely represent the complete manuscript order. On iPad, choose **Reorder**, drag, then choose **Done**. Collapse chapters to reduce list noise.

If Pilcrow says the project file changed on disk, reload and repeat the intended action. This conflict protection prevents one device or collaborator from overwriting a newer manifest.

# Chapter 36: Compile a manuscript

1. Open the Project sidebar.
2. Confirm order, included files, and project metadata.
3. Choose **Compile…**.
4. Choose output format, Render Theme, and compile options.
5. Review front matter, chapter breaks, numbering, and included roles.
6. Compile and inspect the result.

Compilation can produce HTML, PDF, or Word. Choose which front matter, parts, chapters, and back matter start on a new page; set the separator between scenes; include a table of contents; number headings; and optionally keep a Version History snapshot of every included file first. The Manuscript summary shows included files, bytes, omitted files, missing paths, and final order. Missing files must be resolved before Compile becomes available.

Save a group of compile choices as a named preset when you publish the same manuscript in several ways—for example, “Editor DOCX” and “Print PDF.” Delete an obsolete preset from the same sheet. While compilation runs, progress shows the file count and **Stop** cancels the operation. Unresolved `{{variables}}` are reported and left visibly unchanged.

Compilation reads the manifest order and combines source logically; it does not concatenate and overwrite your files. Correct a scene in its source file, then compile again. Use project variables for repeated metadata rather than manually duplicating title or author text.

---

# Part XI — Syntax profiles

# Chapter 37: Choose and understand a syntax profile

A profile tells Pilcrow how source marks become structural roles. CommonMark is bundled, but it is one profile, not the app’s definition.

Use the profile control in the status bar or appropriate document control to choose a profile. Pilcrow can infer one from an extension and remember a per-file choice. The active profile controls highlighting, Outline, formatting availability, Preview, export structure, continuation behavior, and profile-specific inserts.

Choose a profile based on the source language already present. Changing profiles does not convert text; it reinterprets it. If you need conversion, create a copy and transform the source explicitly.

# Chapter 38: Create and test a profile

1. Open **Settings ▸ Library ▸ Syntax Profiles**.
2. Duplicate a close built-in or create a new profile.
3. In **Overview**, set name, identifiers, extensions, and optional inheritance.
4. In **Rules**, add the smallest construct you need.
5. Open **Test Sample**, paste representative source, and choose **Check sample**.
6. Save, activate the profile in a disposable document, and compare Edit, Outline, Preview, and export.

Test boundaries: start and end of file, blank lines, nested constructs, Unicode, an unclosed delimiter, and text that should not match. A profile is trustworthy when it rejects near misses as well as recognizes examples.

Use **Set as New Baseline** after a known-good revision. **Reset to Baseline** discards later experiments. Duplicate before a risky redesign.

# Chapter 39: Edit profile rules and advanced JSON

The rule editor exposes pattern type, line-start requirements, produced role, captures, continuation after Return, delimited-block behavior, layout, inline runs and pairs, captions, and styling roles.

Use literal or structured recognizers whenever they express the syntax. Keep patterns bounded and anchored. Pilcrow rejects known unsafe patterns, but a technically accepted expression can still be too broad or confusing.

Choose **Edit Advanced JSON…** only when the visual editor does not expose the needed property. Apply validates the JSON and prevents changing the profile identity through that sheet. Keep a valid test sample alongside advanced work.

Inheritance is useful for a small dialect: inherit a stable parent and replace only named syntax. Avoid a long chain that makes behavior hard to explain. If importing a profile reports a conflict, compare names and IDs before replacing anything.

---

# Part XII — Themes and appearance

# Chapter 40: Understand Application and Render Themes

Pilcrow has two separate theme systems:

- **Application Themes** are JSON and style the app, bars, sidebar, accent, editor colors, and light or dark appearance.
- **Render Themes** are CSS and style Preview, HTML, PDF, and the semantic subset used for Word.

Choose both under **View ▸ Theme** or Settings. There is no independent mode switch that should fight an Application Theme; the theme declares its appearance. CSS does not style the app or source editor.

When the editor looks wrong, change the Application Theme. When Preview or export looks wrong, change the Render Theme. This single distinction solves most theme confusion.

# Chapter 41: Create and manage themes

Open **Settings ▸ Library ▸ Themes**. Choose the Application or Render collection, then duplicate, import, export, edit, or delete a user theme.

For an Application Theme, use the editor to set appearance, accent, chrome, sidebar, bars, and editor colors. Check selection contrast, current-line visibility, links, warnings, and both active and inactive controls.

For a Render Theme, edit CSS against the Pilcrow class API. Start by changing typography and spacing, then headings, lists, code, tables, callouts, links, footnotes, and supplemental blocks. Test the visual specimen in `Examples/Themes/VisualTestPack` if you are working from the project checkout.

Built-ins are stable starting points. Duplicate instead of trying to overwrite one. A ZIP package may contain both theme kinds; file extensions decide where each item belongs.

# Chapter 42: Choose fonts, size, spacing, and backdrops

Use **Settings ▸ Appearance ▸ Text Size & Fonts** for editor and gutter fonts, point size, line spacing, and tab width. These settings affect the writing surface, not exported typography.

Use **Theme & Backdrop** for the Application Theme, zoom, reading speed, and optional images behind the text area or sidebar. Choose, replace, or remove each backdrop separately. Backdrops should preserve contrast and focus; a beautiful image that reduces legibility is a poor editor setting.

Use the Render Theme and Export Defaults for published fonts and page layout. This separation lets you write in a highly legible monospaced editor while publishing in a proportional book face.

---

# Part XIII — Import, export, and manage your library

# Chapter 43: Import and share Pilcrow resources

Pilcrow can import syntax profiles, Application Themes, Render Themes, macro collections, style guides, and ZIP packages containing supported resources.

1. Open the corresponding Library settings page, or the Import page on iOS.
2. Choose Import and select the file.
3. Review the resource type, name, and any conflict.
4. Import, rename, or replace only when you understand the consequence.
5. Activate and test it in a disposable document.

Export user resources from their Library page to share or back them up. Keep related resources in a ZIP when a project needs a profile, themes, macros, and guide together.

Treat imported profiles, macros, CSS, and style guides as code-like configuration. Read triggers, patterns, raw CSS, and assistant instructions before trusting them.

# Chapter 44: Move or restore your library

Open **Settings ▸ Library ▸ Location**. Choose a folder or **Use This Device**. If the destination already contains a library, choose among:

- **Use What Is There** to switch without copying.
- **Move My Library Here** to transfer and remove the old managed copy after success.
- **Copy My Library Here** to keep both.

Use a synchronized folder only when its provider reliably preserves ordinary files and you understand concurrent edits. Let a transfer finish before quitting. If the location becomes unavailable, reconnect the drive or account, or choose another location; do not create conflicting replacement resources blindly.

On iOS, the Import page can restore library content from a package. Verify active themes and profiles after a restore because resource IDs, not just display names, define references.

---

# Part XIV — Settings, privacy, and support

# Chapter 45: Configure General, Files, and Editing settings

Settings are grouped and searchable. Use the search field for a label such as “line numbers,” “image,” or “header.”

## General

Configure window and launch behavior, language, translation, assistant connections, diagnostics, and Storage & Privacy.

## Files

Choose launch folder behavior, default file type, autosave and recovery, versions retained, file-tree behavior, and what happens when importable items are dropped onto the app.

## Editing — Display & Typing

Configure line numbers, status bar, formatting toolbar, wrapping, current-line rule, Styled Source, markers, rendered blocks, heading folding, auto-expansion, bracket and quote pairing, Markdown pairing, emoji shortcodes, list and quote continuation, indentation on Return, spaces for Tab, spelling, and parsing warnings.

## Editing — Typing sounds

Turn on **Play a sound as I type** to hear a sound as you type. Choose a pack (Typewriter, Duck or Kitten), set the volume, and use **Preview** to hear it. Each key kind gets its own sound: lowercase letters, uppercase letters, numbers, symbols, Space, Tab, Return and Delete. Pastes and multi-character edits are silent.

Under **Your own sounds**, choose **Choose…** next to a key kind to use your own audio file for it (WAV, AIFF, MP3, M4A or CAF). The clip can be at most 2 seconds and 3 MB. Pilcrow converts it to a small mono clip, so a long or loud file cannot slow typing or click. Use **Play** to hear it and **Remove** to go back to the pack's sound. If a file is refused, the message says why. On iPad the silent switch mutes typing sounds, and they mix with other audio.

## Editing — Images

Configure insertion, copying or moving, online loading, path style, and URL escaping.

## Appearance

Choose Application Theme, zoom, backdrops, editor size, fonts, line spacing, and tab width.

## Export

Choose Render Theme, layout, headers, footers, metadata, and heading page breaks.

## Library

Manage profiles, CommonMark options, themes, macros, style guides, rendering libraries, location, and imports.

## Keyboard

Search, rebind, unbind, and reset shortcuts, including field-navigation behavior.

Change one cluster at a time. When evaluating typography, keep the theme fixed; when evaluating parsing, keep the profile fixed. Controlled changes make cause and effect visible.

# Chapter 46: Control privacy and stored data

Open **Settings ▸ General ▸ Storage & Privacy**. Pilcrow separates deletion by category so clearing a cache cannot accidentally delete documents.

- **Review Recovery Data…** inventories recoverable content. Save or close dirty documents before deletion.
- **Review Version History…** shows versions and estimated space before deletion.
- **Clear Recent File Access…** removes recent files, remembered folders, session bookmarks, and per-file syntax choices.
- **Delete AI Data & Keys…** removes connections, Keychain keys, the conversation, and AI privacy choices.
- **Delete Diagnostics…** removes recorded logs and crash support data.
- **Clear Caches…** removes recreatable caches and network responses.

Custom profiles, themes, macros, style guides, and backdrops remain on their visible Library pages and must be reviewed there. These controls do not delete your documents.

Assistant settings also manage excluded file patterns, folders where the assistant is turned off, and AI-data deletion. Online-image loading is a separate privacy choice. Link checking never visits the network.

# Chapter 47: Record and send diagnostics

Open **Settings ▸ General ▸ Diagnostics**. For an intermittent problem, choose **Reproduce an issue**, select relevant parts, level, retention, and included support information. Options include device/system information, Pilcrow settings, speed and memory, recent-action breadcrumbs, and crash details.

Reproduce the problem promptly, then choose **View Log…**. Filter by subsystem and severity. Before sending, inspect the report. Choose **Help ▸ Report a Bug…** to open the bug report form on GitHub with your versions filled in, and let Pilcrow copy the log to your clipboard to paste into it. You can also save the report as a file to attach, share it, or choose **Report on GitHub…** from the log viewer. Reports on GitHub are public.

Diagnostics should record lengths, identifiers, states, and errors—not document content—but always review a report before sharing. Return recording to **Problems only** or disable detailed retention after the issue is captured; verbose logging can consume storage and affect performance.

# Chapter 48: Use Pilcrow in another language

Open Settings and choose Language. A restart may be required. Pilcrow provides English plus Spanish, French, German, Italian, Brazilian Portuguese, Dutch, Russian, Japanese, Korean, and Simplified Chinese.

Non-English interface translations are AI-generated until marked human-reviewed. Pilcrow shows a startup notice in those languages. Choose **Don’t show this again** to dismiss it permanently, or re-enable the notice in Language settings. The label “Machine-translated — may contain errors” identifies unreviewed content.

Changing the interface language does not translate documents. Use the Translation commands for document text. If a command is ambiguous in translation, switch temporarily to English to see the authoritative original wording.

---

# Part XV — Reference and troubleshooting

# Chapter 49: Command and shortcut reference

These are the principal default shortcuts. User-remappable commands can differ after Settings changes.

| Task | Default |
| --- | --- |
| New document | `⌘N` |
| Open file | `⌘O` |
| Open Quickly in folder | `⇧⌘O` |
| Save | `⌘S` |
| Save As | `⌥⇧⌘S` |
| Close | `⌘W` |
| Close all | `⇧⌘W` |
| Undo / Redo | `⌘Z` / `⇧⌘Z` |
| Find / next / previous | `⌘F` / `⌘G` / `⇧⌘G` |
| Go to line | `⌃G` |
| Copy as Markdown | `⇧⌘C` |
| Paste as plain text | `⇧⌘V` |
| Select word | `⌘D` |
| Select line | `⌘L` |
| Select paragraph | `⌥⌘P` |
| Jump to top / bottom | `⌘↑` / `⌘↓` |
| Line start / end | `⌃A` / `⌃E` |
| Move row up / down | `⌥⌘↑` / `⌥⌘↓` |
| Strong / emphasis | `⌘B` / `⌘I` |
| Insert table | `⌥⌘T` |
| Insert image | `⇧⌘I` |
| Preview | `⇧⌘P` |
| Side by Side | `⌃⌘P` |
| Actual size | `⇧⌘0` |
| Zoom in / out | `⇧⌘=` / `⇧⌘-` |
| Line numbers | `⌥⌘L` |
| Next / previous document | `⌃Tab` / `⌃⇧Tab` |
| Pilcrow Help | `⌘?` |

The command palette, sidebar panels, focus mode, multi-caret commands, document switcher, and field navigation may use customizable bindings shown beside their menu items.

# Chapter 50: Troubleshoot common problems

## The file is garbled

Check the encoding in the status bar. Reopen or convert with the correct encoding before editing.

## Formatting or Preview is wrong

Confirm the active profile, validate source delimiters, enable required optional syntax, then confirm the Render Theme. Use Edit with markers visible to inspect literal text.

## A formatting or Insert command is disabled

Switch from Preview to Edit. Then confirm a document and syntax profile are active and that the profile supports the requested construct.

## A diagram, chart, or equation does not render

Check the fenced language label, block boundaries, source syntax, and diagrams/math option. Start from a bundled template to isolate the error.

## Find misses visible Preview text

Search in Edit for text split by formatting or contained in code, equations, diagrams, or charts. Preview search intentionally covers readable rendered text, not every source node.

## A relative image or link is broken

Save the document so it has a folder, verify exact filename and case, prefer a relative path inside the project, and run Check Links.

## A folder replacement skipped files

Close those files in Pilcrow, ensure they are UTF-8 text, rerun the preview, and verify they did not change externally between preview and commit.

## A macro does not fire—or fires too often

Confirm its collection and macro are enabled, check the match type and trigger boundary, test outside code, and narrow a broad pattern.

## Translation is unavailable

Confirm macOS 15 or iOS 18 or later, installed language support, and a supported source/target pair. Document translation is distinct from interface language.

## The Assistant is unavailable

Add and test a connection, make it active, choose an offered model, acknowledge the provider, and ensure the folder or file is not excluded.

## A huge-file action is slow

Wait for background line indexing, use targeted search, and avoid PDF or whole-document transformations when a streamed HTML/Word workflow meets the need.

## Pilcrow reports an unexpected quit or out-of-sync editor

Stop editing, save a copy if possible, use recovery when offered, and record diagnostics before relaunching. Do not discard the recovery set until you verify the saved document.

## The project panel reports a manifest conflict

Reload, inspect the latest project state, and repeat the change. Do not overwrite `manifest.pilcrow` from two devices simultaneously.

## A custom resource will not import

Confirm the expected extension and JSON/CSS format, inspect the reported unsafe pattern or conflict, and import into the correct Application Theme, Render Theme, profile, macro, or style-guide section.

# Chapter 51: Adopt a dependable working routine

Use this routine for ordinary work:

1. Open the folder, not only an isolated file, when the document has related assets.
2. Confirm the profile and encoding before substantial editing.
3. Save an initial checkpoint.
4. Write in Edit; use Side by Side when structure matters.
5. Use macros and fields for repetition, not manual duplication.
6. Save before bulk replacement, comparison acceptance, translation replacement, or profile experiments.
7. Run spelling, style review, and Check Links at appropriate stages.
8. Unfold all sections and inspect Preview from beginning to end.
9. Export with the intended Render Theme and inspect the actual target format.
10. Share source only when the recipient needs to edit; otherwise share finished output.
11. Keep profiles, themes, macros, style guides, project manifests, and local assets with the project backup.
12. Review recovery, versions, AI data, diagnostics, and caches periodically under Storage & Privacy.

The reasoning is simple: make meaning explicit in source, keep presentation in themes, checkpoint before transactions, share the least necessary data, and validate the exact artifact another person will receive. That is the Pilcrow way to keep plain text both powerful and dependable.
