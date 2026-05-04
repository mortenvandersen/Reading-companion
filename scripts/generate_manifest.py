#!/usr/bin/env python3
"""Generate manifest.json listing articles, notes, and concepts so the
dashboard at index.html can populate its lists without a backend.

Run from the repo root. Requires PyYAML.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
H1_RE = re.compile(r"^#\s+(.+)$")


def parse_md(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    fm: dict = {}
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            fm_text = text[4:end]
            try:
                loaded = yaml.safe_load(fm_text)
                if isinstance(loaded, dict):
                    fm = loaded
            except yaml.YAMLError:
                fm = {}
            body = text[end + 4 :].lstrip("\n")
    return fm, body


def first_h1(body: str) -> str | None:
    for line in body.splitlines():
        m = H1_RE.match(line)
        if m:
            return m.group(1).strip()
    return None


def list_md(folder: str) -> list[Path]:
    d = REPO_ROOT / folder
    if not d.exists():
        return []
    return sorted(p for p in d.iterdir() if p.is_file() and p.suffix == ".md")


def date_from_filename(name: str) -> str:
    m = DATE_RE.match(name)
    return m.group(1) if m else ""


def article_entry(p: Path) -> dict:
    fm, body = parse_md(p)
    captured = str(fm.get("captured_at") or "")
    return {
        "path": p.relative_to(REPO_ROOT).as_posix(),
        "filename": p.name,
        "title": fm.get("title") or first_h1(body) or p.stem,
        "source": fm.get("source") or "unknown",
        "source_url": fm.get("source_url") or "",
        "date": captured[:10] or date_from_filename(p.name),
        "tags": fm.get("tags") or [],
    }


def note_entry(p: Path) -> dict:
    fm, body = parse_md(p)
    return {
        "path": p.relative_to(REPO_ROOT).as_posix(),
        "filename": p.name,
        "title": fm.get("title") or first_h1(body) or p.stem,
        "source": fm.get("source") or "unknown",
        "date": str(fm.get("date") or "") or date_from_filename(p.name),
        "tags": fm.get("tags") or [],
        "concepts": fm.get("concepts") or [],
    }


def concept_entry(p: Path) -> dict:
    fm, body = parse_md(p)
    slug = fm.get("slug") or p.stem
    return {
        "path": p.relative_to(REPO_ROOT).as_posix(),
        "filename": p.name,
        "slug": slug,
        "title": first_h1(body) or slug,
        "first_seen": str(fm.get("first_seen") or ""),
        "tags": fm.get("tags") or [],
        "articles": fm.get("articles") or [],
    }


def main() -> int:
    articles = [article_entry(p) for p in list_md("articles")]
    notes = [note_entry(p) for p in list_md("notes")]
    concepts = [concept_entry(p) for p in list_md("concepts")]

    articles.sort(key=lambda x: x["date"], reverse=True)
    notes.sort(key=lambda x: x["date"], reverse=True)
    concepts.sort(key=lambda x: x["title"].lower())

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "counts": {
            "articles": len(articles),
            "notes": len(notes),
            "concepts": len(concepts),
        },
        "articles": articles,
        "notes": notes,
        "concepts": concepts,
    }

    out = REPO_ROOT / "manifest.json"
    out.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False, default=str) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {out.relative_to(REPO_ROOT)}: "
        f"{len(articles)} articles, {len(notes)} notes, {len(concepts)} concepts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
