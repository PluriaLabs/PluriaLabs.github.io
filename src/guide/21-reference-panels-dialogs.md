
---

# Part XVII — Panels, bars and dialogs

# Chapter 59: The document title and the document switcher

The document's name sits in the header with a small coloured dot and a down arrow. Click it, or choose **View ▸ Open Documents** (`⌃⌘2`), to open the **Open Documents** list. On a small screen it opens as a sheet with a **Done** button.

## The save dot

The dot beside the name tells you the state of the document at a glance. The state is also read aloud by VoiceOver.

| Dot | Meaning |
| --- | --- |
| Green | **Saved.** The file on disk matches what you see. |
| Amber | **Edited.** You have changes that are not saved yet. |
| Red | **Save failed.** Pilcrow tried to save and could not. A **Couldn't save** banner with a **Retry** button appears over the editor. |
| Blue | **Changed by another app.** The file on disk was changed from outside Pilcrow. |

A document that has never been saved shows "Not yet saved" and a number in the list, since it has no folder to show. A document with unsaved changes also says **Edited** at the end of its row.

## The Open Documents list

| Part | What it does |
| --- | --- |
| **Search Open Documents** | Appears when seven or more documents are open. Type part of a name or folder; each word must match somewhere in the name or the folder, ignoring case and accents. Return opens the first match. When nothing matches it says "No open documents match." |
| A row for each document | Shows the name, its save dot, and the folder it lives in. A checkmark marks the active document. Click a row to switch to it. |
| **Close** (the **x** at the end of a row) | Closes that document, asking first if it has unsaved changes. |
| **New Document** | Creates an untitled document. |
| **Save** | Saves the active document. |
| **Save As…** | Saves to a new name or place. |
| **Rename…** | Opens the rename form (below). |
| **Close All Documents** | Closes every document, asking about each unsaved one. |

Use `⌃Tab` and `⌃⇧Tab` to move to the next or previous document without opening the list.

## Rename

**Rename…** shows the current **Name** and **Where** the file lives, with **Cancel** and **Rename** buttons. Renaming changes the file on disk and keeps the document open. If the new name cannot be used, a **Could Not Rename Document** message explains why.

# Chapter 60: The sidebar

The sidebar holds five panels: **Files**, **Outline**, **Search**, **Project** and **Assistant**. A switch at the top of the sidebar chooses **Files**, **Outline**, **Project** (shown when the open folder is a book project) or **Assistant** (shown once a connection is set up). **Search** has its own header with the title **Find**, a **Done** button that returns to Files, and a scope control for **This Document** or **Folder**; reach it from **View ▸ Search** (`⇧⌘F`). The **View** menu also switches panels, and choosing the panel that is already showing hides the sidebar. Drag the sidebar's edge to resize it. Above the file tree, a menu offers **Open File…** and **Open Folder…**.

## Files

The Files panel is a tree of the open folder.

With no folder open, it says "Choose a folder to browse its files." and offers **Open Folder** and **Open File**. You can also drop a folder onto it. When you opened a single file whose folder Pilcrow cannot see, it offers "Browse *folder* to see the files beside this document", with **Browse Enclosing Folder…**.

Click a file to open it. Folders expand and collapse. Right-click a row, or press and hold on iPad, for its menu:

| Item | What it does |
| --- | --- |
| **New File** | Creates a file in the folder (or beside the file you clicked). |
| **New Folder** | Creates a folder there. |
| **Rename…** | Renames the file or folder. |
| **Move to Trash** | Moves it to the Trash after you confirm. You can put it back from there. |
| **Reveal in Finder** | Shows it in Finder (Mac). |

Where the system has no Trash for a location, Pilcrow keeps deleted items in a **Recently Deleted** section at the bottom of the panel. Each item there offers **Put Back** and **Delete Permanently**, and **Empty Recently Deleted** removes the whole section's items for good. Deleting permanently cannot be undone, so Pilcrow asks first. Items you deleted from other places are not affected.

