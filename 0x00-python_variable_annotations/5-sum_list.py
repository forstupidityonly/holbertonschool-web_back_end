#!/usr/bin/env python3
"""sum_list takes input_list of float's and returns sum"""


def sum_list(input_list: list) -> float:
    """list of floats"""
    rtnVal = 0
    for x in input_list:
        rtnVal += x
    return rtnVal
