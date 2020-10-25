from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from os import environ

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth_bp.login'
    login_manager.init_app(app)

    # creates the database models
    from .models.user import User
    db.create_all(app=app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # registers blueprints
    from .views.home import home_bp
    app.register_blueprint(home_bp)

    from .views.auth import auth_bp
    app.register_blueprint(auth_bp)

    from .views.profile import profile_bp
    app.register_blueprint(profile_bp)

    from .views.videoconf import videoconf_bp
    app.register_blueprint(videoconf_bp)
    
    from .views.admin import admin
    admin.init_app(app)

    return app
