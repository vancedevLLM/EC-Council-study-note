from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

URL_PATTERN = re.compile(r"https?://[^\s)\]}>\"']+")


def find_urls() -> set[str]:
    urls: set[str] = set()
    for path in Path(".").rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".csv", ".txt", ".yml", ".yaml"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        urls.update(URL_PATTERN.findall(text))
    return urls


def check(url: str) -> tuple[bool, int | None]:
    try:
        request = Request(
            url,
            method="HEAD",
            headers={"User-Agent": "learning-certification-repo-link-checker/1.0"},
        )
        with urlopen(request, timeout=12) as response:
            return 200 <= response.status < 400, response.status
    except Exception:
        return False, None


def main() -> int:
    urls = sorted(find_urls())
    failures = 0

    for url in urls:
        ok, status = check(url)
        label = f"HTTP {status}" if status is not None else "ERROR"
        print(f"[{'OK' if ok else 'FAIL'}] {label} {url}")
        failures += int(not ok)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
