#!/usr/bin/env python3


import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n
    '''
    wait_n = __import__('1-concurrent_coroutines').wait_n

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n
