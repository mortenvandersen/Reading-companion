#!/usr/bin/env python3
"""Pull pending rows from the Supabase `inbox` table and write one
markdown file per article into `articles/`. Mark rows processed.

Run from the repo root. Requires SUPABASE_URL and SUPABASE_SERVICE_KEY
environment variables. Designed to be invoked by a GitHub Action that
commits any new files afterwards.
"""

from __future__ import annotations

import os
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import httpx

REPO_ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = REPO_ROOT / "articles"

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SERVICE_KEY"]

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^a-zA-Z0-9\s-]", "", value).lower().strip()
    value = re.sub(r"[\s-]+", "-", value)
    return value[:80].strip("-") or "untitled"


def parse_slug_from_notes(notes: str | None) -> str | None:
    if not notes:
        return None
    for line in notes.splitlines():
        if line.startswith("slug="):
            candidate = line[len("slug=") :].strip()
            if candidate:
                return slugify(candidate)
    return None


def parse_tags_from_notes(notes: str | None) -> list[str]:
    if not notes:
        return []
    for line in notes.splitlines():
        if line.startswith("tags="):
            raw = line[len("tags=") :].strip()
            return [t.strip() for t in raw.split(",") if t.strip()]
    return []


def host_to_source(site: str | None) -> str:
    if not site:
        return "unknown"
    host = site.lower().replace("www.", "")
    known = {"stratechery.com": "stratechery"}
    if host in known:
        return known[host]
    return host.split(".")[0] or "unknown"


def fetch_pending() -> list[dict]:
    r = httpx.get(
        f"{SUPABASE_URL}/rest/v1/inbox",
        headers=HEADERS,
        params={"status": "eq.pending", "order": "captured_at.asc", "select": "*"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def mark_processed(row_id: str, article_path: str) -> None:
    r = httpx.patch(
        f"{SUPABASE_URL}/rest/v1/inbox",
        headers=HEADERS,
        params={"id": f"eq.{row_id}"},
        json={
            "status": "processed",
            "processed_at": datetime.now(timezone.utc).isoformat(),
            "article_path": article_path,
        },
        timeout=30,
    )
    r.raise_for_status()


def mark_failed(row_id: str, reason: str) -> None:
    truncated = (reason or "")[:500]
    httpx.patch(
        f"{SUPABASE_URL}/rest/v1/inbox",
        headers=HEADERS,
        params={"id": f"eq.{row_id}"},
        json={"status": "failed", "notes": f"INGEST FAILED: {truncated}"},
        timeout=30,
    )


def unique_path(date_str: str, slug: str) -> Path:
    candidate = ARTICLES_DIR / f"{date_str}-{slug}.md"
    if not candidate.exists():
        return candidate
    n = 2
    while True:
        candidate = ARTICLES_DIR / f"{date_str}-{slug}-{n}.md"
        if not candidate.exists():
            return candidate
        n += 1


def yaml_escape(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_article(row: dict) -> Path:
    captured_at = row.get("captured_at") or datetime.now(timezone.utc).isoformat()
    date_str = captured_at[:10]
    title = (row.get("title") or "Untitled").strip()
    slug = parse_slug_from_notes(row.get("notes")) or slugify(title)
    tags = parse_tags_from_notes(row.get("notes"))
    source = host_to_source(row.get("site"))

    path = unique_path(date_str, slug)

    frontmatter_lines = [
        "---",
        f"title: {yaml_escape(title)}",
        f"source: {source}",
        f"source_url: {yaml_escape(row.get('source_url') or '')}",
        f"captured_at: {captured_at}",
        f"inbox_id: {row['id']}",
    ]
    if tags:
        frontmatter_lines.append("tags: [" + ", ".join(yaml_escape(t) for t in tags) + "]")
    frontmatter_lines.append("---")

    body = (row.get("body") or "").rstrip() + "\n"
    content = "\n".join(frontmatter_lines) + "\n\n" + f"# {title}\n\n" + body

    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    rows = fetch_pending()
    if not rows:
        print("No pending rows.")
        return 0

    print(f"Processing {len(rows)} pending row(s).")
    for row in rows:
        try:
            path = write_article(row)
            rel = path.relative_to(REPO_ROOT).as_posix()
            mark_processed(row["id"], rel)
            print(f"  OK  {row['id']} -> {rel}")
        except Exception as e:  # noqa: BLE001
            print(f"  FAIL {row.get('id')}: {e}", file=sys.stderr)
            try:
                mark_failed(row["id"], str(e))
            except Exception as inner:  # noqa: BLE001
                print(f"       (also failed to mark as failed: {inner})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
