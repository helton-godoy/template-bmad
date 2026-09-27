#!/usr/bin/env python3
"""Compat shim (deprecated) — use 02_validate_translations.py.

This file used to be a ~300-line duplicate of 02_validate_translations.py.
It now delegates to the canonical script so both entry points behave
identically on every platform (git symlinks break on Windows checkouts).
"""
import runpy
from pathlib import Path

if __name__ == "__main__":
    runpy.run_path(
        str(Path(__file__).with_name("02_validate_translations.py")),
        run_name="__main__",
    )
