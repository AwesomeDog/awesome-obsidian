<div align="center">

# Awesome Obsidian

<p align="center">
  <b>Obsidian plugins, themes, and workflows for building a local-first Markdown knowledge base.</b>
  <br>
  <sub>A short, maintenance-aware map organized around the jobs a vault needs to do.</sub>
</p>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/AwesomeDog/awesome-obsidian/pulls)
[![Obsidian](https://img.shields.io/badge/Obsidian-Community-purple.svg?logo=obsidian)](https://obsidian.md)
[![Stars](https://img.shields.io/github/stars/AwesomeDog/awesome-obsidian?style=flat&logo=github)](https://github.com/AwesomeDog/awesome-obsidian/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/AwesomeDog/awesome-obsidian)](https://github.com/AwesomeDog/awesome-obsidian/commits)

<p align="center" class="github-only">
  <b>Reading this on GitHub?</b> Try the <a href="https://awesomedog.github.io/awesome-obsidian/"><b>searchable web version</b></a> — full-text search, collapsible sections, and a light/dark theme toggle.
</p>

</div>

---

## Contents

- [Start Here](#start-here)
- [How to Choose](#how-to-choose)
  - [Core Before Plugins](#core-before-plugins)
  - [Safety](#safety)
  - [Curation](#curation)
- [Curated Catalog](#curated-catalog)
  - [0. Getting Started](#0-getting-started)
  - [1. Capture & Ingestion](#1-capture--ingestion)
  - [2. Writing & Editing](#2-writing--editing)
  - [3. Organizing & Metadata](#3-organizing--metadata)
  - [4. Linking & Discovery](#4-linking--discovery)
  - [5. Data Views](#5-data-views)
  - [6. Tasks, Habits & Review](#6-tasks-habits--review)
  - [7. Output & Publishing](#7-output--publishing)
  - [8. Aesthetics & Interface](#8-aesthetics--interface)
  - [9. Vault Maintenance & Sync](#9-vault-maintenance--sync)
  - [10. Automation & AI](#10-automation--ai)
- [Playbooks by Role](#playbooks-by-role)
  - [Students & Learners](#students--learners)
  - [Researchers & Graduate Students](#researchers--graduate-students)
  - [Developers & Technical Authors](#developers--technical-authors)
  - [Writers & Content Creators](#writers--content-creators)
  - [Project Managers & Knowledge Workers](#project-managers--knowledge-workers)
  - [Visual Thinkers & Designers](#visual-thinkers--designers)
  - [Language & Media Learners](#language--media-learners)
  - [Automation Builders & Power Users](#automation-builders--power-users)
- [Workflows](#workflows)
- [Discover New Plugins](#discover-new-plugins)
- [Resources](#resources)
- [FAQ](#faq)

---

## Start Here

**Obsidian** is a local-first Markdown application. Notes stay as ordinary files on your disk, while plugins extend the app around that foundation.

This is a **decision aid**, not a directory of every plugin. It keeps curated sections short, puts core features first, and separates reviewed recommendations from an automated view of newly registered plugins.

### Choose Your Path

| If you are...                       | Start with...                       |
| ----------------------------------- | ----------------------------------- |
| New to Obsidian                     | **Core Before Plugins**             |
| Solving one repeated problem        | **Curated Catalog**                 |
| Picking a starter kit by role       | **Playbooks by Role**               |
| Comparing tools or planning a setup | **How to Choose** and **Workflows** |
| Looking for recent releases         | **Discover New Plugins**            |

### The Core Idea

Knowledge normally moves through a vault as:

> **Capture -> Write -> Organize -> Retrieve -> Act -> Publish**

The catalog follows these jobs. Start where the friction is; there is no need to install a complete stack.

---

## How to Choose

Use this order: **name the problem -> check core -> run a reversible experiment -> install one plugin**. Your notes should remain understandable if the plugin disappears.

### Core Before Plugins

Check the built-in option first:

| You want to...              | Check this core feature                    |
| --------------------------- | ------------------------------------------ |
| Store structured metadata   | **Properties** and frontmatter             |
| Build filterable note views | **Bases**                                  |
| Draw spatial relationships  | **Canvas**                                 |
| Jump to notes or commands   | **Quick Switcher** and **Command palette** |
| Create recurring notes      | **Templates** and **Daily notes**          |
| Recover accidental changes  | **File recovery**                          |
| Clip or migrate content     | Official **Web Clipper** and **Importer**  |

Choose a community plugin only when core cannot solve the recurring need or the plugin provides a clear workflow improvement.

### Safety

- Community plugins can read, write, and send data from your vault. Read the repository and understand its network behavior.
- Keep File recovery and an independent backup enabled before migrations, bulk edits, or tools with write access.
- Install one plugin at a time. Use Restricted mode to isolate a problem.
- Check mobile support and external requirements such as Git, Pandoc, Zotero, or an API key.

### Curation

Curated entries are selected for maintenance, adoption or clear niche value, non-redundancy with core, portable data, licensing, and fit within a short category. See `CONTRIBUTING.md` for the full standard.

---

## Curated Catalog

Each section represents a job, not a required installation step. Use the description to decide whether the problem is yours, then test the smallest useful option.

### 0. Getting Started

> Essential plugins for newcomers. Learn what core features already provide before installing extra tools.

#### First 30 Minutes (No Plugins Required)

**1. Create one vault** and let it be messy — folders can come later.<br>
**2. Turn on the core plugins you will actually use:** **Daily notes**, **Templates**, **Backlinks**, **Outgoing links**, **Bookmarks**, **File recovery**.<br>
**3. Write 10 notes and link them with `[[ ]]`. Feel where the friction is.**<br>
**4. Then return to this list and fix that specific friction.**

#### Optional starting point

The tool below is a general-purpose starting point: it pays off in almost any vault and does not lock your notes into a private format. It also appears in the job it belongs to further down — start here, then read that section before you install it.

- [QuickAdd](https://github.com/chhoumann/quickadd) - Quickly add new notes or content to your vault.
  [⚡ Open](https://obsidian.md/plugins?id=quickadd)
- [Awesome Format Bar](https://github.com/awesomedog/obsidian-awesome-format-bar) - Word-style Markdown formatting toolbar for Obsidian — bold, underline, highlight, color, headings, tables, callouts, emoji picker and 100+ one-click commands.
  [⚡ Open](https://obsidian.md/plugins?id=awesome-format-bar)

---

### 1. Capture & Ingestion

> Streamline bringing external highlights, articles, academic citations, and media into your vault.

- [Importer](https://github.com/obsidianmd/obsidian-importer) - Convert your data to Markdown files you can use in Obsidian. Works with Apple Notes, OneNote, Evernote, Notion, Google Keep, and many other formats.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-importer)
- [Readwise Official](https://github.com/readwiseio/obsidian-readwise) - Sync highlights from Readwise to your vault.
  [⚡ Open](https://obsidian.md/plugins?id=readwise-official)
- [ZotLit](https://github.com/aidenlx/zotlit) - Integrate with Zotero, create literature notes, and insert citations from a Zotero library.
  [⚡ Open](https://obsidian.md/plugins?id=zotlit)
- [Snipd Official](https://github.com/snipd-app/snipd-obsidian) - Sync Snipd podcast highlights to your vault with transcript, notes, AI summaries and metadata.
  [⚡ Open](https://obsidian.md/plugins?id=snipd-official)
- [rss-dashboard](https://obsidian.md/plugins?id=rss-dashboard) - Not found in the official registry.
- [Advanced URI](https://github.com/vinzent03/obsidian-advanced-uri) - Control everything with URI.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-advanced-uri)

> The official **Web Clipper** and **Importer** cover one-off capture and migration; use these plugins for recurring pipelines.

---

### 2. Writing & Editing

> Enhance text input, table editing, formatting hygiene, autocompletion, and long-form focus.

- [Harper](https://github.com/automattic/harper-obsidian-plugin) - The fastest grammar and spell checker that respects your privacy.
  [⚡ Open](https://obsidian.md/plugins?id=harper)
- [Longform](https://github.com/kevboh/longform) - Helps you write and edit novels, screenplays, and other long projects.
  [⚡ Open](https://obsidian.md/plugins?id=longform)
- [Outliner](https://github.com/vslinko/obsidian-outliner) - Work with your lists like in Workflowy or Roam Research.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-outliner)
- [Various Complements](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin) - Complete words similar to auto-completion in an IDE.
  [⚡ Open](https://obsidian.md/plugins?id=various-complements)
- [Latex Suite](https://github.com/artisticat1/obsidian-latex-suite) - Make typesetting LaTeX math as fast as handwriting through snippets, text expansion, and editor enhancements.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-latex-suite)
- [Novel word count](https://github.com/isaaclyman/novel-word-count-obsidian) - Display a word count, page count, creation date, or other statistics for each file, folder and vault in the File Explorer pane.
  [⚡ Open](https://obsidian.md/plugins?id=novel-word-count)

---

### 3. Organizing & Metadata

> Structure your notes with folder notes, tag management, properties/frontmatter, and attachment rules.

- [Metadata Menu](https://github.com/mdelobelle/metadatamenu) - For data quality enthusiasts and Dataview users: access and manage the metadata of your notes.
  [⚡ Open](https://obsidian.md/plugins?id=metadata-menu)
- [Pretty Properties](https://github.com/anareaty/pretty-properties) - Makes note properties look more fun: adds side image, banners, list property colors and allows to hide specific properties.
  [⚡ Open](https://obsidian.md/plugins?id=pretty-properties)
- [Tag Wrangler](https://github.com/pjeby/tag-wrangler) - Rename, merge, toggle, and search tags from the tag pane.
  [⚡ Open](https://obsidian.md/plugins?id=tag-wrangler)
- [TagFolder](https://github.com/vrtmrz/obsidian-tagfolder) - Show tags as folder.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-tagfolder)
- [Folder notes](https://github.com/lostpaul/obsidian-folder-notes) - Create notes within folders that can be accessed without collapsing the folder, similar to the functionality offered in Notion.
  [⚡ Open](https://obsidian.md/plugins?id=folder-notes)
- [Iconic](https://github.com/gfxholo/iconic) - Customize your icons and their colors directly from the UI, including tabs, files & folders, bookmarks, tags, properties, and ribbon commands.
  [⚡ Open](https://obsidian.md/plugins?id=iconic)

> Keep canonical structure in plain frontmatter and core **Properties**; use these tools for editing ergonomics.

---

### 4. Linking & Discovery

> Find notes with fuzzy search, explore deep graph connections, and leverage semantic AI search.

- [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher) - Another choice of Quick switcher.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-another-quick-switcher)
- [Smart Connections](https://github.com/brianpetro/obsidian-smart-connections) - Find related notes and excerpts while writing. Your AI link building copilot displays relevant content in graph + list view. A local embedding model powers semantic search. Zero setup. No API key.
  [⚡ Open](https://obsidian.md/plugins?id=smart-connections)
- [Breadcrumbs](https://github.com/michaelpporter/breadcrumbs) - Visualise the hierarchy of your vault using a breadcrumb trail or matrix view.
  [⚡ Open](https://obsidian.md/plugins?id=breadcrumbs)
- [Extended Graph](https://github.com/elsatam/obsidian-extended-graph) - Extends the features of the core Graph view, display images, manage states, remove links, change node shapes, and more.
  [⚡ Open](https://obsidian.md/plugins?id=extended-graph)
- [floating toc](https://github.com/pkm-er/obsidian-floating-toc-plugin) - A floating directory that hovers a widget of the current directory on the notes page.
  [⚡ Open](https://obsidian.md/plugins?id=floating-toc)
- [Hover Editor](https://github.com/nothingislost/obsidian-hover-editor) - Transform the Page Preview hover popover into a fully working editor instance.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-hover-editor)

---

### 5. Data Views

> Aggregate notes into dynamic queries, database tables, visual diagrams, and interactive canvases.

- [Datacore](https://github.com/blacksmithgu/datacore) - An even faster reactive query engine for the data obsessed.
  [⚡ Open](https://obsidian.md/plugins?id=datacore)
- [Maps](https://github.com/obsidianmd/obsidian-maps) - Adds a map layout to bases so you can display notes as an interactive map view.
  [⚡ Open](https://obsidian.md/plugins?id=maps)
- [Calendar Bases](https://github.com/edrickleong/obsidian-calendar-bases) - Adds a calendar layout to bases so you can display notes with dates in an interactive calendar view.
  [⚡ Open](https://obsidian.md/plugins?id=calendar-bases)
- [Sheet Plus](https://github.com/ljcoder2015/obsidian-sheet-plus) - Create Excel-like spreadsheets and easily embed them in Markdown.
  [⚡ Open](https://obsidian.md/plugins?id=sheet-plus)
- [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin) - Visual PKM powerhouse. Create and edit Excalidraw drawings.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-excalidraw-plugin)
- [Homepage](https://github.com/mirnovov/obsidian-homepage) - Open a note, base, or workspace on startup, or set it for quick access later.
  [⚡ Open](https://obsidian.md/plugins?id=homepage)

> **Bases** is the default starting point. Use for performance-heavy reactive views.

---

### 6. Tasks, Habits & Review

> Turn thoughts into action items, visual Kanban boards, time blocks, and spaced repetition flashcards.

- [Tasks](https://github.com/obsidian-tasks-group/obsidian-tasks) - Track tasks across your vault. Supports due dates, recurring tasks, done dates, sub-set of checklist items, and filtering. Maintained by Clare Macrae and Ilyas Landikov, created by Martin Schenck.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-tasks-plugin)
- [TaskNotes](https://github.com/callumalpass/tasknotes) - Note-based task management with calendar, pomodoro and time-tracking integration.
  [⚡ Open](https://obsidian.md/plugins?id=tasknotes)
- [Day Planner](https://github.com/ivan-lednev/obsidian-day-planner) - Turn tasks from daily notes, the Tasks plugin, and calendars into time blocks on an editable timeline, with built-in time tracker.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-day-planner)
- [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) - Fight the forgetting curve by reviewing flashcards & entire notes.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-spaced-repetition)
- [Flashcards](https://github.com/reuseman/flashcards-obsidian) - Anki integration.
  [⚡ Open](https://obsidian.md/plugins?id=flashcards-obsidian)
- [Habit Tracker 21](https://github.com/zincplusplus/habit-tracker) - A minimalist, elegant habit tracker that helps you build lasting habits with clear progress visualization.
  [⚡ Open](https://obsidian.md/plugins?id=habit-tracker-21)

> Pick one task and date convention; Tasks, TaskNotes, and Day Planner need compatible syntax to share a schedule.

---

### 7. Output & Publishing

> Share your knowledge through digital gardens, static websites, PDF/Word exports, and slide decks.

- [Digital Garden](https://github.com/oleeskild/obsidian-digital-garden) - Publish your notes to a digital garden for others to enjoy.
  [⚡ Open](https://obsidian.md/plugins?id=digitalgarden)
- [Enveloppe](https://github.com/enveloppe/obsidian-enveloppe) - Publish your notes to a preconfigured GitHub repository.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-mkdocs-publisher)
- [Webpage HTML Export](https://github.com/kosmosisdire/obsidian-webpage-export) - Export html from single files, canvas pages, or whole vaults. Direct access to the exported HTML files allows you to publish your digital garden anywhere. Focuses on flexibility, features, and style parity.
  [⚡ Open](https://obsidian.md/plugins?id=webpage-html-export)
- [Enhancing Export](https://github.com/mokeyish/obsidian-enhancing-export) - Enhanced export based on Pandoc. Allows export to formats like HTML, DOCX, ePub and PDF or Hugo.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-enhancing-export)
- [Slides Extended](https://github.com/ebullient/obsidian-slides-extended) - Create markdown-based reveal.js presentations. Fork of Advanced Slides.
  [⚡ Open](https://obsidian.md/plugins?id=slides-extended)
- [Share Note](https://github.com/alangrainger/share-note) - Instantly share/publish a note, with the full theme and content exactly like you see in Obsidian. Data is shared encrypted by default, and only you and the person you send it to have the key.
  [⚡ Open](https://obsidian.md/plugins?id=share-note)

> Export tools need **Pandoc**; PDF output also needs a LaTeX engine.

---

### 8. Aesthetics & Interface

> Upgrade Obsidian with modern multi-column navigation, clean minimalism, and polished layouts.

- [Notebook Navigator](https://github.com/johansan/notebook-navigator) - A better file browser and calendar inspired by Apple Notes, Bear, Evernote and Day One.
  [⚡ Open](https://obsidian.md/plugins?id=notebook-navigator)
- [Style Settings](https://github.com/obsidian-community/obsidian-style-settings) - Adjust theme, plugin, and snippet CSS variables.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-style-settings)
- [Commander](https://github.com/jsmorabito/obsidian-commander) - Customize your workspace by adding commands everywhere, create macros and supercharge your mobile toolbar.
  [⚡ Open](https://obsidian.md/plugins?id=cmdr)
- [Hider](https://github.com/kepano/obsidian-hider) - Hide interface elements such as tooltips, status bar, titlebar, and more.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-hider)
- [Colored Tags](https://github.com/pfrankov/obsidian-colored-tags) - Colorize tags in different colors to visually distinguish them from each other.
  [⚡ Open](https://obsidian.md/plugins?id=colored-tags)

> Prefer a CSS snippet for purely cosmetic changes.

---

### 9. Vault Maintenance & Sync

> Cross-platform synchronization, cloud backups, Git version control, and performance optimization.

- [Self-hosted LiveSync](https://github.com/vrtmrz/obsidian-livesync) - Sync vaults securely to self-hosted servers or WEBRTC.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-livesync)
- [Nutstore Sync](https://github.com/nutstore/obsidian-nutstore-sync) - Sync your vault with Nutstore (坚果云) using WebDAV protocol.
  [⚡ Open](https://obsidian.md/plugins?id=nutstore-sync)
- [Git](https://github.com/vinzent03/obsidian-git) - Integrate Git version control with automatic backup and other advanced features.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-git)
- [Consistent Attachments and Links](https://github.com/dy-sh/obsidian-consistent-attachments-and-links) - Move note attachments and update links automatically.
  [⚡ Open](https://obsidian.md/plugins?id=consistent-attachments-and-links)
- [File Cleaner Redux](https://github.com/husjon/obsidian-file-cleaner-redux) - Help you to clean empty files and unused attachments in the vault.
  [⚡ Open](https://obsidian.md/plugins?id=file-cleaner-redux)
- [Janitor](https://github.com/canna71/obsidian-janitor) - Perform cleanup tasks on your vault.
  [⚡ Open](https://obsidian.md/plugins?id=janitor)

> Use one sync mechanism per vault. Sync mirrors changes; keep a separate versioned backup.

---

### 10. Automation & AI

> Integrate LLMs, autonomous coding agents, and automated macros directly inside your vault.

- [Copilot](https://github.com/logancyang/obsidian-copilot) - Run AI agents such as Claude Code, Codex, and OpenCode inside your vault. Turn your second brain into a smart assistant that gets knowledge work done.
  [⚡ Open](https://obsidian.md/plugins?id=copilot)
- [Local REST API with MCP](https://github.com/coddingtonbear/obsidian-local-rest-api) - Unlock your automation needs by interacting with your notes over a secure REST API.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-local-rest-api)
- [Text Generator](https://github.com/nhaouari/obsidian-textgenerator-plugin) - Generate text content using GPT-3 (OpenAI).
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-textgenerator-plugin)
- [Local LLM Hub](https://github.com/takeshy/obsidian-local-llm-hub) - Chat with local LLMs (Ollama, LM Studio) with local embeddings RAG, file encryption, edit history, slash commands, and workflow automation.
  [⚡ Open](https://obsidian.md/plugins?id=local-llm-hub)
- [Lean Terminal](https://github.com/sdkasper/lean-obsidian-terminal) - Embedded terminal panel powered by xterm.js and node-pty - no external windows.
  [⚡ Open](https://obsidian.md/plugins?id=lean-terminal)
- [MCP Connector](https://github.com/istefox/obsidian-mcp-connector) - Connect MCP-compatible clients (Claude Desktop, Claude Code, Cline) to your vault with semantic search, templates, file management and gated command execution.
  [⚡ Open](https://obsidian.md/plugins?id=mcp-tools-istefox)

> Before enabling AI, check what leaves the vault. Prefer local models for sensitive notes and versioned backups for agents that can write.

---

## Playbooks by Role

The catalog above is organized by *job*. These playbooks are organized by *person* — pick the one that matches you, install that short list, and ignore the rest. No plugin appears in both views, so every entry here adds an option instead of repeating one.

### Students & Learners

> Course material needs a reliable path from capture to understanding, memory, and review.

**Chain:** import slides and handouts -> annotate the source PDFs with **PDF++** -> sketch each hard concept as a **Mind Map** -> keep one **Periodic Notes** page per lecture week -> export assignments through **Pandoc Plugin** and proofread them with **LanguageTool**. Keep an inbox and a weekly review so the vault stays useful during exam season.

- [PDF++](https://github.com/ryotaushio/obsidian-pdf-plus) - The most Obsidian-native PDF annotation tool ever.
  [⚡ Open](https://obsidian.md/plugins?id=pdf-plus)
- [Mind Map](https://github.com/lynchjames/obsidian-mind-map) - Display Markdown notes as mind maps using Markmap.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-mind-map)
- [Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes) - Manage your daily, weekly, and monthly notes.
  [⚡ Open](https://obsidian.md/plugins?id=periodic-notes)
- [Pandoc Plugin](https://github.com/oliverbalfour/obsidian-pandoc) - Commands to export to Pandoc-supported formats like DOCX, ePub and PDF.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-pandoc)
- [LanguageTool Integration](https://github.com/clemens-e/obsidian-languagetool-plugin) - Advanced grammar and spell checking, powered by LanguageTool.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-languagetool-plugin)

---

### Researchers & Graduate Students

> Make every conclusion traceable to its source while using AI to accelerate synthesis.

**Chain:** manage sources in Zotero -> pull metadata and citations with **Zotero Integration** and **Citations** -> annotate PDFs and EPUBs in **Annotator** -> recover text from scans and screenshots with **Text Extractor** -> keep frontmatter consistent with **Linter** -> plot results with **Charts**. Verify every citation against its source before you draft.

- [Zotero Integration](https://github.com/obsidian-community/obsidian-zotero-integration) - Insert and import citations, bibliographies, notes, and PDF annotations from Zotero.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-zotero-desktop-connector)
- [Citations](https://github.com/hans/obsidian-citation-plugin) - Automatically search and insert citations from a Zotero library.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-citation-plugin)
- [Annotator](https://github.com/elias-sundqvist/obsidian-annotator) - Read and annotate PDFs and EPUB files.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-annotator)
- [Text Extractor](https://github.com/scambier/obsidian-text-extractor) - A (companion) plugin to facilitate the extraction of text from images (OCR) and PDFs.
  [⚡ Open](https://obsidian.md/plugins?id=text-extractor)
- [Linter](https://github.com/platers/obsidian-linter) - Format and style your notes. Linter can be used to format YAML tags, aliases, arrays, and metadata; footnotes; headings; spacing; math blocks; regular Markdown contents like list, italics, and bold styles; and more with the use of custom rule options.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-linter)
- [Charts](https://github.com/phibr0/obsidian-charts) - Easily create interactive charts in your notes.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-charts)

---

### Developers & Technical Authors

> Turn executable notes into reviewable, maintainable, publishable technical assets.

**Chain:** document decisions and commands as small notes -> style listings with **Code Styler** and draw flows with **Mermaid Tools** -> run shell jobs from **Terminal** -> paste references with **Auto Link Title** -> generate a **Table of Contents** for long documents. Treat generated text as a draft and keep tests beside examples.

- [Table of Contents](https://github.com/hipstersmoothie/obsidian-plugin-toc) - Create a table of contents for a note.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-plugin-toc)
- [Code Styler](https://github.com/mayurankv/Obsidian-Code-Styler) - Style codeblocks and inline code in reading view and editing view.
  [⚡ Open](https://obsidian.md/plugins?id=code-styler)
- [Mermaid Tools](https://github.com/dartungar/obsidian-mermaid) - Improved Mermaid.js experience: visual toolbar with common elements and more.
  [⚡ Open](https://obsidian.md/plugins?id=mermaid-tools)
- [Terminal](https://github.com/polyipseity/obsidian-terminal) - Integrate consoles, shells, and terminals.
  [⚡ Open](https://obsidian.md/plugins?id=terminal)
- [Auto Link Title](https://github.com/zolrath/obsidian-auto-link-title) - Automatically fetches the titles of links from the web.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-auto-link-title)

> **Mermaid** diagrams and **Canvas** are core features — check them before adding a diagramming plugin. **Advanced URI** and **Local REST API** are what let scripts, Shortcuts, and agents drive your vault from outside.

---

### Writers & Content Creators

> Connect idea capture, long-form structure, media handling, and multi-channel publishing.

**Chain:** capture fragments on any device -> draft one file per chapter -> format as you type with **Easy Typing** and **Editing Toolbar** -> watch length in **Better Word Count** -> mark passages with **Highlightr** -> follow the structure in **Quiet Outline** -> resize media with **Image Converter** before you publish. Keep source notes separate from the publishable draft.

- [Editing Toolbar](https://github.com/pkm-er/obsidian-editing-toolbar) - The Editing Toolbar is modified from cMenu, which provides more powerful customization settings and has many built-in editing commands to be a MS Word-like toolbar editing experience.
  [⚡ Open](https://obsidian.md/plugins?id=editing-toolbar)
- [Better Word Count](https://github.com/lukeleppan/better-word-count) - Count the words of selected text in the editor.
  [⚡ Open](https://obsidian.md/plugins?id=better-word-count)
- [Highlightr](https://github.com/chetachiezikeuzor/Highlightr-Plugin) - A minimal and aesthetically pleasing highlighting menu that makes color-coded highlighting much easier with a configurable assortment of highlight colors.
  [⚡ Open](https://obsidian.md/plugins?id=highlightr-plugin)
- [Quiet Outline](https://github.com/guopenghui/obsidian-quiet-outline) - Make outline quiet and more powerful, including no-auto-expand, rendering heading as Markdown, and search support.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-quiet-outline)
- [Easy Typing](https://github.com/yaozhuwa/easy-typing-obsidian) - Auto format when typing.
  [⚡ Open](https://obsidian.md/plugins?id=easy-typing-obsidian)
- [Image Converter](https://github.com/xryul/obsidian-image-converter) - Convert, compress, resize, annotate, markup, draw, crop, rotate, flip, align, drag-resize, rename with variables, and batch process images: WEBP, JPG, PNG, HEIC, TIF.
  [⚡ Open](https://obsidian.md/plugins?id=image-converter)

> **Readwise Official** requires a paid Readwise subscription. **Image Converter** rewrites files in place, so keep a backup before a bulk resize.

---

### Project Managers & Knowledge Workers

> Keep meetings, commitments, deadlines, and project status in one searchable system.

**Chain:** create consistent meeting notes with **Templater** -> parse dates with **Natural Language Dates** -> lay out milestones in **Kanban** and **Calendar** -> track delivery in **dotpm** and set **Reminder** nudges on commitments -> run a Friday review and archive decisions with links to the source meeting.

- [Templater](https://github.com/silentvoid13/Templater) - Create and use dynamic templates.
  [⚡ Open](https://obsidian.md/plugins?id=templater-obsidian)
- [Natural Language Dates](https://github.com/obsidian-community/nldates) - Create date-links based on natural language.
  [⚡ Open](https://obsidian.md/plugins?id=nldates-obsidian)
- [Kanban](https://github.com/obsidian-community/obsidian-kanban) - Create Markdown-backed Kanban boards.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-kanban)
- [Calendar](https://github.com/liamcain/obsidian-calendar-plugin) - Explore your daily notes.
  [⚡ Open](https://obsidian.md/plugins?id=calendar)
- [dotpm](https://github.com/dotpm/obsidian-pm) - Full-featured task and project management: stunning Gantt charts, Kanban boards, Table views, customizable fields, due date notifications, dependancies.
  [⚡ Open](https://obsidian.md/plugins?id=project-manager)
- [Reminder](https://github.com/uphy/obsidian-reminder) - Manage Markdown TODOs with reminder.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-reminder-plugin)

> A Notion-style database view is now core: start with **Bases** rather than a community plugin.

---

### Visual Thinkers & Designers

> Organize complex problems spatially first, then turn durable insights into reusable text.

**Chain:** diverge on **Advanced Canvas** -> turn the stable nodes into a structure you can navigate with **ExcaliBrain** -> make the vault scannable with **Iconize**, **Banners**, and **File Color** -> lay out reference pages with **Multi-Column Markdown**. Link every visual artifact to a decision or brief.

- [Advanced Canvas](https://github.com/developer-mike/obsidian-advanced-canvas) - Supercharge your canvas experience. Create presentations, flowcharts and more.
  [⚡ Open](https://obsidian.md/plugins?id=advanced-canvas)
- [ExcaliBrain](https://github.com/zsviczian/excalibrain) - An interactive, structured mind-map of your Obsidian vault.
  [⚡ Open](https://obsidian.md/plugins?id=excalibrain)
- [Iconize](https://github.com/florianwoelki/obsidian-iconize) - Add icons to anything in Obsidian, including files, folders, and text.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-icon-folder)
- [Banners](https://github.com/noatpad/obsidian-banners) - Add banner images to your notes!.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-banners)
- [File Color](https://github.com/ecustic/obsidian-file-color) - Set colors on folders and files in the file tree.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-file-color)
- [Multi-Column Markdown](https://github.com/ckrobinson/multi-column-markdown) - Create Markdown documents with multiple columns of content viewable in reading mode.
  [⚡ Open](https://obsidian.md/plugins?id=multi-column-markdown)

> **Excalidraw** also ships a community script library (flowcharts, palettes, import helpers) — enable it from the plugin's settings instead of installing another plugin.

---

### Language & Media Learners

> Capture, explain, and review vocabulary and expressions in authentic context.

**Chain:** watch or listen with **Media Extended** -> pull timestamped transcripts from **YTranscript** or **PodNotes** -> look up words in **Dictionary** -> keep the source page open beside your notes with **Custom Frames** -> import highlights from **Weread**. Revisit the exact clip whenever an example is difficult.

- [YTranscript](https://github.com/lstrzepek/obsidian-yt-transcript) - Easily fetch transcription for any YouTube video.
  [⚡ Open](https://obsidian.md/plugins?id=ytranscript)
- [PodNotes](https://github.com/chhoumann/PodNotes) - Write notes on podcasts with ease.
  [⚡ Open](https://obsidian.md/plugins?id=podnotes)
- [Media Extended](https://github.com/aidenlx/media-extended) - Integrate, manage video or audio directly in your notes, with enhanced playback and timestamp support. (Closed source).
  [⚡ Open](https://obsidian.md/plugins?id=media-extended)
- [Dictionary](https://github.com/phibr0/obsidian-dictionary) - A multilingual dictionary that shows word definitions in the sidebar and popover synonyms.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-dictionary-plugin)
- [Custom Frames](https://github.com/ellpeck/ObsidianCustomFrames) - Turn web apps into panes using iframes with custom styling. Also comes with presets for Google Keep, Todoist and more.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-custom-frames)
- [Weread](https://github.com/zhaohongxuan/obsidian-weread-plugin) - Sync Tencent Weread highlights and annotations.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-weread-plugin)

---

### Automation Builders & Power Users

> Use structured metadata and composable automation to turn Obsidian into a personal operations hub.

**Chain:** give notes interactive fields with **Meta Bind** -> bind repeatable actions to **Buttons** -> assemble dashboards in **make.md** -> find anything instantly with **Soma Search** -> let **Claudian** and **Smart Composer** work against that context. Start with one dashboard, measure friction, and add complexity only when it removes a real step.

- [Meta Bind](https://github.com/mprojectscode/obsidian-meta-bind-plugin) - Make your notes interactive with inline input fields, metadata displays, and buttons.
  [⚡ Open](https://obsidian.md/plugins?id=obsidian-meta-bind-plugin)
- [Buttons](https://github.com/shabegom/buttons) - Create Buttons in your notes to run commands, open links, and insert templates.
  [⚡ Open](https://obsidian.md/plugins?id=buttons)
- [make.md](https://github.com/make-md/makemd) - Build custom, code-free workspaces using databases, visual views, and relational trackers.
  [⚡ Open](https://obsidian.md/plugins?id=make-md)
- [Soma Search](https://github.com/awesomedog/obsidian-soma-search) - Local-first AI search for Obsidian. Semantic, keyword & hybrid search across notes, PDFs, scanned docs, images (OCR + vision) and audio — 100% offline and private, powered by Soma.
  [⚡ Open](https://obsidian.md/plugins?id=soma-search)
- [Claudian](https://github.com/yishentu/claudian) - Embeds Claude Code/Codex and other local Agents as AI collaborators in your vault.
  [⚡ Open](https://obsidian.md/plugins?id=realclaudian)
- [Smart Composer](https://github.com/glowingjade/obsidian-smart-composer) - AI chat with note context, smart writing assistance, and one-click edits for your vault.
  [⚡ Open](https://obsidian.md/plugins?id=smart-composer)

> **make.md** is a heavy, opinionated rework of the interface — try it on a throwaway vault first. For sync, choose one mechanism per vault, never stack multiple sync plugins.

---

## Workflows

These are patterns to adapt, not bundles to install unchanged.

<details open>
<summary><b>Research</b></summary>

Capture citations and PDF annotations -> organize with Properties -> query literature notes -> retain key claims -> export when needed.

</details>

<details>
<summary><b>Personal productivity</b></summary>

Use Daily notes as an inbox -> keep one Markdown task format -> review on a board or calendar -> add habits only if the review loop needs them.

</details>

<details>
<summary><b>Long-form writing</b></summary>

Scaffold the manuscript -> reduce interface noise -> collect and mark up sources -> clean pasted text -> export to the required format.

</details>

<details>
<summary><b>AI-assisted work</b></summary>

Decide what may leave the vault -> retrieve only the context needed -> use AI for bounded transformations -> keep a versioned backup when an agent can write files.

</details>

---

## Discover New Plugins

This automated table shows newly registered community plugins ranked by downloads. Anything already listed in the curated catalog or a playbook is skipped, so the table only surfaces names you have not seen above. It is a discovery signal, not a recommendation or security review.

<sub>📈 **Lookback Period**: Past 120 Days (2026-06-03 ~ 2026-10-01) | **New Plugins Tracked**: 4,003 | **Last Refreshed**: `2026-10-01`</sub>

<!-- AUTO-GENERATED-CONTENT:START (rising-stars) — do not edit this table by hand -->

| Rank  | Plugin                                                                                                        | Downloads    | Description                                                                                     | Install                                                                     |
| ----- | ------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 🥇 1  | [JSON-CSV Importer](https://github.com/farling42/obsidian-import-json)                                        | 📥 **79.3K** | Import a JSON file containing an array of data, creating notes from a Handlebars template file. | [⚡ Open](https://obsidian.md/plugins?id=obsidian-import-json)               |
| 🥈 2  | [Dynamic Views](https://github.com/churnish/dynamic-views)                                                    | 📥 **77.9K** | Elegant grid and masonry card views for Bases.                                                  | [⚡ Open](https://obsidian.md/plugins?id=dynamic-views)                      |
| 🥉 3  | [Sort and Permute lines](https://github.com/vinzent03/obsidian-sort-and-permute-lines)                        | 📥 **73.3K** | Sort and Permute lines in whole file or selection.                                              | [⚡ Open](https://obsidian.md/plugins?id=obsidian-sort-and-permute-lines)    |
| `#4`  | [April Automatic Timelines](https://github.com/april-gras/obsidian-auto-timelines)                            | 📥 **63.5K** | Simple timeline generator for story tellers.                                                    | [⚡ Open](https://obsidian.md/plugins?id=aprils-automatic-timelines)         |
| `#5`  | [Hot Reload](https://github.com/pjeby/hot-reload)                                                             | 📥 **60.1K** | Automatically reload in-development plugins when their files are changed                        | [⚡ Open](https://obsidian.md/plugins?id=hot-reload)                         |
| `#6`  | [draw.io](https://github.com/somesanity/draw-io-obsidian)                                                     | 📥 **55.7K** | Create and edit diagrams with draw.io (diagrams.net), locally and offline.                      | [⚡ Open](https://obsidian.md/plugins?id=drawio)                             |
| `#7`  | [Chinese Market](https://github.com/miaoziguan/obsidian-chinese-plugin-market)                                | 📥 **54.6K** | 面向中文用户的 Obsidian 社区插件搜索工具：输入关键词即可检索并展示翻译后的插件卡片，支持 AI 语义 / 名称 / 作者搜索。                            | [⚡ Open](https://obsidian.md/plugins?id=chinese-plugin-market)              |
| `#8`  | [Full Calendar Remastered](https://github.com/obsidian-full-calendar-remastered/plugin-full-calendar)         | 📥 **47.0K** | Complete Calendar HUB experience. Work with all your calendars in one place. Analyze your ti... | [⚡ Open](https://obsidian.md/plugins?id=full-calendar-remastered)           |
| `#9`  | [Hearth](https://github.com/ondreu/Hearth)                                                                    | 📥 **46.3K** | A beautiful, heavily customizable home screen — dashboard, launchpad, mission control, homes... | [⚡ Open](https://obsidian.md/plugins?id=hearth)                             |
| `#10` | [Smart Chat](https://github.com/brianpetro/smart-chatgpt-obsidian)                                            | 📥 **44.1K** | Integrate OpenAI's ChatGPT seamlessly in notes. Automatically saves links, allows marking th... | [⚡ Open](https://obsidian.md/plugins?id=smart-chatgpt)                      |
| `#11` | [Sync Engine](https://github.com/hesprs/sync-engine)                                                          | 📥 **42.2K** | The extensible vault synchronization engine: Fast · Free · Reliable. Supports WebDAV, S3, an... | [⚡ Open](https://obsidian.md/plugins?id=sync-engine)                        |
| `#12` | [Markdown Tabs](https://github.com/xhuajin/obsidian-tabs)                                                     | 📥 **40.8K** | Create tabs in your notes.                                                                      | [⚡ Open](https://obsidian.md/plugins?id=tabs)                               |
| `#13` | [Excalidraw Extras](https://github.com/zsviczian/obsidian-excalidraw-extras)                                  | 📥 **40.3K** | Companion plugin for Excalidraw high-privilege and large components.                            | [⚡ Open](https://obsidian.md/plugins?id=excalidraw-extras)                  |
| `#14` | [Imagine](https://github.com/albusguo/albus-imagine)                                                          | 📥 **34.3K** | A comprehensive image management plugin for managing, inserting, resizing, viewing, and batc... | [⚡ Open](https://obsidian.md/plugins?id=albus-imagine)                      |
| `#15` | [Unhide](https://github.com/polyipseity/obsidian-unhide)                                                      | 📥 **34.2K** | (formerly Show Hidden Files) Unhide hidden files, like dotfiles, in Obsidian.                   | [⚡ Open](https://obsidian.md/plugins?id=unhide)                             |
| `#16` | [PanGu](https://github.com/natumsol/obsidian-pangu)                                                           | 📥 **28.9K** | Add spaces between Chinese characters and English alphabet. A boon for typographically compu... | [⚡ Open](https://obsidian.md/plugins?id=obsidian-pangu)                     |
| `#17` | [Journalit](https://github.com/cursivez/journalit)                                                            | 📥 **28.1K** | Trading journal with analytics, prop-firm tracking, broker imports and sync, reviews, and cu... | [⚡ Open](https://obsidian.md/plugins?id=journalit)                          |
| `#18` | [Notion Bases](https://github.com/bgarciamoura/obsidian-notion-bases-plugin)                                  | 📥 **25.0K** | Turn any folder into a database — table, kanban board, gallery, calendar, timeline and list ... | [⚡ Open](https://obsidian.md/plugins?id=notion-bases)                       |
| `#19` | [Simple mind map](https://github.com/wanglin2/obsidian-simplemindmap)                                         | 📥 **23.2K** | A mind map that combines aesthetics and functionality. 一个颜值与功能并存的思维导图。                          | [⚡ Open](https://obsidian.md/plugins?id=simple-mind-map)                    |
| `#20` | [Book Reader](https://github.com/swayinfo/elton-reader)                                                       | 📥 **21.6K** | Read EPUB, FB2 and PDF books with highlights, notes and vault-synced reading progress.          | [⚡ Open](https://obsidian.md/plugins?id=elton-reader-books)                 |
| `#21` | [WeSight](https://github.com/freestylefly/wesight-obsidian)                                                   | 📥 **21.4K** | Run Claude Code, Codex, and OpenCode as local AI collaborators inside your vault.               | [⚡ Open](https://obsidian.md/plugins?id=wesight)                            |
| `#22` | [MP Publisher](https://github.com/joeytoday/obsidian-mp-publisher)                                            | 📥 **19.1K** | Preview with custom CSS themes and publish articles to WeChat Official Accounts with one click. | [⚡ Open](https://obsidian.md/plugins?id=mp-publisher)                       |
| `#23` | [Confluence Integration](https://github.com/markdown-confluence/obsidian-integration)                         | 📥 **18.1K** | Publish Markdown content to Atlassian Confluence. It supports some Obsidian Markdown extensi... | [⚡ Open](https://obsidian.md/plugins?id=confluence-integration)             |
| `#24` | [OneDrive Sync](https://github.com/jeffsteinbok/obsidian-onedrive)                                            | 📥 **18.0K** | Sync your Obsidian vault with OneDrive Personal/Consumer                                        | [⚡ Open](https://obsidian.md/plugins?id=onedrive-sync)                      |
| `#25` | [NanoBanana PRO](https://github.com/reallygood83/nanobanana-pro-obsidian)                                     | 📥 **16.4K** | Generate Knowledge Posters (infographics) from your notes using AI. Supports OpenAI, Gemini,... | [⚡ Open](https://obsidian.md/plugins?id=nanobanana-pro)                     |
| `#26` | [Nextcloud Sync](https://github.com/siosig/obsidian-nextcloudsync)                                            | 📥 **15.8K** | Bidirectional sync between Obsidian and Nextcloud using hash-based change detection.            | [⚡ Open](https://obsidian.md/plugins?id=nextcloud-sync)                     |
| `#27` | [CMDS Eagle](https://github.com/johnfkoo951/cmds-eagle)                                                       | 📥 **14.5K** | Connect Eagle asset libraries to your vault. Search and embed assets in notes, import files ... | [⚡ Open](https://obsidian.md/plugins?id=cmds-eagle)                         |
| `#28` | [Advanced Rename and Delete Handler](https://github.com/mnaoumov/obsidian-advanced-rename-and-delete-handler) | 📥 **13.7K** | Handles renames and deletes for the whole vault in one place: updates links, moves attachmen... | [⚡ Open](https://obsidian.md/plugins?id=advanced-rename-and-delete-handler) |
| `#29` | [EasySync](https://github.com/jiaoyingxing/easy-sync)                                                         | 📥 **13.3K** | Two-way OneDrive sync for Obsidian, with conflict safeguards, mobile support, and optional s... | [⚡ Open](https://obsidian.md/plugins?id=easy-sync)                          |
| `#30` | [RavenHogwarts Toolkit](https://github.com/ravenhogwarts/obsidian-ravenhogwarts-toolkit)                      | 📥 **12.8K** | A personal toolkit plugin (OTK) that integrates various utilities, designed to enhance perso... | [⚡ Open](https://obsidian.md/plugins?id=ravenhogwarts-toolkit)              |
| `#31` | [Todoist Board](https://github.com/propranolol11/todoist-board)                                               | 📥 **12.5K** | A Todoist tasks board with sidebar and embedded views. Full 2-way sync.                         | [⚡ Open](https://obsidian.md/plugins?id=todoist-board)                      |
| `#32` | [Resojot](https://github.com/jiaoyingxing/resojot)                                                            | 📥 **12.0K** | Capture voice notes in Obsidian, write them into Markdown, and transcribe them with local or... | [⚡ Open](https://obsidian.md/plugins?id=resojot)                            |
| `#33` | [Galaxy View](https://github.com/longwind1984/galaxy-view)                                                    | 📥 **11.2K** | Cinematic 3D graph view of your vault — fly through your notes like NASA Eyes.                  | [⚡ Open](https://obsidian.md/plugins?id=galaxy-view)                        |
| `#34` | [Smart Gantt](https://github.com/nhannht/obsidian-smart-gantt)                                                | 📥 **11.1K** | Generate Gantt charts from your tasks.                                                          | [⚡ Open](https://obsidian.md/plugins?id=smart-gantt)                        |
| `#35` | [Hermes Agent](https://github.com/jsun2020/hermes-agent-obsidian-plugin)                                      | 📥 **10.7K** | Chat with a locally installed Hermes Agent from your vault. Send the current note or selecti... | [⚡ Open](https://obsidian.md/plugins?id=hermes-agent)                       |
| `#36` | [Journal Partner](https://github.com/zhaohongxuan/journal-partner)                                            | 📥 **10.5K** | Highlight timestamps in your Journal section, capture quick notes, images, and audio from a ... | [⚡ Open](https://obsidian.md/plugins?id=journal-partner)                    |
| `#37` | [Style Manager](https://github.com/emarpiee/obsidian-style-manager)                                           | 📥 **10.4K** | Provides advanced controls for managing themes, CSS snippets, and style settings. Transforms... | [⚡ Open](https://obsidian.md/plugins?id=style-manager)                      |
| `#38` | [Better Paste](https://github.com/johansan/better-paste)                                                      | 📥 **10.2K** | Removes tracking from links, fetches page titles, and cleans up pasted text from AI chats, t... | [⚡ Open](https://obsidian.md/plugins?id=better-paste)                       |
| `#39` | [Cursor-Smith](https://github.com/sadsnake1/cursor-smith)                                                     | 📥 **9,907** | Forge your cursor with the most advanced cursor engine there is!                                | [⚡ Open](https://obsidian.md/plugins?id=cursor-smith)                       |
| `#40` | [Discourse Graph](https://github.com/discoursegraphs/discourse-graph-obsidian)                                | 📥 **9,812** | Add semantic structure to your notes with the Discourse Graph protocol.                         | [⚡ Open](https://obsidian.md/plugins?id=discourse-graphs)                   |
| `#41` | [Bases Board](https://github.com/flowing-abyss/obsidian-bases-board)                                          | 📥 **9,572** | Interactive board view for bases, use as Kanban or Gallery, with grouping for rows and columns. | [⚡ Open](https://obsidian.md/plugins?id=bases-board)                        |
| `#42` | [Telegram Sidebar](https://github.com/reallygood83/teledian)                                                  | 📥 **8,953** | Embed Telegram Web in Obsidian sidebar. Chat with bots and contacts without leaving your vault. | [⚡ Open](https://obsidian.md/plugins?id=telegram-sidebar)                   |
| `#43` | [Mini Notes](https://github.com/rknastenka/obsidian-mini-notes)                                               | 📥 **8,891** | Your quick thoughts, beautifully displayed, with a Google Keep-style colorful card-based view.  | [⚡ Open](https://obsidian.md/plugins?id=mini-notes)                         |
| `#44` | [Calendar for Daily Notes](https://github.com/xryul/calendar-for-daily-notes)                                 | 📥 **8,631** | Calendar for daily notes with grouped lists, created-on-day notes and attachments, color tag... | [⚡ Open](https://obsidian.md/plugins?id=calendar-for-daily-notes)           |
| `#45` | [Mobile PDF Exporter](https://github.com/arias007/obsidian-mobile-pdf-exporter)                               | 📥 **8,591** | One-click selectable preview PDF(docx,pptx,png,html) export for Obsidian mobile and desktop.    | [⚡ Open](https://obsidian.md/plugins?id=mobile-pdf-exporter)                |
| `#46` | [Make It Rain](https://github.com/frostmute/make-it-rain)                                                     | 📥 **8,563** | Pull Raindrop.io bookmarks, highlights, and attachments into Markdown notes with rich metada... | [⚡ Open](https://obsidian.md/plugins?id=make-it-rain)                       |
| `#47` | [Vim Motions](https://github.com/saberzero1/motions)                                                          | 📥 **8,386** | Full Neovim experience inside Obsidian with Lua scripting, Flash/EasyMotion jumps, Telescope... | [⚡ Open](https://obsidian.md/plugins?id=vim-motions)                        |
| `#48` | [Pseudo Mica](https://github.com/svnaxis/obsidian-pseudo-mica)                                                | 📥 **8,320** | Customize translucent window effects on Windows and macOS.                                      | [⚡ Open](https://obsidian.md/plugins?id=pseudo-mica)                        |
| `#49` | [Projects Plus](https://github.com/parkpavel/obs-projects-plus)                                               | 📥 **8,119** | Turn your notes into projects with dashboards, tables, boards, calendars and galleries built... | [⚡ Open](https://obsidian.md/plugins?id=obs-projects-plus)                  |
| `#50` | [Objects](https://github.com/finn-kraemer/obsidian-objects)                                                   | 📥 **7,765** | Instantly create and organize notes from templates using customizable @-triggers without bre... | [⚡ Open](https://obsidian.md/plugins?id=objects)                            |

<!-- AUTO-GENERATED-CONTENT:END -->

Use the **Open** link beside an entry, or search for its name in `Settings -> Community plugins -> Browse`. For beta builds, use the plugin's Releases page or [BRAT](https://github.com/TfTHacker/obsidian42-brat).

The builder compares the official registry with a lookback snapshot and refreshes this table monthly. Downloads include updates and reinstalls, so they measure momentum rather than quality.

---

## Resources

### Learn

- [**Obsidian Help**](https://help.obsidian.md/) - Official documentation for core features, syntax, and settings.
- [**Obsidian Hub**](https://publish.obsidian.md/hub/) - Community guides, comparisons, and vault examples.
- [**Obsidian Roadmap**](https://obsidian.md/roadmap) - Upcoming core features that may replace a plugin.

### Publish and Connect

- [**Obsidian Web Clipper**](https://obsidian.md/clipper) - First-party web capture.
- [**Obsidian Sync**](https://obsidian.md/sync) - Paid synchronization.
- [**Obsidian Publish**](https://obsidian.md/publish) - Paid hosting for notes.
- [**Quartz**](https://quartz.jzhao.xyz/) - Static-site publishing for Obsidian-flavored Markdown.
- [**Pandoc**](https://pandoc.org/) - Document conversion for export workflows.
- [**Zotero**](https://www.zotero.org/) - Reference management for research notes.
- [**Syncthing**](https://syncthing.net/) - Peer-to-peer file synchronization.

### Popular Themes

- [**Minimal**](https://github.com/kepano/obsidian-minimal) - Clean and distraction-free theme.
  [⚡ Open](https://community.obsidian.md/themes/minimal)
- [**Catppuccin**](https://github.com/catppuccin/obsidian) - Soothing pastel dark and light palette.
  [⚡ Open](https://community.obsidian.md/themes/catppuccin)
- [**Border**](https://github.com/akifyss/obsidian-border) - Crisp, highly configurable interface.
  [⚡ Open](https://community.obsidian.md/themes/border)
- [**Blue Topaz**](https://github.com/pkm-er/Blue-Topaz_Obsidian-css) - Feature-rich blue theme.
  [⚡ Open](https://community.obsidian.md/themes/blue-topaz)
- [**Baseline**](https://github.com/aaaaalexis/obsidian-baseline) - Clean, modern theme with strong typography.
  [⚡ Open](https://community.obsidian.md/themes/baseline)
- [**Things**](https://github.com/colineckert/obsidian-things) - Polished productivity-focused interface.
  [⚡ Open](https://community.obsidian.md/themes/things)
- [**Prism**](https://github.com/damiankorcz/Prism-Theme) - Colorful, modern theme with flexible accents.
  [⚡ Open](https://community.obsidian.md/themes/prism)
- [**ITS Theme**](https://github.com/slrvb/Obsidian--ITS-Theme) - Extensive layout and callout customization.
  [⚡ Open](https://community.obsidian.md/themes/its-theme)

> 💡 Themes are installed via `Settings → Appearance → Themes → Manage`, and most expose knobs through **Style Settings**. Use the **Open** link to preview one, or browse everything in the official [theme gallery](https://community.obsidian.md/themes).

### Vault Starters and Methodologies

- [**LYT Kit (Linking Your Thinking)**](https://www.linkingyourthinking.com/) - Nick Milo's popular Maps of Content (MOC) framework.
- [**PARA Method Starter**](https://fortelabs.com/blog/para/) - Projects, Areas, Resources, Archives structure by Tiago Forte.
- [**Zettelkasten Starter Vault**](https://zettelkasten.de/) - Classic slip-box note-taking methodology.
- [**Johnny.Decimal**](https://johnnydecimal.com/) - Systematic decimal-based organizational scheme.

> ⚖️ **Warning about starter vaults:** they arrive pre-loaded with someone else's plugins and folder logic. Borrow the *ideas*, not necessarily the `.obsidian` folder — inherited configs are the hardest kind to debug.

### Community Hubs

- [**Obsidian Official Forum**](https://forum.obsidian.md/) - Official hub for release announcements and technical discussions.
- [**Obsidian Discord**](https://discord.gg/obsidianmd) - Real-time chat community with over 100,000 active members.
- [**Reddit r/ObsidianMD**](https://www.reddit.com/r/ObsidianMD/) - Global community sharing vaults, workflows, and tips.
- [**PKMer Community**](https://pkmer.cn/) - Knowledge management and plugin tutorial community.

---

## FAQ

<details>
<summary><b>How many plugins should I install?</b></summary>

There is no target number. Add the smallest tool that removes a repeated problem, then remove anything you no longer use or understand.

</details>

<details>
<summary><b>Are community plugins safe?</b></summary>

They are not security-audited and have access to your vault and the network. Read the source, understand data flow, and keep backups.

</details>

<details>
<summary><b>Which database view should I use?</b></summary>

Start with Bases. Use Dataview for a mature query language. Consider Datacore only when you need reactive, performance-heavy views and accept its beta status.

</details>

<details>
<summary><b>What is a sensible sync setup?</b></summary>

Use one synchronization mechanism per vault and keep a separate, versioned backup. Sync mirrors changes; it does not replace history.

</details>

<details>
<summary><b>Do these plugins work on mobile?</b></summary>

Many do, but tools that invoke Git, Pandoc, shells, or local agents often require desktop. Check the official compatibility flag.

</details>

---

## Contributing

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) for the data model, inclusion criteria, and build workflow. Edit the source files, then regenerate the root README.

---

## Footnotes

This is an independent, community-run project and is not affiliated with Obsidian or Dynalist Inc. Listings are informational; evaluate security, privacy, compatibility, and licensing yourself. Linked projects remain under their own licenses.
