# /// script
# dependencies = [
#   "bibtexparser"
# ]
# ///

from pathlib import Path
import sys
import argparse

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter

# Fields to remove from entries
FIELDS_TO_REMOVE = [
    "modificationdate",
    "creationdate",
    "timestamp",
    "file",
    "keywords",
    "abstract",
    "note",
    "refid",
    "priority",
    "issn",
    "bdsk-url-1",
    "date-added",
    "date-modified",
    "pubmedid",
    "bdsk-url-2",
    "language",
]


def clean_and_overwrite(bib_path: Path) -> None:
    with bib_path.open("r", encoding="utf-8") as bibtex_file:
        parser = BibTexParser(common_strings=True)
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    for entry in bib_database.entries:
        for field in FIELDS_TO_REMOVE:
            entry.pop(field, None)

    writer = BibTexWriter()
    writer.indent = "    "  # 4-space indent
    writer.order_entries_by = None  # keep the source order

    cleaned_bib_str = bibtexparser.dumps(bib_database, writer)

    # overwrite the original file
    bib_path.write_text(cleaned_bib_str, encoding="utf-8")
    print(f"Cleaned and overwrote {bib_path}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Clean a .bib file by removing unwanted fields and overwrite it."
    )
    parser.add_argument("bib_file", nargs="?", help="Path to .bib file to clean")

    args = parser.parse_args(argv)

    if args.bib_file:
        bib_path = Path(args.bib_file)
    else:
        # fallback default name that was previously used
        bib_path = Path("MyCollection.bib")

    if not bib_path.exists():
        print(f"Error: '{bib_path}' not found.", file=sys.stderr)
        sys.exit(1)

    clean_and_overwrite(bib_path)


if __name__ == "__main__":
    main()
