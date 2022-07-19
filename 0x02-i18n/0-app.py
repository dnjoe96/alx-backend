#!/usr/bin/env python3
""" Module for view definition """
from flask import Flask, render_template

app = Flask()


@app.route('/')
def index():
    """ Index function """
    return render_template('index.html')
