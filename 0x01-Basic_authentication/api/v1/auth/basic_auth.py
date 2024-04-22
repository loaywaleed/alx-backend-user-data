#!/usr/bin/env python3
"""
Basic Authorization module
"""

from api.v1.auth.auth import Auth
from base64 import b64decode


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """Decoding the Base64 value in the header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            value = base64_authorization_header.encode('utf-8')
            decoded = b64decode(value)
            decoded_value = decoded.decode('utf-8')
        except BaseException:
            return None
        return decoded_value
