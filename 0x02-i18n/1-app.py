#!/usr/bin/env python3
""" Module for view definition """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    # ...
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    """ Index function """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
