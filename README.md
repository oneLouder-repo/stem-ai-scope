# STEM AI Scope

A small static web platform for scanning the AI landscape: think tanks, innovation hubs, public education institutes and public-facing university AI labs. It focuses on community uses, ethics, pedagogy, STEM promotion, creative methods, Afrofuturism, Indigenous futurism, and Indigenous and Black AI. Canada comes first, with the UK and EU as a secondary layer.

**Live site:** https://onelouder-repo.github.io/stem-ai-scope/ (once GitHub Pages is on; see below)

## What's in it

| Page | What it shows | Where the content lives |
|---|---|---|
| `index.html` | Digest of the latest roundup, dashboard stats, theme mix, focus-area watchlist | computed from `data/` |
| `summary.html` | ~500-word executive summary | `content/summary.md` |
| `brief.html` | ~2,000-word strategy brief | `content/brief.md` |
| `roundups.html` | Weekly roundups and a searchable, sortable database with CSV export | `data/roundups/*.json`, `data/items.json` |
| `timeline.html` | Theme constellation (week × theme) and a week-by-week spine | same |
| `feed.html` | Posts harvested from every tracked blog, YouTube channel and social feed | `data/feed.json` (generated) |
| `sources.html` | The maintainable source list with live feed status | `data/sources.json` |
| `bibliography.html` | APA 7 references for every scanned item plus foundational literature | `data/items.json`, `data/literature.json` |

Everything is plain HTML, CSS and JavaScript with no build step. Data is JSON, and the long-form documents are Markdown.

## How the automation works

`.github/workflows/scan.yml` runs **every day at 10:15 UTC** (and whenever `data/sources.json` changes):

1. `scripts/harvest_feeds.py` reads every source in `data/sources.json` and writes `data/feed.json` and `data/feed_status.json`. It handles RSS/Atom, auto-discovers feeds from homepages, resolves YouTube handles and reads Bluesky profiles. For sites with no feed, it **scrapes the news listing page**: it collects article links (optionally filtered by a `link_pattern` regex), then reads each article's title, description and date. It uses the Python standard library only.
2. **On Mondays**, `scripts/weekly_scan.py` builds a roundup for the previous Monday–Sunday week. It filters the harvested items to the scan scope, scores them (Canada first, UK/EU second, extra weight on focus areas), keeps the top 15 and writes `data/roundups/YYYY-Www.json`.
3. The workflow commits the changes, and GitHub Pages republishes.

**Optional, recommended:** add an `ANTHROPIC_API_KEY` repository secret (Settings → Secrets and variables → Actions). The weekly scan then asks Claude to drop off-scope items, tidy summaries and write the headline and digest, using only facts from the harvested items. Without the key, it writes a plain automatic digest. To choose the model, set a repository variable `SCAN_MODEL` (default `claude-sonnet-5-5`).

**Run it by hand:** Actions → *Harvest feeds & weekly scan* → *Run workflow*. Leave "week" blank to build last week's roundup, or enter an ISO week such as `2026-W47` to rebuild one.

## Maintaining it

- **Add a source:** add an object to `data/sources.json` (`id`, `name`, `category`, `region`, `type`, `url`, and optionally `feed`, `youtube` or `bluesky`). The Sources page shows within a day whether it worked.
- **Edit a roundup:** edit its file in `data/roundups/`. Headline and digest are free text, and `item_ids` point into `data/items.json`.
- **Add an item by hand:** append it to `data/items.json` with a unique `id` and the right `week`, then add its id to that week's roundup. Run `python scripts/weekly_scan.py --reindex` to refresh the index.
- **Update the summary or brief:** edit the Markdown in `content/`.
- **Add literature:** append to `data/literature.json` (APA string, with `*asterisks*` for italics).

## Local / offline use

Download the repo as a ZIP (Code → Download ZIP), unzip it and **double-click `index.html`**. When a page is opened from disk it reads `data/bundle.js`, a snapshot of all the data that the Action rebuilds on every run, so no server is needed. (Fonts fall back to system fonts if you're offline.)

To refresh the data locally: `python scripts/harvest_feeds.py && python scripts/weekly_scan.py && python scripts/build_bundle.py`. Or serve live files with `python -m http.server 8000`.

## Turn on GitHub Pages

Settings → Pages → *Deploy from a branch* → `main` / `(root)` → Save.

## About the six-month backfill (May 11 – Nov 15, 2026)

The 27 backfilled roundups were researched by hand-run web searches and page checks on 2026-11-15. Every item was opened and its title, publisher, date and summary checked against the page. Items marked "(listing)" in their summary were verified from the publisher's dated news listing. Week 2026-W43 had no verifiable in-scope items and is left empty on purpose. The research inputs are kept in `scripts/seed/` for transparency.
