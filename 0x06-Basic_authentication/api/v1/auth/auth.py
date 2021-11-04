#!/usr/bin/env python3
"""api auth"""
from flask import request

class Auth:
    """api auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """used later"""


    def authorization_header(self, request=None) -> str:
        """no idea"""


    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""
        return None
