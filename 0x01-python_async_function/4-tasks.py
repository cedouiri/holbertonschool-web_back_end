#!/usr/bin/env python3
'''
an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will
spawn wait_random n times with the specified max_delay
'''
import random
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    return the list of all the delays (float values). The list of the
    delays should be in ascending order without using sort() because of
    concurrency
    '''
    c = (task_wait_random(max_delay) for i in range(n))
    la = await asyncio.gather(*c)
    return sorted(la)
