#!/usr/bin/env python3
'''
Regex-ing

'''


import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    '''
    Returns a log msg

    '''
    return (separator.join(x if x.split('=')[0] not in fields else re.sub(
        r'=.*', '=' + redaction, x) for x in message.split(separator)))
