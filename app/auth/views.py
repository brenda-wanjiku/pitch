from . import auth
from flask import render_template
from ..models import User
from flask import render_template, redirect, url_for,flash
from .forms import LoginForm,RegistrationForm
from flask_login import login_user, logout_user,login_required
from .. import db


@auth.route('/register', methods = ['GET', 'POST'])
def register():
     title = "Sign Up"
     form = RegistrationForm()
     if form.validate_on_submit():
            name = form.username.data
            email = form.email.data
            pass_code = form.password.data
            profile_pic = "default.png"
            bio = "No bio"
            new_user = User(name = name, email = email, password = pass_code ,profile_pic = profile_pic, bio = bio)
            new_user.save_user()
     
     return render_template('auth/register.html',title = title, registration_form = form)



@auth.route('/login', methods = ['GET', 'POST'])
def login():
    title = "Sign in"
    
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()

        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(url_for('main.index', user = user))
        flash('Invalid username or password')
    return render_template('auth/login.html',title = title, login_form = login_form)



@auth.route('/logout')
def logout():
    logout_user()
    flash("Successful Log Out")
    return redirect(url_for("main.index"))