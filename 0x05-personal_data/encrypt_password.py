#!/usr/bin/env python3
'''
hash password

'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    returns a salted, hashed password, which is a byte string

    '''
    wp = bytes(password, 'utf-8')
    return bcrypt.hashpw(wp, bcrypt.gensalt())
