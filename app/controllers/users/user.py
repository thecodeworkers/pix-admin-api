from flask import Blueprint, request
from marshmallow import ValidationError
from mongoengine import document
from mongoengine.queryset import NotUniqueError
from ...schemas.user_schema import SaveUserInput
from ...decorators.common import log_record
from ...collections.users import Users
from ...collections.roles import Roles
from ...utils import *

bp = Blueprint('user', __name__, url_prefix='/api/')

@bp.route('/users', methods=['POST'])
def save():
    return __save(save.__name__)

@log_record
def __save(method):
    try:
        schema = SaveUserInput()
        payload = schema.load(request.json)

        role = Roles.objects.get(code=payload['role'])
        payload['role'] = role

        payload['password'] = hash_password(payload['password'])
        document = Users(**payload).save()

        return success_operation(__name__, method, parser_one_object(document))

    except ValidationError as ve:
        return error_operation(__name__, method, 400, ve)
    except NotUniqueError as nue:
        return error_operation(__name__, method, 422, nue)
    except Roles.DoesNotExist as dne:
        return error_operation(__name__, method, 404, dne)
    except Exception as ex:
        return error_operation(__name__, method, 500, ex)
