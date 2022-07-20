#!/usr/bin/env python3
""" Module for view definition """
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Optional

# app = Flask(__name__)


class Config(object):
    """ Config class """
    # ...
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


# def create_app(config_class=Config):
#     app = Flask(__name__)
#     babel.init_app(app)
#     app.config.from_object(config_class)
#     return app


@babel.localeselector
def get_locale() -> Optional[str]:
    """ Get preferred local function """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ Index function """
    return render_template('3-index.html')
def create_app(config_class=Config):
    app = Flask(__name__)
    babel.init_app(app)
    app.config.from_object(config_class)
    return app

if __name__ == '__main__':
    app.run(debug=True)
