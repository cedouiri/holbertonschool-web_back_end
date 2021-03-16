#!/usr/bin/env python3
'''
an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will
spawn wait_random n times with the specified max_delay
'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    return the list of all the delays (float values). The list of the
    delays should be in ascending order without using sort() because of
    concurrency
    '''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
