#!/usr/bin/env python3
"""flask app"""
from auth import Auth
from flask import Flask, jsonify, request, abort

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def taskSix() -> str:
    """task six"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """regester user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email alredy registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """logout user"""
    cookie_session = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(cookie_session)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
