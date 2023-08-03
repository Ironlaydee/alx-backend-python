#!/usr/bin/env python3
"""
a function that type-annotated sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    return a sum of all nums inside a list
    """
    return sum(input_list)
