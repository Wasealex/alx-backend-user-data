#!/usr/bin/env python3
"""session_exp_auth module
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class
    """
    def __init__(self):
        """Constructor
        """
        self.session_duration = getenv("SESSION_DURATION")
        if self.session_duration is None or \
                not self.session_duration.isdigit():
            self.session_duration = 0
        else:
            self.session_duration = int(self.session_duration)

    def create_session(self, user_id: str = None) -> str:
        """create_session method
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id method
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get("user_id")
        if "created_at" not in session_dictionary:
            return None
        if (datetime.now() - session_dictionary.get("created_at")) > timedelta(
                seconds=self.session_duration):
            return None
        return session_dictionary.get("user_id")
