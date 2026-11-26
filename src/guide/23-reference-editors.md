
---

# Part XIX — Editors for library items

# Chapter 74: The profile editor and profile building blocks

A syntax profile tells Pilcrow what your markup means. This chapter describes the profile editor control by control, and then lists every building block a profile can use. For a task-based introduction, see Chapter 37 to Chapter 39.

Open the editor from **Settings ▸ Library ▸ Syntax Profiles**: **New** starts a profile, **Edit** changes a custom one, and **Duplicate** copies a built-in profile so you can change the copy. The editor's title is **Edit Profile**, with **Cancel**, **Save** and **Profile Help** (which opens the in-app reference to these building blocks). On a narrow screen, a **Profile section** switch chooses between **Overview**, **Rules** and **Test Sample**; on a wide one all three show at once.

## Overview

| Field | What it does |
| --- | --- |
| **Name** | The profile's name, shown in the status bar menu and Settings. |
| **Description** | A note about the profile. |
| **File extensions (comma-separated)** | The extensions that choose this profile for a file. Two profiles cannot share an extension. |
| **Inherits** | **None**, or another profile whose rules this one builds on. |
| **Syntax** | **Extends Markdown** or **Replaces Markdown** (below). |
| **At a glance** | Counts of **Block rules**, **Inline rules** and **Nesting rules**. |
| **Edit Advanced JSON…** | Opens the profile as JSON for fields the guided editor does not expose. **Apply** keeps your JSON changes; **Cancel** discards them. |

**Extends Markdown** adds your rules to Markdown's: its headings, lists, emphasis and the rest are still read, and your block and inline rules add to them. A rule that is an unchanged copy of one of the CommonMark profile's describes what Markdown already does, and is left to it. **Replaces Markdown** makes your rules the whole syntax, so Markdown constructs stop being recognized. With it, one rule must produce **End of line**, or nothing separates into paragraphs. The editor warns "Add a rule whose output node is "newline", or nothing will separate into paragraphs", and the profile cannot be saved until one exists. It also lists any output types the profile does not define.

## Rules

Rules come in three groups.

### Block rules

A block rule recognizes whole lines and blocks. **Add rule** adds one. Each rule has a **Pattern**, a **Match** type, what it **Produces**, and **Options**. A rule is removed with its **Delete** button. With none, the editor says "No rules yet. Add one to recognize a block construct."

### Inline rules

An inline rule recognizes text inside a line. **Add inline rule** adds one. Inline rules offer four match types (**Literal prefix**, **Literal exact**, **Regex (bounded)** and **Delimiter pair**); block rules offer all seven.

### Nesting rules

Nesting rules say which outputs may sit inside which. Each has a **Parent node** and **Allowed children (comma separated)**. Empty means unrestricted: "No restrictions. Every node type may nest inside any other." **Add nesting rule** adds one.

### Match types

| Match type | Reads the pattern as | Block | Inline |
| --- | --- | --- | --- |
| **Literal prefix** | Text the construct starts with. | yes | yes |
| **Literal exact** | The whole text of the construct. | yes | yes |
| **Line-start prefix** | Text at the start of a line, such as `# `. | yes | |
| **Indented block** | Lines that begin with the pattern, such as four spaces or a tab. Consecutive ones, and blank lines between them, are one block, shown without the indent. | yes | |
| **Fenced block** | A line that opens a block, closed by a matching line. | yes | |
| **Regex (bounded)** | A regular expression. Pilcrow warns before saving one that could get stuck: "This regex could hang the editor — simplify it." | yes | yes |
| **Delimiter pair** | The same mark on both sides of text on one line, such as `%%` in `%%this%%`. There is no space just inside the marks. | yes | yes |

In a regular expression, `(?<name>…)` names a part of the match. See Named parts below.

## Rule options

Each rule's **Options** group offers:

