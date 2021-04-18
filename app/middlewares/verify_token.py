from flask import request
from flask.globals import session
from ..config.constant import APP_KEY, APP_SECRET, JWT_SECRET, JWT_ALGORITHM
from ..utils import api_abort, get_item_list, parser_one_object
from ..config.keys import verify_application_token
from ..collections.users import Users
import jwt

def verify_app_token():
    try:
        headers = request.headers
        if 'X-Api-Key' not in headers:
            raise Exception('Please provide the app token')

        token = headers['X-Api-Key']

        if not verify_application_token(APP_KEY, APP_SECRET, token):
            raise Exception('Token is invalid')

        pass

    except Exception as e:
        api_abort(401, e)

def verify_user_token():
    try:
        headers = request.headers
        common_message = 'Please provide the user token'

        if 'Authorization' not in headers:
            raise ReferenceError(common_message)

        token = headers['Authorization']

        if not token:
            raise ReferenceError(common_message)

        access_token = get_item_list(token.split(' '), 1)

        if not access_token:
            raise ReferenceError(common_message)

        payload = jwt.decode(access_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = Users.objects.get(email=payload['sub'])
        session['user'] = parser_one_object(user)

        pass

    except jwt.ExpiredSignatureError:
        api_abort(401, 'Token expired')
    except Users.DoesNotExist:
        api_abort(401, 'Unauthorized')
    except ReferenceError as re:
        api_abort(401, re)
    except Exception as ex:
        api_abort(500, ex)
