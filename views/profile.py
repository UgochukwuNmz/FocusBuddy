from flask import Blueprint, render_template
from flask_login import login_required, current_user

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/profile')
@login_required
def profile_page():
    return render_template('profile.html', name=current_user.name, major=current_user.major, year=current_user.year,
    class1=current_user.class1, class2=current_user.class2, class3=current_user.class3, class4=current_user.class4,
    class5=current_user.class5, class6=current_user.class6)

# def get_classes():
#     return [current_user.class1, current_user.class2, current_user.class3, current_user.class4, current_user.class5, current_user.class6]

# def get_major():
#     return current_user.major

# def get_year():
#     return current_user.year