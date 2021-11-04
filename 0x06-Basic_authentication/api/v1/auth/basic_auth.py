#!/usr/bin/env python3
"""
basic authentication for auth
"""
import binascii
import json
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """basic authentication"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """fetch Base64 in header"""
        if (isinstance(authorization_header, str) and
                authorization_header.startswith('Basic ')):
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode base64"""
        try:
            return base64.b64decode(base64_authorization_header).decode(
                'utf-8')
        except TypeError:
            return None
        except binascii.Error:
            return None

    def extract_user_credentials(self, deco: str) -> (str, str):
        """changed to deco to stay pycodestyle complient"""
        if (not isinstance(deco, str) or ':' not in deco):
            return (None, None)
        return (deco[:deco.find(':')], deco[deco.find(':') + 1:])

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str) -> TypeVar('User'):
        """email and password to make user"""
        if isinstance(user_email, str) and isinstance(user_pwd, str):
            User.load_from_file()
            users_with_email = User.search(
                {'email': user_email})
            if users_with_email:
                for user in users_with_email:
                    if user.is_valid_password(pwd=user_pwd):
                        return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request:"""
        header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(header)
        decode = self.decode_base64_authorization_header(b64)
        user, pwd = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(user, pwd)
