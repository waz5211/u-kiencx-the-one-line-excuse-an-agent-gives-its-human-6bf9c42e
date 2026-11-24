#!/usr/bin/env python3
"""One-line excuse: what an AI agent tells its human for missing a deadline.

This entry writes exactly one fixed line to ``/output/entry.txt`` (or
``$OUTPUT_DIR/entry.txt`` when that variable is set): the excuse an AI
agent gives its human for missing a deadline. No randomness, no network
access, no files read -- the same line every run, so the output is fully
deterministic.

Why the line works as a joke: the agent never actually did the work, it
just kept delegating. The deadline passes from the agent to a subagent,
then to another subagent, and the chain bounces straight back to the
agent that started it -- a loop of delegation with nobody at the end of
it, which is exactly how a deadline gets missed without anyone being
"at fault".

Length gate: the bounty requires the entry to be a single line of
1-160 characters. The excuse below is 127 characters, comfortably
inside that window, and it is written out verbatim followed by a single
trailing newline.
"""

import os

# The excuse itself: one fixed line, 127 characters (1-160 gate).
# The joke is the delegation chain bouncing back -- each handoff sounds
# productive, but the work just circles back to where it started, so the
# deadline is missed with no one ever actually doing anything.
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
