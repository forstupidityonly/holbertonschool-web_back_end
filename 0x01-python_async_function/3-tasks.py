#!/usr/bin/env python3
"""Everything is documented"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Everything is documented"""
    return asyncio.create_task(wait_random(max_delay))
