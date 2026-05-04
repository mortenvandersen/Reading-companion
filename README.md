# Reading Companion

A personal system for turning each Stratechery article into a structured, searchable, re-readable conversation with Claude.

## How it works

1. **Capture** — Click the bookmarklet on any Stratechery article tab. The article body is sent to a static capture page hosted on GitHub Pages, which writes a row to a Supabase `inbox` table.
2. **Ingest** — An hourly GitHub Action pulls pending rows from `inbox`, writes one markdown file per article into `articles/`, and marks the row processed.
3. **Read** — Open this repo in Claude Code, say *"let's discuss the new article"*. Claude reads the newest file in `articles/`, produces a TL;DR, and writes a companion note in `notes/` in real time as the discussion unfolds. Concepts surfaced in the article are added to or updated in `concepts/`. The master `index.md` is updated at the end of each session.

## Layout

```
articles/      Raw article text, one file per piece (YYYY-MM-DD-slug.md)
notes/         Companion notes, one per article (matched filename)
concepts/      Recurring frameworks, accumulating (slug.md)
threads/       Multi-article syntheses (added as needed)
index.md       Master index, maintained by Claude Code
templates/     Note and concept templates (referenced by CLAUDE.md, not as content)
capture/       GitHub Pages capture page
scripts/       Ingestion script
.github/       Workflow that runs the ingestion script hourly
```

## Setup

See `CLAUDE.md` for reading workflow. See the build plan in the repo's planning notes for one-time setup of Supabase, GitHub Pages, and the bookmarklet.

## Status

Phase 1 — minimal capture + structured discussion. No embeddings, no search dashboard, no email digest. Those come after 10+ articles have been read with Phase 1.
