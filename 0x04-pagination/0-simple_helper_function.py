#!/usr/bin/env python3
'''
Simple helper function

'''

from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    '''
    a function named index_range that takes two integer
    arguments page and page_size
    '''
    p = page * page_size - page_size
    return (p, p + page_size)
