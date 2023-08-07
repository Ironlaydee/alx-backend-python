#!/usr/bin/env python3
'''execute multiple coroutines at the same time with async
'''
import asyncio
from typing import list


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Executes wait_random n times'''
    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await wait_random(max_delay))
        i += 1

    return sorted(delay_list)
