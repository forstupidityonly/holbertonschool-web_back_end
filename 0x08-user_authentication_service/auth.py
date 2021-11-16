#!/usr/bin/env python3
"""authentication functions"""
import bcrypt


def _hash_password(password: str) -> str:
    """use bcrypt.hashpw on pswrd"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
