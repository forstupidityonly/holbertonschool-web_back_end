#!/usr/bin/env python3
"""api auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    """api auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """used later"""
        if path is None:
            return True
        else:
            if path[-1] != '/':
                path += '/'
        if not excluded_paths:
            return True
        if path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """used later"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""
        return None
