from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from ..models.user import User
from ..app import db
from .forms import LoginForm, RegisterForm

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('login.html', form=form)

# verifies user login information 
@auth_bp.route('/login', methods=['POST'])
def login_post():
    form = LoginForm(request.form)
    email = form.email.data
    password = form.password.data
    remember = form.remember.data

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth_bp.login'))

    login_user(user, remember=remember)

    return redirect(url_for('profile_bp.profile_page'))

@auth_bp.route('/signup')
def signup():
    form = RegisterForm(request.form)
    return render_template('signup.html', form=form)

# registers the new user into the database
@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    form = RegisterForm(request.form)
    email = form.email.data
    name = form.name.data
    password = form.password.data
    major = form.major.data
    year = form.year.data
    class1 = form.class1.data
    class2 = form.class2.data
    class3 = form.class3.data
    class4 = form.class4.data
    class5 = form.class5.data
    class6 = form.class6.data

    user = User.query.filter_by(email=email).first()
    
    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth_bp.login'))
    
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'),
        major=major, year=year, class1=class1, class2=class2, class3=class3, class4=class4, class5=class5,
        class6=class6)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth_bp.login'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_bp.home_page'))