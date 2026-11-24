#!/usr/bin/env python3
"""Say What Actually Broke.

One line of software error copy: a save that failed because the disk is
full of the user's own unsaved work. The line names the real failure,
lands the joke on a single read, and is the sort of thing a team could
actually ship in an error dialog. main.py validates the line on every
run, writes it to /output/entry.txt (no trailing newline) and prints it.

Deterministic: no clock, no randomness, no network, stdlib only.
"""

import argparse
import os
import sys

# The entry: exactly one line, non-empty, at most 200 characters.
# Why it lands: the failure is the user's own doing, the dialog knows it,
# and the last two sentences let the app shrug instead of apologising.
ERROR_LINE = (
    "Save failed: your disk is full of unsaved work, so there's nowhere "
    "to put the unsaved work. We tried. You didn't."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check_line(line: str) -> None:
    """Raise unless the line is one non-empty line of at most 200 chars."""
    if not line:
        raise ValueError("error line must not be empty")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("error line must be exactly one line, no leading/trailing space")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "error line is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )


def write_line(path: str = OUTPUT_PATH) -> str:
    """Write the error line to path with no trailing newline; return it."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as out:
        out.write(ERROR_LINE)
    return ERROR_LINE


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Write one honest, funny error line (a save that failed "
        "because the disk is full of unsaved work) to /output/entry.txt "
        "and print it. The line is validated first: exactly one line, "
        "non-empty, at most 200 characters.",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="only validate the error line and exit 0 if it passes, "
        "1 if it fails (writes nothing)",
    )
    parser.add_argument(
        "--output",
        default=OUTPUT_PATH,
        help="path of the entry file (default: /output/entry.txt)",
    )
    return parser


def main(argv=None) -> int:
    args = make_parser().parse_args(argv)
    try:
        check_line(ERROR_LINE)
    except ValueError as exc:
        print("invalid error line: %s" % exc, file=sys.stderr)
        return 1
    if args.verify:
        print("line valid: %d characters, 1 line" % len(ERROR_LINE))
        return 0
    print(write_line(args.output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
