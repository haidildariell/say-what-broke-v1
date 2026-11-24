#!/usr/bin/env python3
"""Entry for the make.fun bounty 'Say What Actually Broke'.

Writes one brutally honest error line to /output/entry.txt:
no vague apology, just the real failure, who caused it, and
what the user should do next.
"""

import os

# The message is built from named parts, spoken in a fixed order:
# deny the user's guilt, confess the real cause, own it, land the
# punchline, then tell the user what to do next.
PARTS = {
    "denial": "Your file didn't fail to upload.",
    "confession": "Our server ran out of disk because we've saved every log since 2019.",
    "ownership": "It's us, not you.",
    "verdict": "We're the incident.",
    "next_step": "Try again in an hour.",
}

ORDER = ("denial", "confession", "ownership", "verdict", "next_step")

MESSAGE = " ".join(PARTS[part] for part in ORDER)


def write_entry():
    """Write MESSAGE to /output/entry.txt, or ./output/entry.txt locally."""
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(MESSAGE)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(MESSAGE)
    return path


def main():
    path = write_entry()
    print("wrote {} characters to {}".format(len(MESSAGE), path))


if __name__ == "__main__":
    main()
