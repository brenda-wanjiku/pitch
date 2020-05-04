from . import auth
from flask import render_template
from ..models import User
from flask import render_template, redirect, url_for
from .forms import LoginForm,RegistrationForm
from flask_login import login_user, logout_user,login_required
from .. import db


@auth.route('/register', methods = ['GET', 'POST'])
def register():
     form = RegistrationForm()
     if form.validate_on_submit():
        name = form.username.data
        email = form.email.data
        pass_code = form.password.data
        profile_pic = "default.png"
        bio = "No bio"
        new_user = User(name = name, email = email, password = pass_code ,profile_pic = profile_pic, bio = bio)
        new_user.save_user()
        title = "Sign Up"
     return render_template('auth/register.html', registration_form = form, title = title)



@auth.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))

        flash('Invalid username or password')

    title = 'LOG IN'
    return render_template('auth/login.html', login_form = login_form, title = title)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Successful Log Out")
    return redirect(url_for("main.index"))