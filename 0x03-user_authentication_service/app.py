#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request, make_response, abort
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
