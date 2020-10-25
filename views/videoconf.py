import os
from dotenv import load_dotenv
from flask import Flask, Blueprint, render_template, request, abort
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from flask_login import current_user

load_dotenv()
twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_api_key_sid = os.environ.get('TWILIO_API_KEY_SID')
twilio_api_key_secret = os.environ.get('TWILIO_API_KEY_SECRET')

videoconf_bp = Blueprint("videoconf_bp", __name__)

@videoconf_bp.route("/videoconf")
def videoconf_page():
    return render_template("videoconf.html", name=current_user.name)

@videoconf_bp.route('/gettoken', methods=['POST'])
def gettoken():
    username = request.get_json(force=True).get('username')
    if not username:
        abort(401)

    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity=username)
    token.add_grant(VideoGrant(room='My Room'))

    return {'token': token.to_jwt().decode()}

    