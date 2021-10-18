#!/usr/bin/env python3
"""sum_list takes input_list of float's and returns sum"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """list of floats"""
    rtnVal = 0
    for x in input_list:
        rtnVal += x
    return rtnVal
