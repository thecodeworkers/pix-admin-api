from flask import Blueprint, request
from ..config.keys import verify_application_token

bp = Blueprint('keys', __name__, url_prefix='/api/')

@bp.route('/create-keys', methods=['GET'])
def create_key():
    return ''

@bp.route('/verify-keys', methods=['GET'])
def verify_key():
    return 'yes'
