#!/usr/bin/env python3
"""Everything is documented"""
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Everything is documented"""
    myList = asyncio.run(wait_n(n, max_delay))
    myFloat = 0.0
    for i in myList:
        myFloat += i
    return myFloat/n
