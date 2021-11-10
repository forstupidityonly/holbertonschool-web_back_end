#!/usr/bin/env python3
"""session auth"""

from api.v1.auth.auth import Auth


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
