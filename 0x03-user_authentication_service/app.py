#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, jsonify, request
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
