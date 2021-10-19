#!/usr/bin/env python3
"""call wait_random n times"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """the rtn needs to be in assending order? concurrency???"""
    myList = []
    for i in range(6):
        myList.append(asyncio.run(wait_random(max_delay)))
    return myList
