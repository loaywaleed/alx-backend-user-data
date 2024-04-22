#!/usr/bin/env python3
"""
Basic Authorization module
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class that uses basic auth for authentication"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:

        if authorization_header is Nonee or authorization_header != type(str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1:]
