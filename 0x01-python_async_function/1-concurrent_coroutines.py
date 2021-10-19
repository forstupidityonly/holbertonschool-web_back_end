#!/usr/bin/env python3
"""call wait_random n times"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """the rtn needs to be in assending order? concurrency???"""
    i = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    j = [await i for i in asyncio.as_completed(i)]
    return j
