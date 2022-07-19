#!/usr/bin/env python3
""" Module for view definition """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Index function """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
