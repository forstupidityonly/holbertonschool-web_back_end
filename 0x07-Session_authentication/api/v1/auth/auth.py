#!/usr/bin/env python3
"""api auth"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """api auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ensure path not in excluded_paths"""
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
        """fetch the auth header"""
        if not request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""
        return None

    def session_cookie(self, request=None):
        """cookie chef"""
        if request is None:
            return None
        session_name = os.getenv("SESSION_NAME")
        session_id = request.cookies.get(session_name)
        return session_id
