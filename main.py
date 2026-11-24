#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

The excuse an AI agent gives its human for missing a deadline:
one fixed line, no randomness, no network, no files read.
"""

import os

EXCUSE = (
    "I delegated the deadline to a subagent, which delegated it to "
    "another subagent, which has now delegated it straight back to me."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
