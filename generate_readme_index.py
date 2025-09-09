#!/usr/bin/env python3
"""
generate_readme_index.py
Scans the KQL/ directory and updates README.md between markers:
<!-- BEGIN_QUERY_INDEX --> ... <!-- END_QUERY_INDEX -->

If markers are absent, the index section is appended to the end of README.md.

Usage (from repo root):
  python scripts/generate_readme_index.py
"""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
KQL_DIR = REPO_ROOT / "KQL"
README = REPO_ROOT / "README.md"

BEGIN = "<!-- BEGIN_QUERY_INDEX -->"
END = "<!-- END_QUERY_INDEX -->"

def slug(title: str) -> str:
    return title.replace(' ', '_')

def build_index() -> str:
    if not KQL_DIR.exists():
        return "_No `KQL/` directory found._"

    lines = []
    lines.append("## 📑 Query Index\n")
    # Collect folders and .kql files
    for folder in sorted([p for p in KQL_DIR.iterdir() if p.is_dir()]):
        files = sorted([f for f in folder.glob("*.kql")])
        if not files:
            continue
        lines.append(f"### {folder.name}/")
        for f in files:
            rel = f.as_posix().split("/")  # ensure forward slashes
            rel_path = "/".join(rel[rel.index('KQL'):])  # from KQL/
            lines.append(f"- [{f.name}]({rel_path})")
        lines.append("")

    # Handle _Unsorted if present with non-kql files (rare)
    unsorted = KQL_DIR / "_Unsorted"
    if unsorted.exists():
        kqls = sorted([f for f in unsorted.glob("*.kql")])
        lines.append(f"### _Unsorted/")
        if kqls:
            for f in kqls:
                rel_path = f.as_posix().split(f"{REPO_ROOT.as_posix()}/")[-1]
                lines.append(f"- [{f.name}]({rel_path})")
        else:
            lines.append("- *(any queries that don’t yet fit into a category)*")
        lines.append("")

    return "\n".join(lines).strip() + "\n"

def update_readme(index_md: str) -> None:
    if not README.exists():
        # create a minimal README with markers
        content = [
            "# 🔎 KQL Queries for Microsoft 365 Defender",
            "",
            "This repository contains KQL queries for Microsoft 365 Defender Advanced Hunting.",
            "",
            BEGIN,
            index_md,
            END,
            ""
        ]
        README.write_text("\n".join(content), encoding="utf-8")
        return

    text = README.read_text(encoding="utf-8")
    if BEGIN in text and END in text:
        before = text.split(BEGIN, 1)[0]
        after = text.split(END, 1)[1]
        new_text = before + BEGIN + "\n" + index_md + END + after
    else:
        # append at end
        if not text.endswith("\n"):
            text += "\n"
        new_text = text + "\n" + BEGIN + "\n" + index_md + END + "\n"

    if new_text != text:
        README.write_text(new_text, encoding="utf-8")

def main():
    index = build_index()
    update_readme(index)

if __name__ == "__main__":
    main()
