#!/usr/bin/env python3
"""authentication functions"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> str:
    """use bcrypt.hashpw on pswrd"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """function to make uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register_user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} alredy exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """credintals validator"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """make a session for user"""
        try:
            find_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        self._db.update_user(find_user.id, session_id=_generate_uuid())
        return find_user.session_id

    def get_user_from_session_id(self, session_id: str) -> None:
        """get user from id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """set session id to none"""
        if user_id is None:
            return None
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Reset Password Token"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        uuid = _generate_uuid()
        user.reset_token = uuid
        return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update Password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed = _hash_password(password)
        user.hashed_password = hashed
        user.reset_token = None
