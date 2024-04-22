#!/usr/bin/env python3
"""Module that presents the sum_mixed_list function with annotations"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function that returns the sum of the numbers in the list
    `sum_mixed_list`"""
    return sum(mxd_lst)
