#!/usr/bin/env python3
"""document is anotated`"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return the 10 from async_generator"""
    return [obj async for obj in async_generator()]
