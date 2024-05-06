#!/usr/bin/env python3
"""Module that presents the safe_first_element function with annotations"""
from typing import Sequence
from typing import Optional
from typing import Any
from typing import cast


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Function that returns data of any type"""
    if lst:
        return lst[0]
    else:
        return cast(Optional[Any], None)
