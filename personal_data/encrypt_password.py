#!/usr/bin/env python3
""" encrypting the password """

import bcrypt


def hash_password(password: str) -> bytes:
    """ encrypt a password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ check if the password is valid """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)