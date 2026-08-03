#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# ─── How to run ───
# 1. Install uv (if not installed):
#      curl -LsSf https://astral.sh/uv/install.sh | sh
# 2. Run directly (no venv, no pip install needed):
#      uv run count_prompt_chars.py path/to/prompt.txt [--limit 4000]
# 3. Or make executable and run:
#      chmod +x count_prompt_chars.py && ./count_prompt_chars.py path/to/prompt.txt
# ──────────────────

from __future__ import annotations

import sys
from pathlib import Path
from typing import Final, NewType

CharacterLimit = NewType("CharacterLimit", int)

DEFAULT_MAX_CHARACTERS: Final = CharacterLimit(5_000)


def normalize_line_breaks(text: str) -> str:
    """Normalize platform line endings to one logical character each."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def count_prompt_characters(text: str) -> int:
    """Count Unicode code points, including spaces and logical line breaks."""
    return len(normalize_line_breaks(text))


def parse_arguments(
    arguments: list[str],
) -> tuple[Path, CharacterLimit] | None:
    """Parse a prompt path and optional positive character limit."""
    if len(arguments) == 1:
        return Path(arguments[0]), DEFAULT_MAX_CHARACTERS

    has_custom_limit = len(arguments) == 3 and arguments[1] == "--limit"
    if has_custom_limit:
        raw_limit = arguments[2]
        if not raw_limit.isdecimal():
            return None

        max_characters = CharacterLimit(int(raw_limit))
        if max_characters <= 0:
            return None

        return Path(arguments[0]), max_characters

    return None


def main() -> int:
    """Print the prompt count and fail when it exceeds the active limit."""
    parsed_arguments = parse_arguments(sys.argv[1:])
    if parsed_arguments is None:
        print(
            "Usage: count_prompt_chars.py path/to/prompt.txt [--limit N]",
            file=sys.stderr,
        )
        return 2

    prompt_path, max_characters = parsed_arguments
    try:
        prompt = prompt_path.read_bytes().decode("utf-8")
    except OSError as error:
        print(f"Unable to read {prompt_path}: {error}", file=sys.stderr)
        return 2
    except UnicodeDecodeError as error:
        print(f"Prompt is not valid UTF-8: {error}", file=sys.stderr)
        return 2

    count = count_prompt_characters(prompt)
    print(f"{count}/{max_characters}")
    return 0 if count <= max_characters else 1


if __name__ == "__main__":
    raise SystemExit(main())
