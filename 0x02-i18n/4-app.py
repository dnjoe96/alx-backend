#!/usr/bin/env python3
""" Module for view definition """
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Optional


class Config(object):
    """ Config class """
    # ...
    LANGUAGES = ['en', 'fr']
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
    if request.args.get('locale'):
        locale = request.args.get('locale')
        # print(locale)
        if locale in app.config['LANGUAGES']:
            print(locale)
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ Index function """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
