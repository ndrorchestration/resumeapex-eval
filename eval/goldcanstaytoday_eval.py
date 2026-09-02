"""Backward-compatible entry point for the Goldcanstaytoday harness."""

try:
    from .cli import main
except ImportError:  # direct ``python eval/goldcanstaytoday_eval.py`` invocation
    from eval.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
