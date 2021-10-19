#!/usr/bin/env python3
"""commit"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """commit"""
    return [(i, len(i)) for i in lst]
