from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "count_prompt_chars.py"


def run_counter(prompt_path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH), str(prompt_path)],
        check=False,
        capture_output=True,
        text=True,
    )


def test_cli_accepts_prompt_when_exactly_at_limit(tmp_path: Path) -> None:
    # Given
    prompt_path = tmp_path / "prompt.txt"
    _ = prompt_path.write_text("가" * 5_000, encoding="utf-8")

    # When
    result = run_counter(prompt_path)

    # Then
    assert result.returncode == 0
    assert result.stdout.strip() == "5000/5000"


def test_cli_rejects_prompt_when_over_limit(tmp_path: Path) -> None:
    # Given
    prompt_path = tmp_path / "prompt.txt"
    _ = prompt_path.write_text("가" * 5_001, encoding="utf-8")

    # When
    result = run_counter(prompt_path)

    # Then
    assert result.returncode == 1
    assert result.stdout.strip() == "5001/5000"


def test_cli_counts_logical_line_breaks_once(tmp_path: Path) -> None:
    # Given
    prompt_path = tmp_path / "prompt.txt"
    _ = prompt_path.write_bytes("가\r\n나\r다\n".encode())

    # When
    result = run_counter(prompt_path)

    # Then
    assert result.returncode == 0
    assert result.stdout.strip() == "6/5000"
