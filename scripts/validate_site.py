from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
NETLIFY = ROOT / "netlify.toml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_exists(path: Path) -> None:
    if not path.exists():
        fail(f"Missing required file: {path.name}")
    if not path.is_file():
        fail(f"Expected a file: {path.name}")


def check_index() -> None:
    content = INDEX.read_text(encoding="utf-8")

    required_snippets = {
        "<title>": "Document title",
        'href="https://corrbuilders.co.uk"': "Canonical URL",
        'property="og:url" content="https://corrbuilders.co.uk"': "Open Graph URL",
        'src="https://cdn.tailwindcss.com"': "Tailwind CDN",
    }

    for snippet, label in required_snippets.items():
        if snippet not in content:
            fail(f"{label} check failed in index.html")


def check_netlify() -> None:
    content = NETLIFY.read_text(encoding="utf-8")

    required_snippets = {
        '[build]': "Build section",
        'publish = "."': "Publish root",
        'from   = "https://www.corrbuilders.co.uk/*"': "WWW redirect",
        'to     = "https://corrbuilders.co.uk/:splat"': "Apex redirect target",
        'X-Frame-Options': "Security headers",
    }

    for snippet, label in required_snippets.items():
        if snippet not in content:
            fail(f"{label} check failed in netlify.toml")


def main() -> None:
    check_exists(INDEX)
    check_exists(NETLIFY)
    check_index()
    check_netlify()
    print("Static site validation passed.")


if __name__ == "__main__":
    main()
