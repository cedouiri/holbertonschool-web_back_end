#!/usr/bin/env python3
'''
hdfdfdffd
'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Complex types - string and int/float to tuple
    '''
    return (k, v**2)
