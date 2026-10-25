from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Arguments:
    json_path: Path
    search_term: str | None


def parse_arguments() -> Arguments:
    parser = ArgumentParser(description="Analyze the structure of a JSON file.")
    parser.add_argument(
        "json_path", type=Path, help="Path to the JSON file with contacts"
    )
    parser.add_argument(
        "search_term",
        type=str,
        nargs="?",
        default=None,
        help="Optional term to filter contacts",
    )
    args = parser.parse_args()
    return Arguments(args.json_path, args.search_term)
