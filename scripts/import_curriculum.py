"""One-time, non-overwriting import of the user's original candidate curriculum."""

import argparse
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

from common import ROOT, read_yaml, write_yaml


def normalize(source):
    slots = source["slots"]
    dates = [date.fromisoformat(str(row["date"])) for row in slots]
    expected = {date(2027, 1, 1) + timedelta(days=i) for i in range(365)}
    if len(slots) != 365 or set(dates) != expected or len(set(dates)) != 365:
        raise ValueError("Input must cover exactly the 365 dates of 2027")
    if len({row["id"] for row in slots}) != 365:
        raise ValueError("Input IDs must be unique")
    entries, briefs = [], {}
    for row, day in zip(slots, dates):
        track = row["track"]
        expected_track = (
            "micro_design" if day.weekday() == 6 else
            "investing" if day.weekday() == 5 else
            "product" if day.weekday() in {1, 3} else "engineering"
        )
        if track != expected_track or row["day"] != day.strftime("%A"):
            raise ValueError(f"Weekday mismatch: {row['id']}")
        design = track == "micro_design"
        domain = row["domain"] if design else track
        domain = "investing" if domain == "venture" else domain
        kind = "micro_design" if design else "historical"
        brief_path = (
            f"designs/{row['id']}.yaml" if design else
            f"cases/{domain}/{row['id']}.yaml"
        )
        move = row["primary_cognitive_move"] if design else row["planned_cognitive_move"]
        entries.append({
            "date": day.isoformat(), "id": row["id"], "kind": kind,
            "domain": domain, "subdomain": row["subdomain"].replace("_", "-"),
            "focus": move.replace("_", "-"), "status": "candidate",
            "brief_path": brief_path,
            "protocol_path": "protocols/micro-design.md" if design else "protocols/historical.md",
        })
        briefs[brief_path] = {
            "id": row["id"], "kind": kind, "domain": domain, "status": "candidate",
            "scenario_title": row["title"] if design else row["historical_case"],
            "readiness_note": "仅导入原始候选素材；尚未核源或通过 Case QA，不可用于训练。",
            "origin": {"file": "curriculum_2027_complete.yaml", "id": row["id"]},
            "candidate_material": row,
        }
    counts = Counter((e["kind"], e["domain"]) for e in entries)
    expected_counts = {
        ("historical", "engineering"): 157, ("historical", "product"): 104,
        ("historical", "investing"): 52, ("micro_design", "engineering"): 22,
        ("micro_design", "product"): 18, ("micro_design", "investing"): 12,
    }
    if counts != expected_counts:
        raise ValueError(f"Unexpected quotas: {counts}")
    entries.sort(key=lambda row: row["date"])
    return {"year": 2027, "timezone": "Pacific/Auckland", "entries": entries}, briefs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "curriculum_2027_complete.yaml")
    parser.add_argument("--output-root", type=Path, default=ROOT)
    args = parser.parse_args()
    index, briefs = normalize(read_yaml(args.source))
    files = {"curriculum/2027.yaml": index, **briefs}
    # Preflight every target before any write; never replace reviewed work.
    for rel in files:
        path = args.output_root / rel
        if path.exists() or path.is_symlink():
            raise SystemExit(f"Refusing to overwrite {path}")
        if not path.resolve().is_relative_to(args.output_root.resolve()):
            raise SystemExit(f"Target escapes output root: {path}")
    for rel, content in files.items():
        write_yaml(args.output_root / rel, content)
    print(f"Imported {len(index['entries'])} candidates; no source verification performed.")


if __name__ == "__main__":
    main()
