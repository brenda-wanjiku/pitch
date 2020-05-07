from ..models import User,Pitch,Comment
from .forms import UpdateProfile,AddPitch,AddComment
from flask import render_template,redirect,url_for,abort,request
from . import main
from .. import db,photos
from flask_login import login_required,current_user
import markdown2  




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
    
    if "profile_pic" in request.files:
        filename = photos.save(request.files["profile_pic"])
        file_path = f"photos/{filename}"
        user.profile_pic = file_path
        db.session.commit()
    return redirect(url_for('main.profile', user_id = user_id))


@main.route('/user/<user_id>/new', methods = ["GET","POST"])
@login_required
def add_pitch(user_id):
    form = AddPitch()
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        abort(404)
    title = "Add Pitch"
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category = form.category.data 
    
        new_pitch = Pitch(title = title, content = content, category = category,user_id = user_id, likes=0 ,dislikes=0)
        new_pitch.save_pitch()  

        title = 'New pitch'
        pitches = Pitch.query.all()
      
        return redirect(url_for("main.pitch_category",category = category))
    return render_template("new_pitch.html",form = form, title = title)



@main.route("/<user_id>/profile")
def user(user_id):
    user = User.query.filter_by(id = user_id).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    return render_template("user.html", pitches = pitches, user = user)
 
  
@main.route('/comments/<pitch_id>')
@login_required
def comment(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    comments = Comment.query.filter_by(pitch_id = pitch.id).all()

    return render_template('comment.html', pitch = pitch, comments = comments)



@main.route("/comment/<pitch_id>/<username>", methods = ["GET","POST"])
@login_required
def add_comment(pitch_id, username):
    title = "Add comment"
    user = User.query.filter_by(name = username).first()
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    form = AddComment()
   
    if form.validate_on_submit():
        mention = form.text.data 
        new_comment = Comment(mention = mention, pitch_id = pitch.id, user_id =  user.id )
        new_comment.save_comment()
        return redirect(url_for("main.comment", pitch_id = pitch.id))
    return render_template("new_comment.html",title = pitch.title, user = user, form = form,pitch = pitch)


@main.route('/comments/<pitch_id>/like')
@login_required
def like(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    comments = Comment.query.filter_by(pitch_id = pitch.id).first()
    like = pitch.likes()

    return render_template('comments.html', pitch = pitch, comments = comments, like = like)

@main.route('/comments/<pitch_id>/dislike')
@login_required
def dislike(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    comments = Comment.query.filter_by(pitch_id = pitch.id).first()
    dislike = pitch.dislikes()

    return render_template('comments.html', pitch = pitch, comments = comments, dislike =dislike)