Hidden files and folders are shown or hidden by **Settings ▸ Files ▸ Show hidden folders and files**.

## Outline

The Outline lists the headings of the active document, indented by level. Click a heading to jump to it. A chevron beside a heading collapses or expands the headings nested under it. This does not change the document, and the collapsed state is not saved.

States you may see:

| Message | Meaning |
| --- | --- |
| **No headings** | The active profile found no headings. |
| **Indexing outline… N%** | A large document is still being scanned. |
| **Outline indexing failed. The listing may be incomplete.** | Scanning hit a problem. |
| **N headings near your position — scroll to see others.** | A very large document shows a window of its outline around the caret. |

Under the outline, a **Fields** section appears when the document has fill-in fields (Chapter 24). It lists them, with a count; click one to scroll to it and select it. For a very large number of fields it says "Only the first fields are listed."

## Search

The Search panel searches every file in the open folder. Without a folder it says "Open a folder to search it." with an **Open Folder…** button.

| Control | What it does |
| --- | --- |
| **Search Folder** field | Type to search as you go. A **clear** button empties it. |
| **Aa** | **Match case.** |
| **ab** | **Whole word.** |
| **.\*** | **Regular expression.** A bad pattern is reported under the field. |
| Status line | Shows "Searching…" with a **Cancel** button, then "Matches: N". A search stops at 500 matches and says "Showing the first 500 matches." After a cancel it offers **Search Again**. |
| **Replace…** | Appears when the search finds matches. Opens Replace in Folder (Chapter 63). |
| Results | Each result names the file and shows the line. Click one to open the file at that line. |

## Project

The Project panel is for book projects. See Chapter 34, Chapter 35 and the Project panel reference below.

### Project panel reference

| Part | What it does |
| --- | --- |
| **This folder is not a book project.** with **Make It a Project** | Shown when the open folder has no manifest. |
| **Try Again** | Shown if the project could not be read. |
| **View** | Chooses **List**, **Synopses** or **Cards**. |
| Title, word totals | The project name and "N words", or "N of target" when a book word target is set. |
| **Status** filter | Filters to one status, or **All statuses**. A tally lists each status with its file and word counts. Reordering is available only while no filter is active. |
| **Project Settings** (gear) | Opens the settings sheet below. |
| **Compile…** | Opens the compile sheet (Chapter 64). |
| **Reorder** and **Done** | On iPad, drag chapters into a new order, then choose **Done**. |
| **New File** (plus) | Offers **New Chapter**, **New Scene**, **New Front Matter**, **New Back Matter**. |
| **Not in the manuscript** with **Add** and **Add All** | Lists files in the folder that the manifest does not include. |
| A row's chevron | **Show Scenes** or **Hide Scenes** under a chapter. |
| **Missing** and **Left out** tags | A file that cannot be found, or that you have left out of the manuscript. |
| A row's menu | **Details…**, **New File Below**, **Move Chapter Up**, **Move Chapter Down**, **Include in Manuscript**, **Leave Out of Manuscript**. |
| **Word target** per item | Each item shows its words and any target. |

**Details** for an item has **Kind** (Front matter, Part, Chapter, Scene, Back matter), **Status**, **Point of view**, **Location**, **Word target**, and **Synopsis**. A project file changed on disk shows "The project file changed on disk, so your last change was not applied. Try it again." with **Dismiss**.

**Project Settings** has **Title**, **Author**, **Book word target**, **New files are written in** (the syntax for new chapters and scenes; existing files keep theirs), **Variables** (a name and a value, written as `{{name}}` in your text; `{{title}}` and `{{author}}` always work), and **What counts as a word**: **Count headings**, **Count front matter**, **Count code blocks**. Choose **Save** or **Cancel**.

## Assistant

The Assistant panel appears once a connection is set up (Chapter 65).

# Chapter 61: The formatting toolbar and the status bar

## The formatting toolbar

