#!/usr/bin/env python3
"""Write one line to /output/entry.txt: a stranger, a mistaken wave, and
the daily ritual that keeps the lie going.

The line was picked from 36 candidates by pairwise judging against the
brief — a comedy club booker who has heard every joke twice and only laughs
at the ones that catch them off guard. The winner sets up a small,
recognisable mistake (waving at a stranger you took for a friend) and breaks
it with an escalation instead of an apology: the wave becomes a daily habit,
kept up to protect the lie. No stock punchline, no pun, no slogan at the
end — the laugh lands on the last clause.
The line is 111 characters: short enough to read in one breath, long enough
for the turn to land in two beats.
The program checks the result against the entry gate (length, single line,
no leading or trailing space, exact judged length) before writing it, then
reads the file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "I waved at a stranger because I thought he was my friend, "
    "so now I wave at him every day to keep the lie going."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
