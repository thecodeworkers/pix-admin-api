from flask import Blueprint, request
from flask.globals import session
from marshmallow import ValidationError
from mongoengine.queryset import NotUniqueError
from ..crud import get_record
from ...schemas.user_schema import SaveUserInput
from ...decorators.common import log_record
from ...collections.users import Users
from ...collections.roles import Roles
from ...utils import *

bp = Blueprint('user', __name__, url_prefix='/api/')

@bp.route('/users/<id>', methods=['GET'])
def get(id):
    return get_record(id, Users, __name__, get.__name__)

@bp.route('/users', methods=['POST'])
def save():
    return __save(save.__name__), 201

@bp.route('/users/<id>', methods=['PUT'])
def update(id):
    return __update(id, update.__name__)

@bp.route('/users/<id>', methods=['DELETE'])
def delete(id):
    return __delete(id, delete.__name__), 204

@log_record
def __save(method):
    try:
        valid_scope(__name__, method)

        schema = SaveUserInput()
        payload = schema.load(request.json)

        role = Roles.objects.get(code=payload['role'])
        payload['role'] = role

        payload['password'] = hash_password(payload['password'])
        document = Users(**payload).save()

        return success_operation(__name__, method, parser_one_object(document)), 201

    except ValidationError as ve:
        return error_operation(__name__, method, 400, ve)
    except NotUniqueError as nue:
        return error_operation(__name__, method, 422, nue)
    except Roles.DoesNotExist as dne:
        return error_operation(__name__, method, 404, dne)
    except Exception as ex:
        return rewrite_exception(__name__, method, ex)

@log_record
def __update(id, method):
    try:
        valid_scope(__name__, method)

        schema = SaveUserInput()
        document = schema.load(request.json)

        role = Roles.objects.get(code=document['role'])
        document['role'] = role

        data = Users.objects(id=id)
        if data: document['id'] = id

        document['password'] = hash_password(document['password'])
        data = Users(**document).save()
        data = parser_one_object(data)

        return success_operation(__name__, method, data)

    except ValidationError as ve:
        return error_operation(__name__, method, 400, ve)
    except NotUniqueError as nue:
        return error_operation(__name__, method, 422, nue)
    except Roles.DoesNotExist as dne:
        return error_operation(__name__, method, 404, dne)
    except Exception as ex:
        return rewrite_exception(__name__, method, ex)

@log_record
def __delete(id, method):
    try:
        valid_scope(__name__, method)
        document = Users.objects.get(id=id)
        user = session['user']

        if str(document.id) == user['id']:
            raise Exception('This operation not permited', 403)

        document.delete()

        return success_operation(__name__, method)

    except Users.DoesNotExist as dne:
        return error_operation(__name__, method, 404, dne)
    except Exception as ex:
        return rewrite_exception(__name__, method, ex)
