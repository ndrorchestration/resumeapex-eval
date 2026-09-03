from __future__ import annotations

import numpy as np


def bootstrap_ci(values: list[float], *, seed: int, confidence: float = 0.95, resamples: int = 10_000) -> dict[str, float]:
    if not values:
        raise ValueError("values must not be empty")
    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1")
    if resamples < 1:
        raise ValueError("resamples must be positive")
    data = np.asarray(values, dtype=float)
    rng = np.random.default_rng(seed)
    samples = rng.choice(data, size=(resamples, data.size), replace=True).mean(axis=1)
    alpha = 1.0 - confidence
    lo, hi = np.quantile(samples, [alpha / 2, 1 - alpha / 2])
    estimate = float(data.mean())
    return {
        "estimate": estimate,
        "ci_low": float(lo),
        "ci_high": float(hi),
        "half_width": float((hi - lo) / 2),
        "confidence": confidence,
        "resamples": float(resamples),
        "seed": float(seed),
    }
