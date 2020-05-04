from ..models import User,Pitch
from flask import render_template,redirect,url_for,abort
from . import main
from .. import db
from flask_login import login_required
from ..models import User,Pitch, Comment


@main.route('/')
def index():
    philosophy = Pitch.get_pitches('Philosophy')
    title = 'Peaches'


    return render_template('index.html',title = title, philosophy = philosophy )


@main.route('/pitches/<category>')
def categories(category):
    title = "Category"
   

    return render_template('pitches.html', title = title)

@main.route('/user/<name>')
def profile(uname):
    user = User.query.filter_by(name = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)




