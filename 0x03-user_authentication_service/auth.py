#!/usr/bin/env python3
"""
Authorization module
"""

import bcrypt
from db import DB, User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """Hashing password and returning it"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """generating uuid"""
    return str(uuid4())


class Auth:
    """Auth representation"""

    def __init__(self):
        """Instantiation of the class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method that registers users"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validating login"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if bcrypt.checkpw(password.encode(), user.hashed_password):
            return True
        else:
            return False
   
    def create_session(self, email: str) -> str:
        """Creating a session"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
