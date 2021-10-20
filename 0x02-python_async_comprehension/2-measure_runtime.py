#!/usr/bin/env python3
"""imma use timegates bc i dont know whats going on with the rtn objects"""


import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """timegate like physics"""
    j = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    i = time.time()

    return i - j
