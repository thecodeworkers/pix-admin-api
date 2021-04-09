from flask import Blueprint, request
from ..config.constant import APP_NAME, APP_KEY
from cryptography.hazmat.primitives import hashes, hmac

bp = Blueprint('keys', __name__, url_prefix='/api/')

@bp.route('/create-keys', methods=['GET'])
def create_key():
    h = hmac.HMAC(APP_KEY.encode('utf-8'), hashes.SHA256())
    token = h.update(APP_NAME.encode('utf-8'))
    token = h.finalize()

    return token.hex()

@bp.route('/verify-keys', methods=['GET'])
def verify_key():
    token = request.args.get('token')
    v = hmac.HMAC(APP_KEY.encode('utf-8'), hashes.SHA256())
    v.update(APP_NAME.encode('utf-8'))
    v.verify(bytes.fromhex(token))

    return 'yes'
