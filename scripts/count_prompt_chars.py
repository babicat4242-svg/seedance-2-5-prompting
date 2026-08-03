#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# ─── How to run ───
# 1. Install uv (if not installed):
#      curl -LsSf https://astral.sh/uv/install.sh | sh
# 2. Run directly (no venv, no pip install needed):
#      uv run count_prompt_chars.py path/to/prompt.txt
# 3. Or make executable and run:
#      chmod +x count_prompt_chars.py && ./count_prompt_chars.py path/to/prompt.txt
# ──────────────────

from __future__ import annotations

import sys
from pathlib import Path
from typing import Final

MAX_CHARACTERS: Final = 5_000


def normalize_line_breaks(text: str) -> str:
    """Normalize platform line endings to one logical character each."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def count_prompt_characters(text: str) -> int:
    """Count Unicode code points, including spaces and logical line breaks."""
    return len(normalize_line_breaks(text))


def main() -> int:
    """Print the prompt count and fail when it exceeds the hard limit."""
    if len(sys.argv) != 2:
        print("Usage: count_prompt_chars.py path/to/prompt.txt", file=sys.stderr)
        return 2

    prompt_path = Path(sys.argv[1])
    try:
        prompt = prompt_path.read_bytes().decode("utf-8")
    except OSError as error:
        print(f"Unable to read {prompt_path}: {error}", file=sys.stderr)
        return 2
    except UnicodeDecodeError as error:
        print(f"Prompt is not valid UTF-8: {error}", file=sys.stderr)
        return 2

    count = count_prompt_characters(prompt)
    print(f"{count}/{MAX_CHARACTERS}")
    return 0 if count <= MAX_CHARACTERS else 1


if __name__ == "__main__":
    raise SystemExit(main())
