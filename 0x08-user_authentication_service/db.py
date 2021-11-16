#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """The method should save the user to the database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """rtn the first row found in users as filtered by keyword"""
        if not kwargs:
            raise InvalidRequestError
        result = self._session.query(User).filter_by(**kwargs).first()
        if not result:
            raise NoResultFound
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """use find_user by id then update using kwargs"""
        user = self.find_user_by(id=user_id)
        validVals = ['id', 'email', 'hashed_password', 'session_id',
                     'reset_token']
        for key, val in kwargs.items():
            if key not in validVals:
                raise ValueError
            setattr(user, key, val)
            self._session.commit()
