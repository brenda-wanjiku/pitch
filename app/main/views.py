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

@main.route('/pitches/<category>', methods = ['GET','POST'])
def pitch_count(id):
    pitch = Pitch.get_pitch(id)
    posted_date = pitch.posted.strftime('%b %d, %Y')

    if request.args.get("likes"):
        pitch.likes = pitch.likes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))


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


@main.route('/user/<name>/new', methods = ["GET","POST"])
@login_required
def add_pitch(name):
    form = AddPitch()
    user = User.query.filter_by(name = name).first()
    if user is None:
        abort(404)
    title = "Add Pitch"
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category = form.category.data 
    
        new_pitch = Pitch(title = title, content = content, category = category,name = name, likes=0 ,dislikes=0)
        new_pitch.save_pitch()  

        title = 'New pitch'
        pitches = Pitch.query.all()
      
        return redirect(url_for("main.get_category",category = category))
    return render_template("new_pitch.html",form = form, title = title)








