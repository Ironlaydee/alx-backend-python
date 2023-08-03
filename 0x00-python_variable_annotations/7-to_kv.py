#!/usr/bin/env python3
"""
 a function type-annotated to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    cast to tuple
    """
    return (k, v**2)
