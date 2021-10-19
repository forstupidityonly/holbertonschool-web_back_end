#!/usr/bin/env python3
"""commit"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """commit"""
    return lambda x: x * multiplier
