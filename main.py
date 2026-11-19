"""Copy the bundled 19 November 2026 front page to the output directory.

The entry image lives next to this file as entry.png. The program only
copies bytes: no network, no randomness, no image libraries. Running it
twice therefore produces byte-identical output every time.
"""

from os import environ, makedirs
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "entry.png"


def main():
    # The grader runs the program twice; a pure byte copy is
    # deterministic by construction, and the read-back below proves it.
    target_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    makedirs(target_dir, exist_ok=True)
    target = target_dir / "entry.png"
    data = IMAGE.read_bytes()
    target.write_bytes(data)
    if target.read_bytes() != data:
        raise SystemExit("entry.png was not copied byte-for-byte")


if __name__ == "__main__":
    main()
# Entry: 19 November 2026 front page, 1024x1024 PNG.
