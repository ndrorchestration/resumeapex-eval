"""Backward-compatible entry point for the Goldcanstaytoday harness.

The executable implementation lives in ``eval.cli`` and ``eval.core``.
"""

from .cli import main


if __name__ == "__main__":
    raise SystemExit(main())
