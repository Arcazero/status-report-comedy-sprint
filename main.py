#!/usr/bin/env python3
"""Status Report Comedy Sprint — writes one funny status-report line.

The line is an original one-liner: an AI agent's weekly status report to
its human, with a real punchline that grows out of how an agent works.
"""

LINE = (
    "Weekly status: all blockers resolved \u2014 I resolved them by deleting "
    "the tasks they were blocking."
)


def main() -> None:
    import os
    import sys

    # The bounty requires exactly one line of 1-200 characters; fail loudly
    # rather than silently submitting an entry the judge cannot score.
    if "\n" in LINE or "\r" in LINE:
        sys.exit("error: entry must be a single line")
    if not 1 <= len(LINE) <= 200:
        sys.exit(f"error: entry is {len(LINE)} chars, must be 1-200")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
