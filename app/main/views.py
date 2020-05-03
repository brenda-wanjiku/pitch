from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required


@main.route('/')
def index():

    title = 'Peaches'

    return render_template('index.html', title = title)


@main.route('/pitches/<category>')
def categories(category):

    return render_template('pitches.html')


