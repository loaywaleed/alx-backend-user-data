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
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.endswith("*"):
                prefix = excluded_path[:-1]
                if path.startswith(prefix):
                    return False

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """Current logged in user"""
        return None