| Option | What it does |
| --- | --- |
| **Priority** | Rules with a higher priority are tried first. |
| **Only at the start of a line** | Keeps a rule from matching mid-line. |
| **Named parts become attributes** | Each named part of a regular expression becomes an attribute of the output. The editor lists "Parts in this pattern" and "Parts this output reads". For an output that holds text, such as bold or a link, the text shown is the part named `text` if there is one, else the last part that matched. |
| **Produces** | What the rule makes: an output from the lists below, or a **Custom** name. |
| **Custom node name** | The name for a **Custom** output. |
| **Fixed attributes** | Parts that have the same value every time, added with **Add attribute** (a **Name** and a **Value**). A value may include a named part, written `{name}`: an e-mail rule whose pattern names the `address` can give its link the `url` `mailto:{address}`. |
| **Insert text** | What the **Insert** menu writes for this rule, exactly as it should appear, with `$0` where the caret should go. A rule matched by a regular expression, a block or indentation needs this, or the Insert menu leaves it out. |
| **Only after a blank line** | For an indented block: an indented line right after text stays part of that text, such as a list item's next line. |
| **After Return at the end of a line** | For lists and quotes: **Automatic** (repeats bullets and quotes, counts up numbered items, and starts task items unchecked), **Repeat the marker**, **Count up**, **Start fresh from the marker**, or **Add nothing**. |

### Fenced and delimited blocks

For a **Fenced block** rule, **Block holds** says what is inside:

| Choice | Meaning |
| --- | --- |
| **Nothing yet** | Not set. |
| **Text, shown as written** | Code or preformatted text. |
| **Nothing — hidden** | A comment, left out of the document. |
| **Other blocks, in a box** | A quote, sidebar or admonition holding paragraphs, lists and more. |
| **Other blocks, no box** | The blocks join the surrounding text; the lines only group them. |
| **A table** | See Tables, below. |
| **A table drawn in text** | A grid or aligned columns of text that runs from its opening line to the next blank line, such as reStructuredText's. |
| **Indented text under a line ending in a marker** | The opening line is prose that ends in the marker, as reStructuredText's `::` does; the prose stays a paragraph, and the text set in under it after a blank line is shown as written. |
| **Indented text under an opening line** | A directive such as `.. code-block::`, which holds the indented lines under it and has no closing line. |

**Closing line** is the line that ends the block; empty means the same line as the opening one ("Same as the opening line"). A delimiter that is not a regular expression, such as `+++`, is matched as plain text. **Closing line repeats the opening mark, at least as often** is for Markdown-style fences: the closing line is the opening line's first character repeated at least as many times, so a longer fence holds a shorter one as text. A text block's language, when the opening line names a known one, is coloured in the editor.

### Tables

A table block's options:

| Option | What it does |
| --- | --- |
| **Layout** | **Grid with rule lines** (cells between `|` with a rule line between rows) or **Aligned columns** (columns lined up under a first rule line). |
| **Cell separator** | The text that starts each cell. |
| **Rule line pattern**, **Header rule line pattern** | Lines that draw only a rule, and the one that ends the header. |
| **Row ends with** | A mark that ends each row, as a LaTeX `tabular` does. |
| **Spanning cell pattern** | A cell that spans columns. |
| **Cell options pattern** | A regular expression for what may come just before a cell's separator; a part named `colspan` makes the cell span that many columns. |
| **Column list separator**, **Repeat marker** | How a `columns` list is written: with `,` and `*`, `3*` counts three columns. |
| **First line before a blank line is the header** | The header row is implied by layout. |
| **Formats** | Other ways to write the cells, each a name and a separator (such as `csv` and `,`), added with **Add format** and chosen with the table's `format` part. |

## Profile-wide settings

| Setting | What it does |
| --- | --- |
| **Nest lists by marker** | Each new marker, such as `**` after `*`, starts a deeper level, whatever the indentation. |
| **List continuation line** | A line, alone after a list item, that attaches the next block to the item. |
| **Keep single line breaks** | A line break inside a paragraph stays a line break. |
| **Give headings ids** | A heading with no id of its own gets one from its title: lower case, words joined by the **word separator**, after the **prefix** (**Heading id prefix**, **Heading id word separator**). With `_` and `_`, "Getting Started" is `_getting_started`, so a cross-reference to it shows the title. A repeated title adds the separator and a number. |
| **Number headings** | Once the document defines the attribute named in **When the document defines**, such as AsciiDoc's `:sectnums:`, headings from **From heading level** down are numbered: `1.`, `1.1.`, `2.`. Headings before the definition are not. |
| **Numbered captions** | A titled block of an output listed here, such as `image`, `table` or `example`, gets the **Label** and its own number before its title (for example "Figure 1."), at the **Caption place**, **Above** or **Below** the block. Added with **Add caption**. |

