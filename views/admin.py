from flask import Blueprint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from ..app import db
from ..models.user import User

admin_page = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

admin = Admin(template_mode='bootstrap3')

# adds the different database models to the Admin panel
admin.add_view(ModelView(User, db.session))