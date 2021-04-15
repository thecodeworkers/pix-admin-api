from flask import Blueprint, request
from .logger import log_record


bp = Blueprint('auth', __name__, url_prefix='/api/')

@bp.route('/create-keys', methods=['GET'])
def create_key():
    return ''

@bp.route('/verify-keys', methods=['GET'])
def verify_key():
    return __sign_up()


@log_record
def __sign_up():
    return {
        'user_id': '',
        'log_type': 'INFO',
        'service': 'auth',
        'method': 'sign_in',
        'details': {
            'description': 'A user was registered',
            'id': ''
        },
        'response': 'yes'
    }