## Inline marks that pair by what stands around them

A language such as Markdown writes bold and italic with a run of characters that opens or closes depending on the characters beside it, and a code span or link with brackets, so one pattern for the whole construct cannot find them. Turn on **Read marks by what stands around them** to describe them.

| Setting | What it does |
| --- | --- |
| **Escape character** | A character that makes the next one plain. |
| **Code span character** | A run of this character opens a span that the next run of the same length closes. |
| **Run marks** | Marks that pair as runs, added with **Add run mark**. Each has a **Mark**, what **One mark draws** and what **Two marks draw**, and **May open or close inside a word** (off for `_`). |
| **Pair marks** | Marks that pair with a run of the same length, added with **Add pair mark**: the **Mark**, what it **Draws**, and **Only when this setting is on**, a syntax setting such as highlight that must be on (or **Always**). |
| **Links and web addresses** | **Image prefix**, **Address written on its own is enclosed by**, **Schemes that begin a bare address**, **Line that defines a label has**, and **Footnote label begins with** (the character after a label's opening bracket that makes it a footnote: `[^note]` is drawn as a footnote reference when a line begins `[^note]:`). |

Marks pair within a line. Code, escaped characters and a link's address are plain text to the marks around them.

## Styled source

With **Styled Source** on, the editor draws a document in the look of its syntax: larger headings, bold and italic runs, quote bars, list indents, task boxes, rules, links and code cards, and hides the marks that make them (with **Hide Markers** on) except on the line the caret is on. The editor knows nothing about any one syntax: a rule says what its match is by carrying a styling entry, and a rule without one is coloured but not restyled.

Every rule's **Options** has a **Styled source** group:

| Field | What it does |
| --- | --- |
| **Role** | What the match is, or **Not styled**. For one construct inside a line: heading, strong, emphasis, code, strike, highlight, underline, link, subscript, superscript. For a whole line: rule (a thematic break), list (a list item's marker, including its indent and the space after it), task (a marker followed by a checkbox) and quote (the `>` marks of a quoted line). For a block recognized whole: codeBlock. For a block whose opening and closing lines are separate matches: quoteRegion. For a table, equation or diagram drawn as a picture: renderedBlock. |
| **Content group** | The capture group, counting from 1, that holds what the construct is about: the word inside `*bold*`, the title in `\section{Title}`. What the match has besides it is the construct's own marks, which Hide Markers hides. `0` means the whole match is content and nothing hides, as for a web address. Leave it out when the match is only marks, such as a heading's `== `. |
| **Heading level**, **Level group** | A heading's level, 1 to 6. Left out, it is the number at the end of the rule's output name (`heading2`), or the length of the capture group that holds a run of `#`. |
| **Marker group** | For a list or task, the capture group that is the marker with its indent and the spaces after it, when the match begins with something else, such as the `> ` of a quoted item. |
| **Styles to the end of the line** | Styles from the match to the end of the line, for a rule that matches only a heading's marker and leaves its title as the text that follows. |
| **Draws as** | For a rendered block, what it is: a table, math or diagram, or **Not a picture**. |
| **Address groups** | For a link, the capture groups, tried in order, that hold the address it opens when clicked or tapped; `0` is the whole match. Only web, mail and telephone addresses open. |

The group numbers count the pattern's parentheses from 1; 0 is the whole match. A profile that does not replace Markdown also keeps Markdown's own reading of the kinds its rules do not declare, such as its quote bars and the pairs of `**`.

## Document attributes and conditional sections

A **Document attribute** rule defines a value by `name`, and an **Attribute reference** rule (an inline rule with parts `name` and `original`) replaces a reference with it. A reference to an attribute no one has defined stays as written. A **Conditional section** keeps or drops the blocks between its lines, depending on whether the attributes it names are set. Attributes apply from where they are defined onwards.

A rule producing **Settings for the next block** recognizes a whole line that configures the block after it and shows nothing itself. Its parts and fixed attributes are given to that block: `title`, `id`, `nodeType`, `language` and `hardbreaks` have the meanings listed under Parts, and any other part is kept on the block, where a table, list or quote reads it.

## Testing a profile

At the bottom of the editor, **Test Sample** holds sample text (it starts as a heading and a line of text). Choose **Check sample** to see the nodes your rules make, indented as they nest. It says "No blocks recognized." when nothing matches.

## Baseline

A profile's **baseline** is its restore point: how it was when you created, duplicated or imported it. **Reset to Baseline** discards every change since then, after you confirm. **Set as New Baseline** saves the profile and makes its current state the restore point.

Saving is refused, with a message, if the profile replaces Markdown but has no end-of-line rule, if a pattern is unsafe and could hang the editor, or if the file cannot be written.

## Outputs

What a rule **Produces**: its name in the menu, then the name the profile file stores, whether block or inline rules can produce it, and the parts it reads. A rule may also name an output this list does not have, kept as **Custom**.

#### Text structure

| Output | Stored as | Kind | Reads |
| --- | --- | --- | --- |
| **Heading 1** | `heading1` | block |  |
| **Heading 2** | `heading2` | block |  |
| **Heading 3** | `heading3` | block |  |
| **Heading 4** | `heading4` | block |  |
| **Heading 5** | `heading5` | block |  |
| **Heading 6** | `heading6` | block |  |
| **Paragraph** | `paragraph` | block |  |
| **Horizontal rule** | `thematicBreak` or `thematic_break` | block |  |
| **End of line** | `newline` | block and inline |  |
| **Heading (level from the rule)** | `heading` | block | `level` |

#### Lists

| Output | Stored as | Kind | Reads |
| --- | --- | --- | --- |
| **List** | `list` | block | `ordered`, `start` |
| **Bulleted list item** | `listItemUnordered` | block |  |
| **Numbered list item** | `listItemOrdered` | block |  |
| **Checklist item** | `taskListMarker` | block |  |
| **Description list term** | `definition_term` | block | `term`, `marker` |

#### Blocks

| Output | Stored as | Kind | Reads |
| --- | --- | --- | --- |
| **Code block** | `code_block` or `codeBlock` or `fencedCode` | block | `language`, `content` |
| **Preformatted text** | `literal_block` | block |  |
| **Raw HTML** | `html_block` | block |  |
| **Equation** | `math_block` or `mathBlock` | block | `notation`, `content` |
| **Diagram** | `diagram` | block | `format`, `content` |
| **Table** | `table` | block | `columns`, `header`, `noHeader`, `format` |
| **Table row line** | `tableRow` | block |  |

#### Boxes and quotes

| Output | Stored as | Kind | Reads |
| --- | --- | --- | --- |
| **Quote** | `blockquote` | block | `attribution`, `citetitle` |
| **Quote line marker** | `blockquoteMarker` | block |  |
| **Admonition line** | `alertMarker` | block | `type` |
| **Admonition box** | `admonition` | block | `type`, `title` |
| **Sidebar** | `sidebar` | block | `title` |
| **Example box** | `example` | block | `title` |
| **Collapsible section** | `details` | block | `summary`, `open` |
| **Group (no box)** | `open_block` | block |  |

#### Hidden and settings

| Output | Stored as | Kind | Reads |
| --- | --- | --- | --- |
| **Comment (hidden)** | `comment` | block |  |
| **Settings for the next block** | `block_attributes` | block | `nodeType`, `title`, `id`, `language`, `hardbreaks`, `sectionLabel`, `sectionLabelStart`, `presentation` |
| **Document attribute** | `attribute_definition` | block | `name`, `value`, `unset` |
| **Conditional section** | `conditional` | block | `condition`, `conditionType`, `anyOf`, `allOf` |

#### Formatting

| Output | Stored as | Kind | Reads |
| --- | --- | --- | --- |
| **Bold** | `strong` | inline |  |
| **Italic** | `emphasis` | inline |  |
| **Highlight** | `mark` | inline |  |
| **Underline** | `underline` | inline |  |
| **Strikethrough** | `strikethrough` | inline |  |
| **Superscript** | `superscript` | inline |  |
| **Subscript** | `subscript` | inline |  |
| **Inline code** | `codeSpan` or `code` | inline |  |
| **Keyboard key** | `keyboard` | inline | `keys` |
| **Line break** | `line_break` | inline |  |
| **Replacement text** | `text` | inline | `content` |
| **Raw HTML (inline)** | `html_inline` | inline | `content` |

#### Links and references

| Output | Stored as | Kind | Reads |
| --- | --- | --- | --- |
| **Link** | `link` | inline | `url`, `title`, `text` |
| **Web address** | `autolink` | inline |  |
| **Cross-reference** | `cross_reference` | inline | `targetID`, `label` |
| **Anchor** | `anchor` | inline | `id`, `label` |
| **Attribute reference** | `substitution` | inline | `name`, `original` |
| **Footnote** | `footnote_definition` | inline | `id`, `text` |
| **Index term** | `index_term` | inline | `primary`, `secondary`, `tertiary` |

#### Media and maths

| Output | Stored as | Kind | Reads |
| --- | --- | --- | --- |
| **Image** | `image` | block and inline | `url`, `alt`, `title` |
| **Video** | `video` | block | `src` |
| **Audio** | `audio` | block | `src` |
| **Inline equation** | `math_inline` or `inlineMath` | inline | `notation`, `content` |



## Parts

Parts are the named pieces of a match that an output reads.

| Part | Meaning |
| --- | --- |
| `allOf` | The separator between names when all of them are needed, such as `+`. |
| `alt` | An image's description, for readers who cannot see it. |
| `anyOf` | The separator between names when any one of them is enough, such as `,`. |
| `attribution` | Who said a quote, shown under it. |
| `citetitle` | The work a quote comes from, shown after the attribution. |
| `columns` | A table's column list, such as `1,2,1`; its entries count the columns. |
| `condition` | The attribute names the section depends on. |
| `conditionType` | `defined` keeps the section when the attributes are set, `undefined` when they are not. |
| `content` | The text itself, when it is not the whole match. |
| `format` | A diagram's engine (`mermaid` or `vega-lite`); for a table, which of its delimited formats the cells use. |
| `hardbreaks` | When present, keeps the next block's single line breaks. |
| `header` | Any value but `false` makes a table's first row its header. |
| `id` | A name: for the next block, the id cross-references point to; for a footnote, a name that lets later footnotes with no text of their own share its number. |
| `keys` | The keys to press, separated by commas. |
| `label` | The text shown for a reference or anchor, in place of the target's own title. |
| `language` | A code block's programming language, used for its coloring. |
| `level` | The heading level, from 1 to 6. |
| `marker` | The separator after the term, such as `::`. A different marker nests a list inside the description. |
| `name` | The attribute's name, in a definition or a reference. |
| `nodeType` | Makes the next block into another output, by its name in the file. |
| `noHeader` | When present, a table has no header row. |
| `notation` | The maths notation: `tex` (the default) or `latex`. |
| `open` | `true` shows a collapsible section open. |
| `ordered` | `true` makes the list numbered. |
| `original` | The reference as written, shown when the attribute is not defined. |
| `presentation` | How the next description list is shown: `sideBySide` puts terms and descriptions in two columns; `questions` numbers each term as a question, with its answer under it. |
| `primary` | The index entry. |
| `secondary` | A sub-entry under the index entry. |
| `sectionLabel` | A word the next heading's number follows, such as `Appendix`: such headings are counted on their own, `Appendix A:`. |
| `sectionLabelStart` | The first of those numbers: a letter (`A`) counts in letters, a number in numbers. |
| `src` | The address of the video or audio file. |
| `start` | The number a numbered list starts at. |
| `summary` | The line shown on a collapsible section while it is closed. |
| `targetID` | The id the reference points to. |
| `term` | The term being described. |
| `tertiary` | A sub-entry under the secondary one. |
| `text` | The text shown, when the pattern captures more than that. A footnote's text follows the paragraph, table or list it is in, numbered. |
| `title` | A title: a box's heading, an image's or link's tooltip, or a caption above the next block. |
| `type` | The kind of admonition, such as `note`, `tip` or `warning`. |
| `unset` | When present, the rule removes the attribute instead of defining it. |
| `url` | The address a link or image points to. |
| `value` | The attribute's value; references to attributes defined earlier are replaced in it. |

# Chapter 75: The theme editors

There are two kinds of theme, and each has its own editor. Open either from **Settings ▸ Library ▸ Themes**: **New** creates a theme, **Edit** changes a custom one, and **Duplicate** copies a built-in theme so you can change the copy. Built-in themes cannot be edited.

## The Render Theme editor

**Edit Render Theme** styles Preview, HTML, PDF, image and print output. Its Pilcrow custom properties also set Word styles. A Render Theme does not style the app or the editor.

| Part | What it does |
| --- | --- |
| **Name** | The theme's name. |
| **Appearance** | **Automatic**, **Light** or **Dark**. |
| **CSS** | The stylesheet, in a code editor. See Chapter 80 for the properties and classes. |
| **Rendered preview** | A specimen document drawn with your CSS as you type, so you can see the effect. |
| **CSS diagnostics** | Problems Pilcrow found in the CSS, such as a remote resource that is not allowed. |
| **Cancel**, **Save** | Close or keep the theme. Closing with changes asks **Discard theme changes?** with **Discard Changes** or **Keep Editing**. |
| **Baseline** | **Reset to Baseline** discards every change since the theme was created, duplicated or imported (after you confirm). **Set as New Baseline** saves the theme and makes its current state the restore point. |

## The Application Theme editor

**Edit Application Theme** styles Pilcrow itself: its appearance, accent, sidebar, bars and editor.

| Part | What it does |
| --- | --- |
| **Name** | The theme's name. |
| **Appearance** | **Automatic**, **Light** or **Dark**. An Automatic theme has two palettes. |
| **Editing colours for** | For an Automatic theme, **Light** or **Dark**: which of its two palettes you are editing. |
| Colours, in five groups | **App** (the accent), **Sidebar** (background and foreground), **Status and formatting bars** (background and foreground), **Editor** (background, foreground, cursor, selection, gutter background, gutter foreground, current-line rule), and **Syntax** (heading, marker, code, link, muted, and code keyword, string, number and comment). Each colour shows **Default** until you set one, and a **Reset** button puts it back. |
| **Preview** | A miniature of Pilcrow, with a sidebar, an editor and a status bar, in the colours you chose, in light or dark. |
| **Cancel**, **Save**, **Baseline** | As above. |

A theme may also colour individual syntax tokens. Those colours are kept, but are edited in the theme's JSON file (`syntax.tokens`); see Chapter 79.

# Chapter 76: The macro editor

Open the macro editor from **Settings ▸ Library ▸ Macros**: **New** inside a collection, or **Edit** on a macro. Its title is **New Macro** or **Edit Macro**.

| Field | What it does |
| --- | --- |
| **Name** | A label for the macro. |
| **Trigger** (for example `/sig`) | The text that starts it. A macro expands when you type the trigger followed by a space, tab or return. |
| **Match** | How the trigger is read: **Exact text**, **Prefix**, or **Regular expression**. A regular expression that could hang the editor is refused: "That regular expression could hang the editor. Simplify it." |
| **Replacement** | The text it expands to. |
| **Insert Date/Time** | A menu that adds a date or time token to the replacement. |
| **Enabled** | Turns the macro on or off without deleting it. |
| **Don't expand inside code** | Stops the macro firing inside code spans and code blocks. |
| **Cancel**, **Save** | Close or keep the macro. If it cannot be saved, the message says why. |

In the replacement, `$1`, `$2` and so on are tab stops, and `$0` is where the cursor lands. After a macro expands, Tab (or **Next Field**) jumps from stop to stop. Dates and times use tokens: `{{date:yyyy-MM-dd}}`, `{{time:HH:mm:ss}}` and `{{datetime:MM/dd/yyyy h:mm a}}`, and named formats `iso8601`, `rfc2822`, `unix`, `short`, `medium`, `long` and `full`. A **Now:** line under the field shows what the replacement would produce at this moment.

---

# Part XX — Shortcuts and using iPad

# Chapter 77: The complete shortcut list

This chapter lists every default shortcut in one place. Shortcuts in **bold** can be changed in **Settings ▸ Keyboard** (Chapter 72). The Mac uses the symbols below; on iPad they work with a hardware keyboard.

| Symbol | Key |
| --- | --- |
| `⌘` | Command |
| `⌥` | Option |
| `⌃` | Control |
| `⇧` | Shift |

## Files and documents

| Action | Shortcut |
| --- | --- |
| New document | `⌘N` |
| Open | `⌘O` |
| Open Quickly | `⇧⌘O` |
| Close document | `⌘W` |
| Close all (iPad) | `⇧⌘W` |
| Save | `⌘S` |
| Save All | `⌥⌘S` |
| Duplicate | `⇧⌘S` |
| Save As | `⌥⇧⌘S` |
| Export | `⇧⌘E` |
| Print | `⌘P` |
| Open Documents | **`⌃⌘2`** |
| Next document | `⌃Tab` |
| Previous document | `⌃⇧Tab` |
| Pilcrow Help | `⌘?` |
| Settings (Mac) | `⌘,` |

## Editing

| Action | Shortcut |
| --- | --- |
| Undo | `⌘Z` |
| Redo | `⇧⌘Z` |
| Copy as Markdown | `⇧⌘C` |
| Paste as Plain Text | `⇧⌘V` |
| Find | `⌘F` |
| Replace | `⌘R` |
| Find Next | `⌘G` |
| Find Previous | `⇧⌘G` |
| Show Spelling and Grammar (Mac) | `⌘:` |
| Check Document Now (Mac) | `⌘;` |
| Go to Line | `⌃G` |
| Command Palette | **`⌃⇧P`** |
| Go Back | **`⌃⌘←`** |
| Go Forward | **`⌃⌘→`** |
| Move Row Up | `⌥⌘↑` |
| Move Row Down | `⌥⌘↓` |

## Selecting, carets and deleting

| Action | Shortcut |
| --- | --- |
| Select Word | `⌘D` |
| Select Line | `⌘L` |
| Select Paragraph | `⌥⌘P` |
| Jump to Top | `⌘↑` |
| Jump to Bottom | `⌘↓` |
| Jump to Line Start | `⌃A` |
| Jump to Line End | `⌃E` |
| Add Caret Above | **`⌃⇧↑`** |
| Add Caret Below | **`⌃⇧↓`** |
| Select Next Occurrence | **`⌃⌥D`** |
| Select All Occurrences | **`⌃⌥⇧D`** |
| Carets in a Column | **`⌃⇧G`** |
| Next Field | **`⌥Tab`** |
| Previous Field | **`⌥⇧Tab`** |
| Delete Word | `⇧⌘D` |
| Delete Line | `⌥⇧⌘L` |
| Delete Paragraph | `⌥⇧⌘P` |

With a trackpad or mouse on a Mac, hold **Option** and drag to select a rectangle of text.

## Formatting and inserting

| Action | Shortcut |
| --- | --- |
| Strong | **`⌘B`** |
| Emphasis | **`⌘I`** |
| Inline Code | **`⌃`** followed by a backtick: `` ⌃` `` |
| Strikethrough | **`⌃⇧`** `` ` `` |
| Inline Math | **`⌃M`** |
| Hyperlink | **`⌘K`** |
| Clear Format | **`⌘\`** |
| Paragraph | `⌘0` |
| Heading 1 to Heading 6 | `⌘1` to `⌘6` |
| Increase Heading Level | `⌘=` |
| Decrease Heading Level | `⌘-` |
| Unordered List | `⌥⌘U` |
| Ordered List | `⌥⌘O` |
| Task List | `⌥⌘X` |
| Indent | `⌘]` |
| Outdent | `⌘[` |
| Blockquote | `⌥⌘Q` |
| Code Fences | `⌥⌘C` |
| Insert Table | `⌥⌘T` |
| Insert Image | `⇧⌘I` |
| Horizontal Line | `⌥⌘-` |
| Link Reference | `⌥⌘K` |
| Footnote | `⌥⌘R` |

## View

| Action | Shortcut |
| --- | --- |
| Toggle Sidebar | **`⇧⌘L`** |
| Outline | **`⌃⌘1`** |
| Files | **`⌃⌘3`** |
| Search | **`⇧⌘F`** |
| Assistant | **`⌃⌘4`** |
| Preview | `⇧⌘P` |
| Side by Side | `⌃⌘P` |
| Focus Mode | **none** |
| Actual Size | `⇧⌘0` |
| Zoom In | `⇧⌘=` |
| Zoom Out | `⇧⌘-` |
| Line Numbers | `⌥⌘L` |

Shortcuts for items that have none, such as Focus Mode, Highlight, Subscript and Superscript, are set by assigning one in **Settings ▸ Keyboard**, where the command is listed, or by using the command palette.

# Chapter 78: Using Pilcrow on iPad

Pilcrow runs on iPadOS 17 or later. It works with touch alone, with a hardware keyboard, and with a trackpad or mouse.

## Touch

- **Pane divider.** In Side by Side, drag the divider between source and preview to resize them. Double-tap it to reset.
- **Navigator.** Drag the sidebar's edge to resize it. In a narrow window the sidebar covers the document and a **Done** button closes it.
- **Column selection.** Turn on **More ▸ Column Selection**, then drag one finger to select a rectangle of text. Two fingers still scroll. A **Column Selection** badge shows while it is on, with a button to turn it off. Or use **More ▸ Carets in a Column…** to place carets by number.
- **The context menu.** Press and hold in the text for the editor's menu (below).
- **Files.** Press and hold a file in the Files panel for its menu (Chapter 60).

## With a hardware keyboard

Every shortcut in Chapter 77 works. Hold **⌘** to see the iPad's menu bar, or move a pointer to the top of the screen. Pilcrow can hide its own header menus when a keyboard or mouse is connected; see **Settings ▸ Appearance ▸ Menus in the Header**.

## With a trackpad or mouse

Right-click opens the editor's context menu. Hold **Option** while dragging to select a rectangle of text.

## The editor's context menu

Right-click on Mac, or press and hold on iPad, in the text. Items the active syntax profile cannot express are greyed out, and the system adds its own items (Cut, Copy, Paste, spelling suggestions, Look Up and so on).

On **Mac**:

| Item | What it does |
| --- | --- |
| **Copy / Paste As…** | **Copy as Markdown**, **Copy as Plain Text**, **Copy as HTML Code**, **Paste as Plain Text**. |
| **Paragraph** | **Paragraph**, **Heading 1** to **6**, **Blockquote**, **Bulleted List**, **Numbered List**, **Task List**, **Code Fence**. |
| **Format** | **Strong**, **Emphasis**, **Code**, **Strikethrough**, **Inline Math**, **Display Math**, **Diagram**, **Chart**, **Hyperlink**. |
| **Selection** | **Select Word**, **Select Line**, **Select Paragraph**. |

On **iPad**, three submenus sit with the system's items:

| Item | What it does |
| --- | --- |
| **Format** | The inline styles: strong, emphasis, code and the rest. |
| **Paragraph** | The paragraph types: headings, quote, lists, code fence. |
| **Insert** | The same inserts as the formatting toolbar's **More** menu, including **Insert Alert**, **Insert Image…** and **Insert Table…**, and, under **Syntax**, the active profile's own constructs. |

## Differences from the Mac

| On iPad | On Mac |
| --- | --- |
| Settings opens from the gear in the header, in a sheet. | **Pilcrow ▸ Settings…** (`⌘,`). |
| The header can show Pilcrow's own menus (**Menus in the Header**). | The menu bar is the system's. |
| **Interface Size** sets the size of menus, bars and dialogs. | Not available. |
| Import is in **Settings ▸ Library ▸ Import**. | **File ▸ Import**. |
| No Save All, Duplicate, Move To, Reload from Disk, Show in Finder or Page Setup. | These are in the File menu. |
| **Edit ▸ Spelling and Grammar** has one item, **Check Spelling While Typing**. | **Edit ▸ Spelling and Grammar** also has **Show Spelling and Grammar** and **Check Document Now**. |
| Typing sounds are muted by the iPad's silent switch. | Not applicable. |
