#!/usr/bin/env python3
"""
a function thattype-annotated sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    return a sum of all nums inside a list
    """
    return sum(mxd_lst)
