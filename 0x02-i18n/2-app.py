#!/usr/bin/env python3
""" Module for view definition """
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Optional

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class """
    # ...
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale() -> Optional[str]:
    """ Get preferred local function """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ Index function """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