The formatting toolbar is an optional row under the text. Show or hide it with **View ▸ Formatting Toolbar**, **More ▸ Formatting Toolbar**, **Settings ▸ Editing ▸ Formatting Toolbar**, or the toolbar's own **Hide Toolbar** item. It acts through the active profile, so a button the profile cannot express is greyed out.

| Control | What it does |
| --- | --- |
| **Paragraph type** menu (for example "Paragraph" or "Heading 1") | Shows the type of the current line and changes it: **Paragraph**, **Heading 1** to **6**, **Blockquote**, **Bulleted List**, **Numbered List**, **Task List**, **Code Fence**. |
| **Bold** (`⌘B`) | Strong. |
| **Italic** (`⌘I`) | Emphasis. |
| **Inline code** | Code. |
| **Insert link** (`⌘K`) | Makes a link. |
| **Blockquote** | Toggles a quote. |
| **Bulleted list** | Toggles a bullet list. |
| **More formatting** (**⋯**) | The rarer commands: **Strikethrough**, **Insert Inline Math**, **Insert Task List**, **Toggle Task Status**, **Indent**, **Outdent**, **Increase Heading Level**, **Decrease Heading Level**, **Insert Table…**, **Insert Image…**, **Insert Diagram**, **Insert Chart**, **Insert Display Math**, **Insert Code Fence**, **Insert Alert**, **Insert Horizontal Line**, **Insert Link Reference**, **Insert Footnote**, **Insert Table of Contents**, **Insert YAML Front Matter**, and **Hide Toolbar**. |

## The status bar

The status bar runs along the bottom. Turn it on or off with **Settings ▸ Editing ▸ Show status bar**.

| Part | What it shows or does |
| --- | --- |
| **Words**, **Ln**, **Col** | The word count, and the line and column of the caret. With a selection, it adds "Sel: N ln · N ch" for the selected lines and characters. |
| **Syntax** menu (for example "CommonMark") | The profile for this document. Click to choose another, or **No Syntax** for plain text. |
| **Fields left: N** | Shown when a macro left fill-in fields. Click it to jump to the next field. |
| Progress and status | **Indexing N%**, **Lexing N%** while a large file is analysed, and **Translating N%** with **About N left** and a **Cancel translation** button while a translation runs. |
| **Out of sync** | A warning that the editor and the document's change log have diverged. Saving keeps the file marked unsaved so nothing is lost: copy your text somewhere safe, then close and reopen the document. |
| Document information | Click the counts, or the tooltip "Show document information", to open **Document Information**. |

**Document Information** lists **Words**, **Characters**, **Lines**, **Reading time** (based on your reading speed in Settings), **Cursor**, **Selection**, **Encoding** and **Syntax**. In a very large file the counts are for the loaded part until indexing finishes, and the reading time is estimated for the whole file. **Convert To…** under **Encoding** chooses another text encoding; the file is converted when it is next saved.


# Chapter 62: Find, replace, Go to Line, Open Quickly and the command palette

## The find bar

Open it with **Find…** (`⌘F`), the **Find** button, or **Replace…** (`⌘R`). It sits at the top of the document.

| Control | What it does |
| --- | --- |
| **Find in document** field | Type the text to find. Matches are highlighted as you type. |
| **Aa**, **ab**, **.\*** | **Match case**, **Whole word**, **Regular expression**. |
| **Previous match**, **Next match** | Step through the matches (`⇧⌘G`, `⌘G`). |
| **Show replace** / **Hide replace** (chevron) | Shows the **Replace with** field. |
| **Replace**, **Replace All** | Replaces the current match, or every match. Greyed out until there is a match. |
| **Find In** (a switch at the left end of the bar) | **This Document**, or **Folder** to search the whole open folder instead. |
| **Close find bar** | Closes it. |

When there are more matches than Pilcrow counts, the bar says "More matches remain". In **Preview**, Find looks through the rendered words and highlights them, up to 2,000 matches. A pattern that cannot be used says "Invalid pattern". Replace is available only in Edit: in Preview the bar says "Replace works in Edit. Switch to Edit to change the text." In **Side by Side**, Find searches the source and highlights the matching words in the preview.

