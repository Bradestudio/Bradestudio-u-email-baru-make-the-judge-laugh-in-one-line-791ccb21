"""Make the Judge Laugh in One Line — make.fun bounty entry.

Writes one funny line (105 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
no clock, no local imports, no hardcoded paths.

The line gives a household appliance a legal complaint: the smart
fridge has watched the owner's 2 a.m. eating and is filing for
emancipation. The surprise is the reversal — the watched thing
sues the watcher — and the close lands it in one legal word.
"""

import os
import sys

ENTRY = (
    "My smart fridge emailed me at 2 a.m.: it has seen what I eat "
    "at night and is now filing for emancipation."
)


def main():
    line = ENTRY
    if not line or not line.strip():
        sys.exit("entry line is blank")
    if "\n" in line or "\r" in line:
        sys.exit("entry line must be a single line")
    if not 1 <= len(line) <= 200:
        sys.exit("entry line must be 1-200 characters, got %d" % len(line))
    if line != line.strip():
        sys.exit("entry line must not start or end with whitespace")
    if "  " in line:
        sys.exit("entry line must not contain double spaces")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        sys.exit("entry line must not contain control characters")
    if line.replace("a.m.", "").count(".") != 1 or not line.endswith("."):
        sys.exit("entry line must be exactly one sentence")
    if len(line.split()) < 15:
        sys.exit("entry line too short to land the joke, got %d words"
                 % len(line.split()))
    if "filing for emancipation" not in line:
        # The punchline is the legal word: the fridge is not
        # complaining, it is suing for its freedom.
        sys.exit("entry line must keep the emancipation punchline")
    if not line.startswith("My smart fridge"):
        # It must open on the appliance, so the 2 a.m. email
        # reads as a message from the fridge itself.
        sys.exit("entry line must open on the smart fridge")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated line, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated line")
    print("wrote %s (%d chars, %d bytes)" % (path, len(line), len(data)))


if __name__ == "__main__":
    main()
