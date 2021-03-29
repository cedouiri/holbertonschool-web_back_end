#!/usr/bin/env python3
'''
hash password

'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    returns a salted, hashed password, which is a byte string

    '''

    wp = password.encode("utf-8")
    return bcrypt.hashpw(wp, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Implement an is_valid function that expects
    2 arguments and returns a boolean

    '''

    if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
        return True
    else:
        return False
