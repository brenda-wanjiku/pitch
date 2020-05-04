from ..models import User,Pitch,Comment
from .forms import UpdateProfile
from flask import render_template,redirect,url_for,abort
from . import main
from .. import db
from flask_login import login_required, current_user



@main.route('/')
def index():
    philosophy = Pitch.get_pitches('Philosophy')



    return render_template('index.html',philosophy = philosophy )


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






