#!/usr/bin/env python3
"""flask app"""

from auth import Auth
from flask import Flask, jsonify

AUTH = Auth()
app = Flask(__name__)


@app.route('/', method=['GET'], strict_slashes=False)
def taskSix() -> str:
    """task six"""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
