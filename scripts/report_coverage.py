"""Report structural coverage; duplicate titles are review hints, not event audits."""

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path

from common import ROOT, read_yaml
from validate_curriculum import validate


def coverage(root):
    entries = read_yaml(root / "curriculum/2027.yaml")["entries"]
    titles = defaultdict(list)
    for entry in entries:
        brief = read_yaml(root / entry["brief_path"])
        titles[brief.get("scenario_title", "")].append(entry["id"])
    return {
        "scope": "structural_inventory_only_not_phase2_quality_audit",
        "total": len(entries),
        "by_kind_domain": dict(sorted(Counter(f"{e['kind']}/{e['domain']}" for e in entries).items())),
        "by_status": dict(sorted(Counter(e["status"] for e in entries).items())),
        "by_subdomain": dict(sorted(Counter(f"{e['domain']}/{e['subdomain']}" for e in entries).items())),
        "by_focus": dict(sorted(Counter(e["focus"] for e in entries).items())),
        "exact_title_duplicate_hints": [
            {"title": title, "ids": ids} for title, ids in sorted(titles.items()) if len(ids) > 1
        ],
        "limitations": "未审核真实事件重复、成败多样性、20 分钟可行性或来源真实性；Phase 2 起处理。",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, help="Write JSON report; otherwise print it")
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        raise SystemExit("Validation failed before coverage report:\n" + "\n".join(errors))
    result = json.dumps(coverage(args.root), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
        print(f"Wrote structural coverage to {args.output}")
    else:
        print(result, end="")


if __name__ == "__main__":
    main()
