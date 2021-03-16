#!/usr/bin/env python3
'''
an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will
spawn wait_random n times with the specified max_delay
'''
import time
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    return the list of all the delays (float values). The list of the
    delays should be in ascending order without using sort() because of
    concurrency
    '''
    return asyncio.create_task(wait_random(max_delay))
