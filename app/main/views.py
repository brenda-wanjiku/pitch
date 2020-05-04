from ..models import User,Pitch,Comment
from .forms import UpdateProfile
from flask import render_template,redirect,url_for,abort
from . import main
from .. import db,photos
from flask_login import login_required, current_user




@main.route('/')
def index():
    philosophy = Pitch.get_pitches('Philosophy')



    return render_template('index.html',philosophy = philosophy )


@main.route('/pitches/<category>')
def pitch_category(category):
    title = "Category"
    pitches = Pitch.query.filter_by(category = category).all()

   

    return render_template('pitches.html', title = title, pitches = pitches )


@main.route('/user/<user_id>')
@login_required
def profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    title = user.name.upper()
    return render_template("profile/profile.html", pitches = pitches, user = user,title = title)


@main.route('/user/<user_id>/update',methods = ["GET","POST"])
@login_required
def update_profile(user_id):
    title = "Edit Profile"
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit() 
        return redirect(url_for('main.profile',user_id = user.id)) 
    return render_template("profile/update.html",form = form,title = title)

@main.route('/user/<user_id>/update/pic', methods = ['POST'])
@login_required
def update_pic(user_id):
    title = "Edit Profile"
    user = User.query.filter_by(id = user_id).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic = path
        db.session.commit()
    return redirect(url_for('main.profile', id = user_id))