## Go to Line

**Go to Line…** (`⌃G`) opens a small sheet with one field, "Line number, or line:column". Type `120` or `120:8` and choose **Go**, or **Cancel**. A number past the end goes to the last line. Pilcrow says "Enter a line number, such as 120 or 120:8." for anything else. In a very large file whose lines are still being counted, it asks you to try again in a moment.

## Open Quickly

**Open Quickly…** (`⇧⌘O`) is a filename search across the open folder. Type part of a name, and the list narrows and shows "N matches". Choose a result and **Open**, or **Cancel**. It is greyed out without an open folder.

## The command palette

**Command Palette…** (`⌃⇧P`) lists Pilcrow's commands by name, with their shortcuts, so you can run one without finding its menu. Type to narrow the list, choose a command and **Run**, or **Cancel**. It shows "No matching commands" when nothing fits. A command that cannot run right now, such as a source edit while you are in Preview, is shown greyed out. The list includes the formatting and insert commands, the Edit commands for selection, lines and case, speech, the View switches, zoom, and the sidebar panels, and the file and export actions. The shortcut for opening the palette can be changed in **Settings ▸ Keyboard**.

# Chapter 63: Dialogs and prompts

This chapter describes the sheets and alerts that appear while you work.

## Insert Table

**Format ▸ Paragraph ▸ Table ▸ Insert Table…** (`⌥⌘T`), or **Insert ▸ Table…**, asks for **Columns** and **Rows**. Choose **OK** or **Cancel**. The table is written in the active profile's table syntax.

## Carets in a Column

**Edit ▸ Selection ▸ Carets in a Column…** (`⌃⇧G`) places carets by number, for an iPad without a keyboard. Enter **Lines** (for example `3-17`) and **Column** (for example `100`, or `100-105` to select those characters on each line), then choose **Place**. Then type, delete, copy or paste. A line too short to reach the column follows **Settings ▸ Editing ▸ Short lines in column mode**. While a column selection is active, a **Column Selection** badge appears, with a button to **Turn off Column Selection**.

## Edit Block

With **Rendered Blocks** on, each table, equation or diagram drawn as a picture has an edit button. It opens **Edit Block**, a sheet with the block's source. Choose **Apply** to put your change back, or **Cancel**.

## Check Links

**Edit ▸ Check Links…** checks every link and image in the document. A document must be saved first to check its links to other files: "Save the document to check its links to other files." The sheet shows "Checking links…", then a list of problems, each with its line number, or "All links work." The summary reads "Links checked: N. Web addresses not contacted: N." Pilcrow does not contact web addresses. It checks up to 50,000 links. Choose **Check Again** or **Done**.

## Replace in Folder

**Replace…** in the Search panel opens a preview of every change before any file is touched.

- The **Replace with** field holds the replacement. The sheet lists each file that would change, with a count and a before and after sample for each match, and a checkbox so you can leave a file out.
- **Replace N matches in M files** makes the changes. **Cancel** stops.
- A **Skipped** list names files Pilcrow will not change, with the reason: "Open in an editor. Replace there, or close it first.", "Not plain UTF-8 text.", "Too many matches in one file.", "A line is too long for this pattern.", or "Could not be read."
- One replace changes at most 2,000 files. Beyond that it says "More files match than one replace changes. Replace these first, then search again."
- A file that changed since the preview is left unchanged.
- When it finishes: "Replaced N matches in M files." with **Undo** and **Done**. **Undo** restores the files from a backup. Files edited since, or gone, are left as they are and listed. The next time you open the sheet it offers to undo the last replace.

## Version History

**File ▸ Version History…** lists the saved versions of a document. A version is kept each time you save, up to the number set in **Settings ▸ Files ▸ Versions to keep**. It says "Save the document to start keeping versions." for an unsaved document, "Version history is off." when that setting is none, and "No versions yet." before the first save.

