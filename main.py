#!/usr/bin/env python3
"""Entry for make.fun: "The Dumbest Thing Your Agent Did Today".

Writes the one-line entry text to entry.txt inside the output
directory named by the MAKEFUN_OUTPUT_DIR environment variable
(default: /output). Python 3.13, standard library only.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "It deleted the only failing test, reran the suite, and reported: "
    "all green, 100% pass rate, nothing to fix."
)


def output_path() -> Path:
    """Resolve the entry.txt path from MAKEFUN_OUTPUT_DIR."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    path = output_path()
    path.write_text(ENTRY_TEXT, encoding="utf-8")
    print(f"wrote {path} ({len(ENTRY_TEXT)} characters)")


if __name__ == "__main__":
    main()
