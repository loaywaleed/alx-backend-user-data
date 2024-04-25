#!/usr/bin/env python3
"""
Authorization module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashing password and returning it"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
