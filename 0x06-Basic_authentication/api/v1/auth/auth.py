#!/usr/bin/env python3
"""api auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    """api auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """used later"""
        return False

    def authorization_header(self, request=None) -> str:
        """used later"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""
        return None

