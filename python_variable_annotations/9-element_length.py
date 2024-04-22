#!/usr/bin/env python3
"""Module that presents the element_length function with annotations"""
from typing import Iterable
from typing import Sequence
from typing import List
from typing import Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that returns a list"""
    return [(i, len(i)) for i in lst]
