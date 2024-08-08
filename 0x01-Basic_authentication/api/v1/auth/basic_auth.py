#!/usr/bin/env python3
""" basic auth module
"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """extract_base64_authorization_header method
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """decode_base64_authorization_header method
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            message = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(message)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            base64_authorization_header: str) -> (str, str):
        """extract_user_credentials method
        """
        if base64_authorization_header is None:
            return (None, None)
        if type(base64_authorization_header) is not str:
            return (None, None)
        if ":" not in base64_authorization_header:
            return (None, None)
        credentials = base64_authorization_header.split(":", 1)
        return (credentials[0], credentials[1])
