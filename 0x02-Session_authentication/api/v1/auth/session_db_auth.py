#!/usr/bin/env python3
"""session database auth module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class
    """
    def create_session(self, user_id: str = None) -> str:
        """create_session method
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session = UserSession(user_id=user_id, session_id=session_id)
        session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id method
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        user_session = UserSession.search({"session_id": session_id})
        if user_session is None:
            return None
        if self.session_duration <= 0:
            return user_session.get("user_id")
        if "created_at" not in user_session:
            return None
        if (datetime.now() - user_session.get("created_at")) > timedelta(
                seconds=self.session_duration):
            return None
        return user_session.get("user_id")

    def destroy_session(self, request=None):
        """destroy_session method
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_session = UserSession.search({"session_id": session_cookie})
        if user_session is None:
            return False
        UserSession.remove(user_session.get("id"))
        return True

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id method
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        user_session = UserSession.search({"session_id": session_id})
        if user_session is None:
            return None
        if self.session_duration <= 0:
            return user_session.get("user_id")
        if "created_at" not in user_session:
            return None
        if (datetime.now() - user_session.get("created_at")) > timedelta(
                seconds=self.session_duration):
            return None
        return user_session.get("user_id")

    def destroy_session(self, request=None):
        """destroy_session method
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_session = UserSession.search({"session_id": session_cookie})
        if user_session is None:
            return False
        UserSession.remove(user_session.get("id"))
        return True
