from flask import Blueprint, request
from ...utils import success_operation, error_operation
from ..logger import log_record

bp = Blueprint('auth', __name__, url_prefix='/api/')

@bp.route('/create-keys', methods=['GET'])
def create_key():
    return ''

@bp.route('/verify-keys', methods=['GET'])
@log_record
def sign_in():
    print(__name__)
    return error_operation(
        'auth',
        sign_in.__name__,
        500,
        'error'
    )
    return success_operation(
        'auth',
        sign_in.__name__,
        'token'
    )
