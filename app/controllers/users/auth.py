from flask import Blueprint, request
from marshmallow import ValidationError
from ...schemas.auth_schema import SignInInput
from ...collections.users import Users
from ...decorators import log_record
from ...utils import *

bp = Blueprint('auth', __name__, url_prefix='/api/')

@bp.route('/signin', methods=['POST'])
def signin():
    return __signin(signin.__name__)

@log_record
def __signin(method):
    try:
        schema = SignInInput()
        payload = schema.load(request.json)

        auth = __get_user_auth({'email': payload['username']})
        if not auth: auth = __get_user_auth({'username': payload['username']})
        if not auth: return error_operation(__name__, method, 404, 'User nor exist')

        if not verify_password(auth['password'], payload['password']):
            return error_operation(__name__, method, 404, 'Password not match')

        user = {
            'email': auth['email'],
            'username': auth['username'],
            'authToken': 'token'
        }

        return success_operation(__name__, method, user)

    except ValidationError as ve:
        return error_operation(__name__, method, 400, ve)
    except Exception as ex:
        return error_operation(__name__, method, 500, ex)

def __get_user_auth(criteria):
    return Users.objects(**criteria).first()
