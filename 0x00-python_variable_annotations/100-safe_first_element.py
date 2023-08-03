#!/usr/bin/env python3
"""
Augment that can correct duck-typed annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe first element
    """
    if lst:
        return lst[0]
    else:
        return None
