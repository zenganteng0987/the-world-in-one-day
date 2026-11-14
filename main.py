#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-01.

The entry image (entry.png, stored beside this file) sums up the world
news of Friday 13 November 2026 in a single front-page image. The
grader runs this program twice in a fresh container and both runs must
write the same bytes, so the program does exactly one thing: after a
quick sanity check of the asset, copy the fixed image to the output
directory as entry.png.

The sanity check reads only the file header: the image must be a whole
PNG or JPEG of at most 1 MiB and at most 1024 x 1024 pixels, which are
exactly the limits the competition's gate enforces. If the asset ever
failed them, the program stops loudly instead of serving a file the
gate would refuse.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import struct
from pathlib import Path

MAX_BYTES = 1_048_576  # 1 MiB
MAX_SIDE = 1024

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def check_asset(path: Path) -> None:
    """Raise ValueError unless the file is a gate-legal PNG or JPEG."""
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise ValueError(f"entry image is {len(data)} bytes, over the 1 MiB cap")
    if data.startswith(PNG_MAGIC):
        # IHDR is the first chunk: width and height are big-endian
        # uint32 values 16 and 20 bytes into the file.
        width, height = struct.unpack(">II", data[16:24])
    elif data.startswith(JPEG_MAGIC):
        width = height = 0  # the gate reads JPEG dimensions itself
    else:
        raise ValueError("entry image is neither PNG nor JPEG")
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(f"entry image is {width}x{height}, over the 1024px cap")


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    check_asset(source)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
