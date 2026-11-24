"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to entry.txt.
Deterministic: no network, no wall-clock, no randomness.
"""

import os

JOKE = (
    "The office printer only jams on deadline day, which makes it the most "
    "honest project manager in the building."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
