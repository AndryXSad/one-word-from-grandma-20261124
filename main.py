"""One Word From Grandma — entry program.

Design: the entry is exactly one word, the word a grandma would text
about AI. The program keeps that word as a single constant, checks it
against the bounty gate (UTF-8, 1 to 30 characters, not only whitespace,
a single word with no spaces), and writes exactly those bytes — no
trailing newline, so the file is as small as the word itself — to
/output/entry.txt. Pure standard library, no network, no randomness,
no reads from outside this repository: two runs produce the same file.
"""

import os
import sys

# The word: "Rosie".
# Grandma names the AI after Rosie, the robot maid from The Jetsons —
# the show from her era. She thinks the AI is a maid who has moved in,
# so she texts its name. Warm, a little baffled, funny in one word,
# tied to robots, and fresh in a field full of robit/doohickey/witchcraft
# copies. See CANDIDATES.md for the full shortlist and the reasons.
WORD = "Rosie"

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    word = WORD
    encoded = word.encode("utf-8")
    if not 1 <= len(word) <= 30:
        print(f"word must be 1-30 characters, got {len(word)}", file=sys.stderr)
        return 1
    if not word.strip():
        print("word must not be only whitespace", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in word):
        print("entry must be a single word, no spaces", file=sys.stderr)
        return 1
    if not word.isalpha():
        # No punctuation tricks, no digits, no hyphen: one plain word,
        # the way a grandma would type it.
        print("entry must be letters only", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(encoded)
    print(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
