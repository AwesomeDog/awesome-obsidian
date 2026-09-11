# Contributing to Awesome Obsidian

Thank you for helping keep this map useful for the Obsidian community.

This repository uses a **data-driven build system**. You do **not** need to manually format complex Markdown tables or look up GitHub repository links.

---

## How to Add or Move a Plugin

1. Fork this repository and create a branch (`git checkout -b add-my-plugin`).
2. Open [`data/curated.json`](data/curated.json).
3. Find the single lifecycle stage where the plugin removes the most friction:
   - `0. Getting Started`
   - `1. Capture & Ingestion`
   - `2. Writing & Editing`
   - `3. Organizing & Metadata`
   - `4. Linking & Discovery`
   - `5. Data Views`
   - `6. Tasks, Habits & Review`
   - `7. Output & Publishing`
   - `8. Aesthetics & Interface`
   - `9. Vault Maintenance & Sync`
   - `10. Automation & AI`
4. Add the plugin's official **ID** into the section's `"plugins"` list:
   ```json
   "plugins": [
     "existing-plugin-id",
     "your-new-plugin-id"
   ]
   ```
5. Run the build script to update the `README.md`:
   ```bash
   npx --yes prettier --write data/curated.json
   python scripts/build.py
   npx awesome-lint
   # if rate limited:
   GITHUB_TOKEN=$(gh auth token) python scripts/build.py
   ```
   *(The script uses cached data in `cache/` so it will complete in less than a second without hitting API limits.)*
6. Commit your changes and submit a Pull Request!

---

## 📌 Inclusion Criteria

An entry earns a spot in a curated category only if it is:

1. **Actively maintained** — a release or meaningful commit within the last ~12 months, and no archived repository.
2. **Widely trusted** — meaningful adoption (typically 10k+ downloads) *or* a clearly best-in-class solution for a niche with no alternative.
3. **Non-redundant with core** — it must do something Obsidian's built-in features genuinely cannot.
4. **Non-redundant within the list** — each lifecycle category is capped at six picks; a newcomer generally has to *replace* an incumbent rather than pile on.
5. **One plugin per category** — place each plugin in the single stage of the lifecycle where it delivers the most value. (Duplicates are allowed only when a plugin is genuinely dual-purpose, as with Dataview.)

`data/curated.json` also holds a second, independent axis: **`playbooks`** — short starter kits grouped by *role* (Students, Developers, Writers, ...) instead of by job. Plugins repeat between `sections` and `playbooks` on purpose, so rule 5 applies only within `sections`. A playbook should stay short: **change it when a role's recommended kit changes, not every time a plugin is added to a lifecycle stage.**
6. **Problem-solving** — plugins that remove a real workflow bottleneck beat cosmetic tweaks, which are usually better done as a CSS snippet.
7. **Open-source & safely licensed** — a public repository with a readable license.
8. **Data-respectful** — no undisclosed telemetry, no lock-in of your Markdown into a proprietary format.
9. **Compatible with recent Obsidian versions** (v1.5+; Bases-based tools require v1.9+).

The **Discover New Plugins** table in the README intentionally applies *none* of these judgments: it is a raw popularity signal for plugins younger than one year, published for discovery only. **Inclusion there is not an endorsement.**

---

## ✅ Pull Request Checklist

