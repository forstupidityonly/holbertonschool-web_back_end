#!/usr/bin/env python3
"""commit"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """commit"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
