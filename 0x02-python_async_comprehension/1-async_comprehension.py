#!/usr/bin/env python3
''' Import async_generator from the previous task and write a coroutine called async_comprehension that takes no arguments.'''

from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Creates a list of 10 numbers'''

    return [num async for num in async_generator()]
