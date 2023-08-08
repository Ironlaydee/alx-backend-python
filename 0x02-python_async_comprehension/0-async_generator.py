#!/usr/bin/env python3
'''The coroutine executes a loop of 10 iterations, 
asynchronously pausing for 1 second during each iteration, 
and subsequently producing a yielded random number ranging from 0 to 10..
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
