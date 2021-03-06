#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """documentation fill"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def helloWorld():
    """rtn rendertemplate"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """get local"""
    local = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES'])
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    pp.run(host="0.0.0.0", port=5000)
