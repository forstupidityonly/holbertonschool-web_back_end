#!/usr/bin/env python3
""" """
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ """
    myList = asyncio.run(wait_n(n, max_delay))
    myFloat = 0.0
    for i in myList:
        myFloat += i
    return myFloat/n
