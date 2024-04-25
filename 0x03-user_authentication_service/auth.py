#!/usr/bin/env python3
"""
Authorization module
"""

import bcrypt
from db import DB, User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashing password and returning it"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


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