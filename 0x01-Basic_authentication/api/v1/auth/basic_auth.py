#!/usr/bin/env python3
"""
Basic Authorization module
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class that uses basic auth for authentication"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Header extraction method"""

        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]
