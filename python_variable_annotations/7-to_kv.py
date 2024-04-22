#!/usr/bin/env python3
"""Module that presents the to_kv function with annotations"""
from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that returns the string `k` and the square of the
    number `v` inside a tuple"""
    return (k, v**2)
