#!/usr/bin/env python3
"""sum_list takes input_list of float's and returns sum"""

from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """list of floats & int"""
    rtnVal = 0
    for x in mxd_lst:
        rtnVal += x
    return rtnVal
