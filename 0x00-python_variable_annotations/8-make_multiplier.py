#!/usr/bin/env python3
'''
hdfdfdffd
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Complex types - functions

    '''
    def multi_func(x: float) -> float:
        return x * multiplier
    return multi_func