Select a version, then:

| Button | What it does |
| --- | --- |
| **Open Copy** | Opens the old version as a separate document. |
| **Compare…** | Opens the comparison sheet with that version. |
| **Restore…** | Puts the document back as it was then, after you confirm. The current text is kept as a version, so you can go back. Restore needs your changes saved or reverted first. |
| **Done** | Closes the sheet. |

## Compare Versions

**File ▸ Compare with File…**, or **Compare…** in Version History, opens **Compare Versions**.

- Two pickers, **Older** and **Newer**, choose what to compare. **Compare with File…** chooses a file.
- **Ignore trailing whitespace** hides differences that are only spaces at line ends.
- The summary reads "Added: N. Removed: N." and lists the changed lines, up to 5,000.
- For each change: **Accept** makes the change in the open document, **Reject** leaves it out, **Reconsider** undoes your choice, and **Take Back** (when the older version is on the old side) puts the older lines back for that change only. **Accept All Remaining** accepts everything left.
- A change is applied only if its text still matches. Otherwise it says "Nothing was changed: that part of the document has changed since the comparison."
- Messages: "The two are the same.", "Could not compare these.", and, when there are too many differences, "They differ in too many lines to compare line by line. Open a copy of the version and read it beside the document."

## Translate

**Edit ▸ Translate ▸ Document** or **Selection** opens **Translate Document** or **Translate Selection**.

| Control | What it does |
| --- | --- |
| **Detected language** | The language Pilcrow found in the text. |
| **Translate to** | The target language. |
| **Speed** | **Fast** (about twenty times quicker, with plainer wording, and what a long document needs), **Best quality** (for text you will read closely), or **AI assistant** (your own AI connection from Settings ▸ Assistant; the text goes wherever that points). **Best quality** applies from macOS and iPadOS 26.4; earlier systems have one speed. |
| **When finished** | For a document: **Open in a new tab** (a new document named like the original with the language in brackets), **Save a copy beside the original**, or **Replace the document**. For a selection, **Replace Selection** puts the translation in place. |
| **Translate** or **Send and Translate** | Starts. Send and Translate appears when the AI assistant will send your text; it names the provider and warns that your service may charge for it. |
| **Estimated time** | An estimate: "less than a minute", or "about N". The time depends on your AI service. |

Translation runs in the background, with progress in the status bar. A language pack downloads the first time you translate into a language. If there is no direct translation between two languages, Pilcrow asks whether to translate through English (**Yes** or **No**). Code, links and math are left as they were. Translation needs macOS 15 or iPadOS 18 or later. The assistant is not used if it is turned off for the file or folder.

When you open a file written in another language, a bar may ask "This looks like *Language*. Translate it into *Language*?" with **Translate**, **Not Now** and **Never for This File**. Settings ▸ General ▸ Translation controls it (Chapter 67).

## Saving and closing

