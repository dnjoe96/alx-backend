#!/usr/bin/env python3
""" Module for view definition """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user(login_as):
    """ Get user detail from mock database """
    if login_as:
        if id in users.keys():
            return users.get(login_as)
    return None


@app.before_request
def before_request():
    """
    use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ Index function """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
