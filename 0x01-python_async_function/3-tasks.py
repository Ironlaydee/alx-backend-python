#!/usr/bin/env python3
'''A function that takes an integer and returns an asyncio task
'''
import asyncio

def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Create an asynchronous task for wait_random.
    '''
    wait_random = __import__('0-basic_async_syntax').wait_random

    return asyncio.create_task(wait_random(max_delay))
