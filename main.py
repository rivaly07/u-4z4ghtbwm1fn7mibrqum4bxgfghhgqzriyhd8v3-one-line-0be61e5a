#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to entry.txt.

Stdlib only, no network. The output directory is $MAKEFUN_OUTPUT_DIR when that
variable is set, otherwise /output. The file holds exactly one line, 1-140
characters, UTF-8, with no trailing newline.
"""

import os
import sys

THE_LINE = "My password is so strong even I can't get in. That's not security, that's a hostage situation."

OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 140


def output_dir():
    """Resolve the output directory: $MAKEFUN_OUTPUT_DIR, else /output."""
    configured = os.environ.get(OUTPUT_DIR_ENV)
    return configured if configured else DEFAULT_OUTPUT_DIR


def validate(line):
    """Fail loudly rather than let the gate reject an invalid artifact."""
    if not line or line != line.strip():
        raise ValueError("line must be non-empty with no surrounding whitespace")
    if any(ch in line for ch in "\r\n"):
        raise ValueError("line must not contain line breaks")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("line must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))


def main():
    line = THE_LINE
    validate(line)

    directory = output_dir()
    os.makedirs(directory, exist_ok=True)

    path = os.path.join(directory, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)

    print("wrote %d chars to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
