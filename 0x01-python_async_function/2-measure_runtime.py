#!/usr/bin/env python3

import asyncio
import time

async def measure_time(n: int, max_delay: int) -> float:
    '''Computes the average runtime of wait_n
    '''
    wait_n = __import__('1-concurrent_coroutines').wait_n

    total_time = 0.0
    for _ in range(n):
        start_time = time.time()
        await wait_n(1, max_delay)
        total_time += time.time() - start_time

    return total_time / n

if __name__ == "__main__":
    n = 5  # Number of times to measure
    max_delay = 5  # Maximum delay value
    average_runtime = asyncio.run(measure_time(n, max_delay))
    print(f"Average runtime per iteration: {average_runtime:.4f} seconds")