1. **Edit data, not prose.** Never hand-edit generated sections of `README.md` (they are wrapped in `AUTO-GENERATED-CONTENT` markers) — change [`data/curated.json`](data/curated.json) instead.
2. **One plugin per pull request**, with a title like `add: <plugin-name> to Capture & Ingestion`.
3. **Justify it against the [Inclusion Criteria](#-inclusion-criteria)** in the PR description: name the user problem, explain why core Obsidian is not enough, and say which existing entry it replaces or complements.
4. **Confirm health:** maintained within ~12 months, repository not archived, license present, no undisclosed telemetry.
5. **Place it in exactly one lifecycle stage.** Duplicate entries are allowed only when the plugin has a genuinely distinct job in each stage.
6. **Run the build locally** if you can, so the rendered diff is reviewable.
7. **Format `data/curated.json`** with `npx --yes prettier --write data/curated.json` so the diff shows exactly one added line per plugin.

---

## 🧹 Other Ways to Help

- **Report rot:** dead links, renamed repos, archived plugins, or entries superseded by core features.
- **Improve the meta:** FAQ answers, workflow examples, and translations.
- **Challenge an entry.** Removals are as valuable as additions — this list stays useful by staying short.

---

## 📝 Editing the Static Text

All prose and layout live in a single file: [`data/README.template.md`](data/README.template.md). Edit it directly and re-run the build — never edit the root `README.md`, it is overwritten on every build.

The `.template.md` suffix is deliberate: it keeps the two files distinguishable in an editor's fuzzy-finder, and stops GitHub from rendering the unreplaced `{{PLACEHOLDER}}` tokens as a landing page for `data/`.

The template defines the reader journey: start from core Obsidian, choose by job, inspect the curated catalog, then explore workflows and newly registered plugins. `data/curated.json` supplies the catalog data without deciding the order of the rest of the README.

`{{PLACEHOLDER}}` tokens are filled in automatically — `{{TOC_SECTIONS}}`, `{{TOC_PLAYBOOKS}}`, `{{RISING_SUMMARY}}`, `{{RISING_TABLE}}`, `{{SECTIONS}}`, `{{PLAYBOOKS}}`, `{{APPENDIX}}`. Don't remove them.

`data/curated.json` also accepts hand-written Markdown per section. Both `sections` and `playbooks` use the same fields, and `scripts/build.py` renders them with one shared function:

| Field | Where it renders |
| --- | --- |
| `sections[].intro` / `playbooks[].intro` | Between the section description and its plugin list |
| `sections[].outro` / `playbooks[].outro` | After the plugin list (tips, warnings, comparison tables) |
| `appendix.notes.<group>` | After the matching appendix group (`themes`, `templates`) |

Keep `playbooks[].intro` as the **workflow chain** for that role (capture -> ... -> output) and `playbooks[].outro` as the caveats — core-feature substitutes, paid dependencies, and plugins that must not be combined.

---

## 🧩 Awesome List Compliance

This repo is submitted to the [awesome](https://github.com/sindresorhus/awesome) index, so `README.md` must satisfy the official [list guidelines](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md). These are easy to break without noticing, precisely because `README.md` is generated — a template edit can silently violate three rules at once.

**Run the linter before opening a PR:**

```bash
npx awesome-lint
```

It also runs in CI ([`.github/workflows/lint.yml`](.github/workflows/lint.yml)) on every push and pull request that touches `README.md` or `data/`.

### Hard rules

| Rule | Detail |
| --- | --- |
| Heading | Title case, matches the repo name: `# Awesome Obsidian`. **No emoji.** |
| Top description | Describes the *subject*, not the list. ❌ "A curated list of awesome…" ✅ "Obsidian plugins, themes, and workflows for…" |
| `Contents` | Named `Contents` (not "Table of Contents"), must be the **first** section, at most one level of nesting, and must **not** list `Contributing` or `Footnotes`. |
| Badges | **No CI badges** — that includes GitHub Actions workflow badges. Awesome / PRs Welcome / community badges are fine. |
| License | **No license section in the readme** — GitHub shows it at the top of the repo already. The repo is **CC0 1.0 Universal**; awesome explicitly rejects code licenses like MIT, BSD, Apache or GPL. |
| Items | `- [Name](url) - Description.` — description starts with an uppercase letter and **ends with a period**. Curated plugins add an indented second line with the `⚡ Open` deep link; awesome-lint only checks the *first* paragraph of a list item, so the description itself must stay on the marker line. |
| Footnotes | Acknowledgements, disclaimer, star history and other non-essential content go in a single `Footnotes` section at the bottom. It is **not** in the TOC. |
| Contributing | The readme section (if any) sits at the top or bottom of the main content and is **not** in the TOC. |
| Topics | GitHub repo topics must include `awesome-list` and `awesome` — set in repo settings, not in a file. |

By contributing you agree to release your contribution into the public domain under [CC0 1.0 Universal](LICENSE).

### Where to fix a violation

Never edit `README.md` directly — it is regenerated by `scripts/build.py`. Fix the source instead:

| Violation | Fix in |
| --- | --- |
| Heading, description, badges, `Contents`, `Footnotes` | `data/README.template.md` |
| Entry layout, description wording | `scripts/build.py` → `list_item()` / `plugins_list()` |
| Section-level prose (tips, warnings, tables) | `data/curated.json` (`intro` / `outro`) |

---

## 🗂️ Repository Structure

```
.
├── README.md                  # ← generated: do not edit curated/auto sections by hand
├── data/
│   ├── curated.json           # ✍️ the only file most PRs need to touch
│   └── README.template.md     # README prose and layout template
├── scripts/                   # build engine: fetch stats, diff, render README
├── .github/
│   └── workflows/
│       ├── lint.yml           # awesome-lint on push / PR
│       └── update.yml         # monthly discovery table refresh
├── CONTRIBUTING.md
└── LICENSE                    # CC0 1.0 Universal
```

---

## Note on the "Discover New Plugins" Section

The `Discover New Plugins` section in `README.md` is computed automatically and refreshed on the 1st of every month by GitHub Actions. You don't need to manually update this section.

Pipeline details:

1. **Source Data**: Directly monitors the official [`obsidianmd/obsidian-releases`](https://github.com/obsidianmd/obsidian-releases) repository.
2. **Timeline Analysis**: Compares the current registry against the Git snapshot from 120 days ago (`--days`) to isolate newly released plugins.
3. **Download Metrics**: Real-time stats sourced from `community-plugin-stats.json`.
4. **Execution**: Automated monthly run via GitHub Actions (1st of the month, 03:00 UTC).
