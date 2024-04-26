#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request, redirect, make_response, abort
from flask import Response
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome() -> Response:
    """Home route"""
    return jsonify(
        {"message": "Bienvenue"}
        )


@app.route("/users", methods=["POST"])
def users():
    """Route for registering users"""
    email = request.form["email"]
    password = request.form["password"]
    try:
        user = AUTH.register_user(email, password)
        return jsonify(
            {"email": email, "message": "user created"}
            ), 200
    except ValueError:
        return jsonify(
            {"message": "email already registered"}
            ), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> Response:
    """Login route, validates login credentials"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        json_payload = jsonify({"email": email, "message": "logged in"}), 200
        response = make_response(json_payload)
        response.set_cookie("session_id", AUTH.create_session(email))
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> Response:
    """Logs user out and destroys session"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> Response:
    """Obtains user's profile"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """Reset password token route"""
    email = request.form.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify(
        {"email": email, "reset_token": reset_token}
        ), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
