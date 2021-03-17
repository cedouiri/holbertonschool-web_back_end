#!/usr/bin/env python3

'''
coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
'''


import random
import asyncio
import time


async_generator = __import__('0-async_generator').async_generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    measure_runtime should measure the total runtime and return it.
    Notice that the total runtime is roughly 10 seconds, explain it to yourself
    '''
    t = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    r = time.perf_counter() - t
    return r
