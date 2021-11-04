#!/usr/bin/env python3
"""
basic authentication for auth
"""
import binascii
import json
import base64

from api.v1.auth.auth import Auth


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
