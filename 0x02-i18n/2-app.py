#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


def get_locale():
    """determine language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Renders a basic html template
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
