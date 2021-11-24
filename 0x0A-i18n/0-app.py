#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, app, render_template
app = Flask(__name__)


@app.route('/')
def helloWorld():
    """rtn rendertemplate"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
