#!/usr/bin/env python3
"""async_generator """


import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """wait one sec and yeald randint 1-10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0.0, 10.0)
