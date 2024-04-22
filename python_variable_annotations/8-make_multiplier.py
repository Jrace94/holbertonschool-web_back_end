#!/usr/bin/env python3
"""Module that presents the make_multiplier function with annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that returns another function"""

    def func(n: float) -> float:
        """
        Function that returns the decimal multiplication
        between `n` and `multiplier`
        """
        return float(n * multiplier)

    return func
