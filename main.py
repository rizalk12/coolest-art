"""The Village That Sails the Sky.

Artwork entry for make.fun coolest-art-01: a lantern-lit village rides on
the shell of a colossal ancient turtle as it swims through a sea of clouds
at dusk, one tiny red-sailed boat drifting far below.

The artwork ships as entry.png next to this file. Running this program
copies those exact bytes to <output dir>/entry.png, where the output dir
is $MAKEFUN_OUTPUT_DIR (default /output). No network, no randomness, no
clock: every run produces a byte-identical copy.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1_048_576  # competition cap for the artwork file
JPEG_MAGIC = b"\xff\xd8"  # every JPEG starts with these two bytes


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    try:
        with open(SOURCE, "rb") as f:
            data = f.read()
    except OSError as e:
        sys.exit(f"error: cannot read artwork {SOURCE}: {e}")
    if not data.startswith(JPEG_MAGIC):
        sys.exit("error: entry.png is not a JPEG image")
    if len(data) > MAX_BYTES:
        sys.exit(f"error: entry.png is {len(data)} bytes, over the {MAX_BYTES} cap")
    dest = os.path.join(out_dir, "entry.png")
    with open(dest, "wb") as f:
        f.write(data)
    print(f"wrote {dest} ({len(data)} bytes)", file=sys.stderr)


if __name__ == "__main__":
    main()
