#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth = getenv("AUTH_TYPE")

if auth == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.before_request
def before_request():
    """before_request handler
    """
    if auth is None:
        pass
    else:
        setattr(request, "current_user", auth.current_user(request))
        exluded = ['/api/v1/status/',
                   '/api/v1/unauthorized/', '/api/v1/forbidden/',
                   '/api/v1/auth_session/login/']
        if auth.require_auth(request.path, exluded):
            if auth.authorization_header(request) is None and\
                    auth.session_cookie(request) is None:
                abort(401)
            if auth.current_user(request) is None:
                abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """unauthorized handler
    return: str of key error with value Unauthorized when
    401 response detected
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """forbidden access to a site
    return: str of key error with value forbidden
    403 request used
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
