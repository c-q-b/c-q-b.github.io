"""Small dependency-free integrity check for the static portfolio site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


PROJECT_DIR = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.local_references: list[str] = []
        self.anchors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        if (values.get("href") or "").startswith("#"):
            self.anchors.append(unquote(values["href"][1:]))
        for attribute in ("src", "href", "poster", "data-lightbox"):
            value = values.get(attribute)
            if value and self._is_local(value):
                self.local_references.append(value)

    @staticmethod
    def _is_local(value: str) -> bool:
        parsed = urlparse(value)
        return not parsed.scheme and not parsed.netloc and not value.startswith("#")


def main() -> None:
    parser = SiteParser()
    parser.feed((PROJECT_DIR / "index.html").read_text(encoding="utf-8"))

    duplicate_ids = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    missing_files = sorted(
        {
            reference
            for reference in parser.local_references
            if not (PROJECT_DIR / unquote(urlparse(reference).path)).is_file()
        }
    )

    missing_anchors = sorted(set(parser.anchors) - set(parser.ids))
    if duplicate_ids or missing_files or missing_anchors:
        if duplicate_ids:
            print(f"Duplicate IDs: {duplicate_ids}")
        if missing_files:
            print(f"Missing local files: {missing_files}")
        if missing_anchors:
            print(f"Missing anchor targets: {missing_anchors}")
        raise SystemExit(1)

    print(f"HTML IDs: {len(parser.ids)}")
    print(f"Local asset references: {len(parser.local_references)}")
    print("Site integrity check passed.")


if __name__ == "__main__":
    main()
