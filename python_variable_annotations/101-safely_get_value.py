#!/usr/bin/env python3
"""Module that presents the safely_get_value function with annotations"""
from typing import Mapping, TypeVar, Any, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Function that returns data of any type"""
    if key in dct:
        return dct[key]
    else:
        return default
