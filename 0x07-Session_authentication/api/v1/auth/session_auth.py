#!/usr/bin/env python3
"""session auth"""

from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """session auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """make session id for user"""
        if user_id is None or type(user_id) is not str:
            return None
        Session_ID = str(uuid4())
        self.user_id_by_session_id[Session_ID] = user_id
        return Session_ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user id for session id"""
        if session_id is None or type(session_id) is not str:
            return None
        User_ID = self.user_id_by_session_id.get(session_id)
        return User_ID

    def current_user(self, request=None):
        """current user"""
        seshCookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(seshCookie)
        return User.get(user_id)
