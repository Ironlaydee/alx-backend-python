#!/usr/bin/env python3
""" a function do not create an async function
that takes an integer and returns an asyncio task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
