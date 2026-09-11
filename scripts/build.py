#!/usr/bin/env python3
"""scripts/build.py — builds Awesome Obsidian.
Reads data/curated.json (plugin IDs only), caches the official registry in cache/, computes the
trending leaderboard for the lookback window, and fills the {{TOC_SECTIONS}} {{TOC_PLAYBOOKS}}
{{RISING_SUMMARY}} {{RISING_TABLE}} {{SECTIONS}} {{PLAYBOOKS}} {{APPENDIX}} tokens of
data/README.template.md.

The template owns the reading order. This script only supplies the two data-driven catalogs —
`sections` (organized by job) and `playbooks` (organized by role) — their one-level
table-of-contents links, and the automated discovery table. Both share one renderer.
"""
import os, re, sys, json, argparse, urllib.request
from datetime import datetime, timezone, timedelta

PLUGINS_URL = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json"
STATS_URL = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json"
COMMITS_API = "https://api.github.com/repos/obsidianmd/obsidian-releases/commits?path=community-plugins.json&until={until}&per_page=1"
HISTORIC_URL = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/{sha}/community-plugins.json"

def http_get_json(url, headers=None, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "Awesome-Obsidian-Builder/1.0", **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def ensure_cache_file(path, url, refresh=False, headers=None):
    """Return JSON from cache/ when present, otherwise download it and cache it."""
    if not refresh and os.path.exists(path):
        try:
            return load_json(path)
        except Exception as e:
            print(f"[!] Corrupted cache at {path}, re-fetching: {e}")
    print(f"[*] Downloading {url} -> {path}...")
    data = http_get_json(url, headers=headers)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return data

def get_historic_plugins(cache_dir, cutoff, refresh=False, token=None):
    """Registry snapshot as of `cutoff`. Fails loudly: without a trustworthy baseline the
    trending board is meaningless, so there is deliberately no fallback."""
    path = os.path.join(cache_dir, f"historic-plugins-{cutoff:%Y-%m-%d}.json")
    if not refresh and os.path.exists(path):
        try:
            return load_json(path)
        except Exception as e:
            print(f"[!] Corrupted cache at {path}, re-fetching: {e}")
    until = cutoff.strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        commits = http_get_json(COMMITS_API.format(until=until),
                                {"Authorization": f"Bearer {token}"} if token else None)
        if not commits:
            raise ValueError("no commit touched community-plugins.json in range")
        sha, date = commits[0]["sha"], commits[0]["commit"]["committer"]["date"]
        print(f"[*] Found git commit from {date}: {sha}")
        return ensure_cache_file(path, HISTORIC_URL.format(sha=sha), refresh=True)
    except Exception as e:
        sys.exit(f"[x] Fatal: could not resolve historic snapshot before {until}: {e}")

def slug(title):
    """GitHub's heading anchor: lowercase, drop punctuation, spaces -> hyphens.
    Consecutive hyphens are preserved (GitHub does not collapse them)."""
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-").strip("-")

def render_template(path, replacements):
    if not os.path.exists(path):
        sys.exit(f"[x] Fatal: template not found at {path}")
    text = open(path, encoding="utf-8").read()
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", value)
    return text

def clean_description(desc):
    """Drop Obsidian's boilerplate disclaimer, escape pipes, collapse whitespace."""
    if not desc:
        return ""
    desc = re.sub(r"\s*-\s*This plugin has not been manually reviewed by Obsidian staff\.?", "", desc, flags=re.I)
    return re.sub(r"\s+", " ", desc.replace("|", "\\|").strip())

def format_number(n):
    """1234 -> 1,234; 12000 -> 12.0K; 1200000 -> 1.2M."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 10_000:
        return f"{n / 1_000:.1f}K"
    return f"{n:,}" if n >= 1_000 else str(n)

def clip(desc, limit):
    """Shorten a description to fit a table cell; untouched unless it really overflows."""
    return desc[:limit] + "..." if len(desc) > limit + 3 else desc

def plugin_cells(p, desc_limit=110):
    """Cells shared by both tables: Plugin, Description, Install.

    The author used to be a column of its own; it is gone now — the plugin link already
    points at the repo, so the handle only added width and duplicate URLs.
    """
    repo = p.get("repo", "")
    return [
        f"[{p['name']}](https://github.com/{repo})" if repo else p["name"],
        clip(p.get("description", ""), desc_limit),
        f"[⚡ Open](https://obsidian.md/plugins?id={p['id']})",
    ]

def cell_length(text):
    """Length the way the linter measures it: UTF-16 code units, as JS `String#length` does.

    An emoji outside the BMP (🥇, 📥) is one character in Python but two code units in
    JavaScript, which is what `remark-lint-table-pipe-alignment` counts.
    """
    return len(text.encode("utf-16-le")) // 2

def table_rows(cols, cells_per_row):
    """Emit a table with its pipes aligned per column.

    awesome-lint's table-pipe-alignment rule measures a cell as `rightIndex - leftIndex`
    unless it is given a `stringLength` option, i.e. UTF-16 code units. Padding by display
    width or by Python's `len()` both drift on rows holding a medal or a 📥 and get flagged.
    """
    grid = [list(cols), ["---"] * len(cols)] + [list(row) for row in cells_per_row]
    widths = [max(cell_length(row[i]) for row in grid) for i in range(len(cols))]
    rows = []
    for index, row in enumerate(grid):
        cells = ["-" * w for w in widths] if index == 1 else [
            cell + " " * (widths[i] - cell_length(cell)) for i, cell in enumerate(row)]
        rows.append("| " + " | ".join(cells) + " |")
    return rows

def trending_table(plugins, limit):
    cols = ["Rank", "Plugin", "Downloads", "Description", "Install"]
    medals = {1: "🥇 1", 2: "🥈 2", 3: "🥉 3"}

    def cells(i, p):
        name, desc, install = plugin_cells(p, 92)
        return [medals.get(i, f"`#{i}`"), name, f"📥 **{format_number(p['downloads'])}**",
                desc, install]

    return "\n".join(table_rows(cols, [cells(i, p) for i, p in enumerate(plugins[:limit], 1)]))

def list_item(p):
    """Curated entry: `- [Name](url) - Description.` on the first line, the install link
    on an indented second line.

    The split is deliberate: awesome-lint only inspects the *first* paragraph of a list item
    (`const [paragraph] = listItem.children`), so the description has to stay on the marker
    line to satisfy the "link - description ending in a period" rule, while the metadata line
    is free of it. Nothing is truncated — GitHub wraps long descriptions naturally.
    """
    repo = p.get("repo", "")
    desc = p.get("description", "").strip()
    if desc and not desc.endswith("."):
        desc += "."
    url = f"https://github.com/{repo}" if repo else f"https://obsidian.md/plugins?id={p['id']}"
    line = f"- [{p['name']}]({url})" + (f" - {desc}" if desc else "")
    meta = f"[⚡ Open](https://obsidian.md/plugins?id={p['id']})" if repo else ""
    return f"{line}\n  {meta}" if meta else line

def plugins_list(plugins):
    return "\n".join(list_item(p) for p in plugins)

def render_readme(curated, plugin_map, table, summary, template_path):
    sections, appendix = curated.get("sections", []), curated.get("appendix", {})
    def entry(pid):
        """Registry record reduced to the fields the table needs, with a safe fallback
        for IDs that are no longer in the registry."""
        p = plugin_map.get(pid)
        if not p:
            return {"id": pid, "name": pid, "description": "Not found in the official registry."}
        return {
            "id": pid,
            "name": p.get("name", pid),
            "repo": p.get("repo", ""),
            "description": clean_description(p.get("description", "")),
        }
    # Catalog and playbook entries are one level below their parent in Contents.
    def toc_of(items, prefix="  "):
        return [f"{prefix}- [{s['title']}](#{slug(s['title'])})" for s in items]

    def block(s):
        desc = f"> {s['description']}\n\n" if s.get("description") else ""
        intro = (s.get("intro") or "").strip()
        outro = (s.get("outro") or "").strip()
        return (f"### {s['title']}\n\n{desc}{intro + '\n\n' if intro else ''}"
                + plugins_list([entry(pid) for pid in s.get("plugins", [])])
                + (f"\n\n{outro}" if outro else ""))

    playbooks = curated.get("playbooks", [])
    toc = toc_of(sections)
    blocks = [block(s) for s in sections]
    pb_toc = toc_of(playbooks)
    pb_blocks = [block(s) for s in playbooks]
    # The community directory keys theme pages by a slug of the theme name, so a curated
    # theme gets the same one-click "Open" affordance that plugins get from their registry ID.
    def theme_open(it):
        return f"https://community.obsidian.md/themes/{slug(it.get('id') or it['name'])}"

    tail = []
    for key, heading, by_repo in (("themes", "Popular Themes", True),
                                  ("templates", "Vault Starters and Methodologies", False),
                                  ("communities", "Community Hubs", False)):
        items = appendix.get(key) or []
        if not items:
            continue
        def link(it, by_repo=by_repo):
            return (f"https://github.com/{it['repo']}" if it.get("repo") else it.get("url", "#")) \
                if by_repo else it.get("url", "#")

        def item(it, key=key):
            # `**[Name](url)**` trips awesome-list-item: the rule reads the first child of the
            # paragraph as the link and finds `strong` instead. `[**Name**](url)` renders the
            # same bold link and satisfies it.
            line = f"- [**{it['name']}**]({link(it)}) - {it.get('desc', '')}"
            return f"{line}\n  [⚡ Open]({theme_open(it)})" if key == "themes" else line

        tail += [f"### {heading}\n"] + [item(it) for it in items]
        note = (appendix.get("notes") or {}).get(key, "").strip()
        if note:
            tail += ["", note]
        tail += [""]
    return render_template(template_path, {
        "TOC_SECTIONS": "\n".join(toc),
        "TOC_PLAYBOOKS": "\n".join(pb_toc),
        "RISING_SUMMARY": summary,
        "RISING_TABLE": table,
        "SECTIONS": "\n\n---\n\n".join(blocks),
        "PLAYBOOKS": "\n\n---\n\n".join(pb_blocks),
        "APPENDIX": "\n".join(tail).rstrip(),
    })

def main():
    ap = argparse.ArgumentParser(description="Build Awesome Obsidian.")
    add = ap.add_argument
    add("--refresh", action="store_true", help="Force refresh cached files from remote")
    add("--cache-dir", default="cache", help="Cache directory (default: cache)")
    add("--curated", default="data/curated.json", help="Path to curated.json")
    add("--readme", default="README.md", help="Path to output README.md")
    add("--template", default=os.path.join("data", "README.template.md"), help="Markdown template to render")
    add("--days", type=int, default=120, help="Trending lookback window in days (default: 120)")
    add("--trending-limit", type=int, default=50,
        help="Rows in the auto-generated Discover New Plugins table, ranked by downloads (default: 50)")
    add("--token", default=os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN"),
        help="GitHub Personal Access Token")
    a = ap.parse_args()
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=a.days)
    os.makedirs(a.cache_dir, exist_ok=True)
    print(f"[*] Build starting at {now:%Y-%m-%d %H:%M:%SZ}")
    print(f"[*] Cache directory: {a.cache_dir} (refresh={a.refresh})")
    curated = load_json(a.curated)
    plugins = ensure_cache_file(os.path.join(a.cache_dir, "community-plugins.json"), PLUGINS_URL, a.refresh)
    stats = ensure_cache_file(os.path.join(a.cache_dir, "community-plugin-stats.json"), STATS_URL, a.refresh)
    print(f"[+] Total official plugins: {len(plugins):,}")
    baseline = {p["id"] for p in get_historic_plugins(a.cache_dir, cutoff, a.refresh, a.token)}
    if not baseline:
        sys.exit(f"[x] Fatal: historic baseline for {cutoff:%Y-%m-%d} is empty; "
                 "refusing to build a trending list from an untrustworthy baseline.")
    print(f"[+] Historic baseline plugins: {len(baseline):,}")
    # Anything already reviewed above is skipped here: the same URL appearing twice in one
    # document is a lint error, and a plugin that survived curation belongs in the catalog.
    curated_ids = {pid for group in (curated.get("sections", []), curated.get("playbooks", []))
                   for s in group for pid in s.get("plugins", [])}
    fresh = [p for p in plugins if p["id"] not in baseline and p["id"] not in curated_ids]
    print(f"[+] New plugins identified in past {a.days} days: {len(fresh):,}"
          f" (skipping {len(curated_ids)} already curated)")
    trending = sorted(({
        "id": p["id"], "name": p.get("name", p["id"]),
        "repo": p.get("repo", ""), "description": clean_description(p.get("description", "")),
        "downloads": stats.get(p["id"], {}).get("downloads", 0),
    } for p in fresh), key=lambda p: p["downloads"], reverse=True)
    summary = (f"<sub>📈 **Lookback Period**: Past {a.days} Days ({cutoff:%Y-%m-%d} ~ {now:%Y-%m-%d}) | "
               f"**New Plugins Tracked**: {len(fresh):,} | **Last Refreshed**: `{now:%Y-%m-%d}`</sub>")
    with open(a.readme, "w", encoding="utf-8") as f:
        f.write(render_readme(curated, {p["id"]: p for p in plugins},
                              trending_table(trending, a.trending_limit), summary, a.template))
    print(f"[+] Successfully generated {a.readme}")
    print("[🎉] Build finished successfully!")

if __name__ == "__main__":
    main()
