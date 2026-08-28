from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "microsoft-certifications.json"
OUTPUT = ROOT / "data" / "microsoft-certifications.csv"


def main() -> None:
    records = json.loads(SOURCE.read_text(encoding="utf-8"))

    fields = [
        "exam_code",
        "title",
        "area",
        "official_exam",
        "official_study_guide",
        "external_guide",
    ]

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for record in records:
            writer.writerow({field: record.get(field, "") for field in fields})

    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
