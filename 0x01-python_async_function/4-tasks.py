#!/usr/bin/env python3
'''change the code into a new function.
'''
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.
    '''
    modified_random = __import__('4-tasks').task_wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await modified_random(max_delay))
        i += 1

    return sorted(delay_list)
