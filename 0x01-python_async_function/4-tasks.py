#!/usr/bin/env python3
"""take the code from somwhere and change it
into a new function
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Sexcept task_wait_random is being called."""
    futures = [task_wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
