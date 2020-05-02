from flask import render_template
from . import main


@main.route('/')
def index():

    render_template('index.html')