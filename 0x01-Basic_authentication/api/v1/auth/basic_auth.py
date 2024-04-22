#!/usr/bin/env python3
"""
Basic Authorization module
"""

from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


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
                                           base64_authorization_header: str
                                           ) -> str:
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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Extracting user credentials from header"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        username = decoded_base64_authorization_header.split(":", 1)[0]
        password = decoded_base64_authorization_header.split(":", 1)[1]
        return username, password

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """User object from credentials"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users_list = User.search({'email': user_email})
        except Exception:
            return None

        for user in users_list:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        header = self.authorization_header(request)

        if header is None:
            return None
        base64_header = self.extract_base64_authorization_header

        if base64_header is None:
            return None

        decoded = self.decode_base64_authorization_header(base64_header):

        if decoded is None:
            return None

        user_credentials = self.extract_user_credentials(decoded)

        if user_credentials is None:
            return None

        user_object = self.user_object_from_credentials(
            user_email=user_credentials[0], user_pwd=user_credentials[1])

        return user_object
