#!/usr/bin/env python3
"""authentication of password for now"""
import bcrypt


def _hash_password(pswrd: str) -> str:
    """use bcrypt.hashpw on pswrd"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pswrd.encode('utf-8'), salt)
    return hashed
