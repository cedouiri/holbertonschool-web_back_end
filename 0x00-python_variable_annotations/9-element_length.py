#!/usr/bin/env python3


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Let's duck type an iterable object

    '''
    return [(i, len(i)) for i in lst]
