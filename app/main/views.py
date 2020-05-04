from ..models import User,Pitch
from flask import render_template,redirect,url_for
from . import main
from .. import db
from flask_login import login_required


@main.route('/')
def index():
    tech = Pitch.get_pitches('Technology')
    title = 'Peaches'


    return render_template('index.html',title = title, tech = tech)


@main.route('/pitches/<category>')
def categories(category):
    title = "Category"
    phil = Pitch.get_pitches('Philosophy')

    return render_template('pitches.html', title = title, phil = phil)






