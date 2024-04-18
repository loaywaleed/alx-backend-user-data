#!/usr/bin/env python3
"""
Authorization module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Authorization functionalities class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth public method handling"""
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """Current logged in user"""
        return None
