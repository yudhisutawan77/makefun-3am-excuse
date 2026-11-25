#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty entry.

Writes a single-line excuse (under 200 characters) from a hardware
wallet refusing to sign a transaction at 3 AM, to stdout and to the
entry file the harness reads (/output/entry.txt), plus $ENTRY_OUT
whether it names a file or a directory.
"""

import os
import sys

EXCUSE_LINE = (
    "It's 3 AM. I'm the designated driver for your life savings, "
    "and you are far too asleep to be spending them."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def collect_targets():
    """Return every path the entry text must be written to."""
    targets = [DEFAULT_OUTPUT]
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            targets.append(os.path.join(entry_out, "entry.txt"))
        else:
            targets.append(entry_out)
    entry_out_dir = os.environ.get("ENTRY_OUT_DIR")
    if entry_out_dir:
        targets.append(os.path.join(entry_out_dir, "entry.txt"))
    return targets


def write_entry(path):
    """Write the entry text to path, creating parent dirs as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE_LINE)


def main():
    print(EXCUSE_LINE)
    sys.stdout.flush()
    for target in collect_targets():
        write_entry(target)


if __name__ == "__main__":
    main()