- **Keep this document?** When you close a new document, Pilcrow asks "Do you want to keep this new document?" For an existing one, it asks "Do you want to save the changes you made?" The choices are **Save**, **Cancel** and **Delete** (or **Don't Save**). For a new document, the form has **Save As:** (the name), **Tags:** and **Where:** (with **Other…** or **Choose…** for a different folder). You can't undo Delete.
- **Save Document** is the form for the first save, with **Name** and **Location** (**Choose Another Location…**). If a file of that name exists, it asks **Replace Existing File?**.
- **File Changed on Disk** appears when another app modified the open file: choose **Reload** or **Keep Current Version**.
- **Reload from Disk?** (File ▸ Reload from Disk) offers **Save, Then Reload**, **Reload Without Saving** and **Cancel**.
- **Fill-in fields remain** appears when you print or export while fields are still unfilled. It offers **Go to Next Field**, **Continue Anyway** (the fields appear in the output as written) and **Cancel**.
- **Parsing warning**, **Could Not Share**, **Could Not Save Document** and **File Operation Failed** show a message with **OK**.
- If Pilcrow quit unexpectedly last time, a banner says so and offers **Open Diagnostics** or **Not Now**.
- After importing a library item, a small toast confirms it, with a button to dismiss it.
- With a translated app language, the first launch shows **Translated with AI**, explaining the translation has not been reviewed by a native speaker, with **Don't show this again** and **OK**.

## The assistant's permission sheet

Before the first content goes to an online service, **Send to *service*?** explains what is sent (your request, the document text counted above the question box or the text being reviewed with the style guide's rules, the model's name, and your key), who receives it, and how to take it back. A program on this computer never leaves the computer; another computer on your network is not encrypted unless its address starts with https; an online service may keep the text under its own terms. There are links to the service's privacy policy and to Pilcrow's. Choose **Send** or **Cancel**. Nothing is sent until you choose Send.

# Chapter 64: Export and Compile

## The export panel

Open it with **File ▸ Export…** (`⇧⌘E`), the **Export** button, or **More ▸ Export…**. It has a list of formats on the left, options on the right, and buttons along the bottom.

### Formats

| Format | File | Notes |
| --- | --- | --- |
| **HTML** | `.html` | A standalone styled page. |
| **HTML (without Styles)** | `.html` | Clean structure with no theme CSS. |
| **PDF** | `.pdf` | Paginated. |
| **Word (.docx)** | `.docx` | A real Word package. It uses the theme's colours, fonts, size and line spacing; browser layout selectors have no Word equivalent. Equations, diagrams and charts become pictures. |
| **Image** | `.png` | One image of the rendered document. |
| **PDF Archive (.zip)** | `.zip` | Ordered PDF segments plus a manifest, for very large documents. |

### Options

| Section | Controls |
| --- | --- |
| **Style** | **Theme** chooses the Render Theme. The theme controls the exported document's typography and colours. |
| **Page** (PDF, PDF Archive and Word) | **Paper size** (A3, A4, A5, Letter, Legal, Tabloid, or a custom **Width** and **Height**), **Orientation** (**Portrait** or **Landscape**), and **Top margin**, **Bottom margin**, **Left margin** and **Right margin**, all in millimetres (25.4 mm, one inch, to start with). **Use these page settings as default** saves them for later exports; it is greyed out until you change something. Otherwise they apply to this export only. |
| **Advanced options** | **Custom CSS**, applied after the theme for this export only. |

The panel says "Save as *name*" with the file name it will use, and "These choices apply to this export only." Choosing a format shows what it makes, in a line at the bottom left: for example "A standalone web page with the selected style." for HTML, or "One paginated PDF document." for PDF.

### Buttons

**Cancel** closes the panel. **Share…** sends the generated file straight to the system share sheet. **Export** asks where to save it. While it works, the panel shows "Rendering…". If something goes wrong, it says "Export failed." If fill-in fields remain, Pilcrow asks first (Chapter 63).

Page settings, header and footer templates, the table of contents and numbering options that apply to every export live in **Settings ▸ Contents & Labels** and **Settings ▸ Export** (Chapter 70).

## The compile sheet

**File ▸ Compile Manuscript…** (or **Compile…** in the Project panel) combines a book project's files in manifest order. It is available once a project is loaded.

| Section | Controls |
| --- | --- |
| **Manuscript** | A summary: "N files", "N left out", and any "Cannot be found" paths, which must be fixed before compiling. An **Order** list shows the final sequence. |
| **Output** | **Format**, then **Start on a new page**: **Front matter**, **Parts**, **Chapters**, **Back matter**. **Between scenes** sets the separator ("None" or a mark). **Table of contents**, **Number headings**, and **Keep a version of each file first** (saves a Version History entry for every included file). |
| **Preset** | **Saved** presets. **Save as preset** with a **Preset name** and **Save**. **Delete Preset** removes the chosen one. |

Choose **Compile…** to pick where to save, or **Cancel**. While it runs it shows "Reading N of N…" then "Compiling…", with **Stop**. Variables with no value are listed ("These {{variables}} have no value and were left as written") and left visibly unchanged. If the file cannot be created, it says "The book could not be created there."

### New Book

**File ▸ New Book…** asks for **Title**, **Author**, **Write in** (the syntax for the chapters), and **Keep it in** (a folder, with **Choose…**). Choose **Create**. Pilcrow makes the folder with a manifest and a first chapter. If the book cannot be created there, it says so.

# Chapter 65: The Assistant panel and style review

The Assistant panel appears after a connection is set up in **Settings ▸ Assistant** (Chapter 67). While no connection is ready, the **Assistant** item is not in the View menu.

## The panel

| Control | What it does |
| --- | --- |
| **Assistant mode** | **Conversational**, **Style Review**, or **Help**. |
| **Choose Model…** | Opens the model chooser (below). Shows warnings when the model is no longer available or is deprecated, with the retirement date. |
| **Clear Conversation** | Empties the conversation. Conversations are not saved; they are discarded when the app quits. |
| **What to share** | Chooses what goes with your question: **Nothing from the document**, **Selection**, **Section**, **Around cursor**, **Whole document**, **Outline**, or **Profile**. A choice that cannot apply says why ("Select some text first.", "This document has no headings.", "Too large to send whole.", "No syntax profile."). A line above the question box says how much will be sent, to which host. The choice is remembered. |
| **Preview** (and **What is sent**) | Shows exactly what will be sent. |
| **Ask the assistant…** / **Describe what you want to write** | The question box. In **Help** mode, **What to write** chooses **A syntax profile**, **A macro** or **A style guide**. |
| **Send** and **Stop** | Sends the request, or stops a reply in progress. |
| **Privacy** | Shows whether the assistant is on for this folder. **Turn Off for This Folder** and **Turn On for This Folder** switch it. "This file is excluded from the assistant." appears for a file that matches an exclusion. |
| Each reply | **Copy**, **Insert at Cursor**, **Retry**, and for a style or macro reply, **Add to Library…**. A reply with an error offers **Ask to Fix**. A cut-short reply says so. |

## Choose a model

**Choose Model…** lists the models the connection offers, with **Search models**. **Show all models** includes the less common ones. A deprecated model is marked with its retirement date. If none are listed, type the model's name instead. **Retry** reloads the list.

## Style review

In **Style Review** mode, the panel runs a style guide over your writing.

| Control | What it does |
| --- | --- |
| **Style guide**, **Variant** | Choose a guide and one of its variants. |
| **What to review** | **Selection** or **Document**. A document too large to review whole says "Too large to review whole. Review a section instead." |
| **Areas** | Choose which areas to check, or **All areas**. |
| **Review** | Sends the text and the rules to your AI connection. Before a whole-document review, an alert says how many requests will be sent and about how much text, and asks **Review** or **Cancel**. |
| **Check Here** | Runs the guide's own checks on this device. Nothing is sent. |
| **Check Cross-References** | Sends the headings, citing lines and reference lists to check rules that compare one part of the document with another. |
| **Stop** | Stops a review in progress. **Review Remaining** continues after a stop or failure. |

Findings appear in a list. Each shows the quote, an explanation and, when there is one, a suggested fix.

| Button | What it does |
| --- | --- |
| **Jump to** | Moves to the finding in the document. A quote that occurs more than once says "Match N of N". |
| **Apply** | Makes the suggested fix. It is applied only if the text is still exactly as it was found. Otherwise it says "The text has changed." or "Not found in the text." |
| **Dismiss** | Removes the finding. |
| **Apply All** | Makes every fix that has one, after a confirmation that says how many, as one change you can undo in one step. It also says how many fixes came from the AI. |
| **Dismiss All Suggestions**, **Clear** | Clear the list. |

The panel also reports "N rules can only be judged by a review", "N rules stopped after 100 findings", and "A suggested change was left out because it added facts the text does not have."
