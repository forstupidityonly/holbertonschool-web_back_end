#!/usr/bin/env python3
"""sum_list takes input_list of float's and returns sum"""

from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """commit"""
    return (k, v**2)
