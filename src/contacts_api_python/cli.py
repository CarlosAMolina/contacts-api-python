from argparse import ArgumentParser
from dataclasses import dataclass


@dataclass
class Arguments:
    search_term: str | None


def parse_arguments() -> Arguments:
    parser = ArgumentParser(description="Analyze the structure of a JSON file.")
    parser.add_argument(
        "search_term",
        type=str,
        nargs="?",
        default=None,
        help="Optional term to filter contacts",
    )
    args = parser.parse_args()
    return Arguments(args.search_term)
