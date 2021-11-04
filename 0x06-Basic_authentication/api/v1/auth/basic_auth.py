#!/usr/bin/env python3
"""
basic authentication for auth
"""
import binascii
import json

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """basic authentication"""
