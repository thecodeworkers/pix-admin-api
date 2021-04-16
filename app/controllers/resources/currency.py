from flask import Blueprint, request
from marshmallow import ValidationError
from mongoengine.queryset import NotUniqueError
from ..crud import save_record, get_record, delete_record
from ...collections.currencies import Currencies
from ...schemas.currency_schema import SaveCurrencyInput
from ...utils.parser import parser_one_object
from ...utils.api import success_operation, error_operation
from ...decorators.common import log_record

bp = Blueprint('currency', __name__, url_prefix='/api/')

@bp.route('/currencies/<id>', methods=['GET'])
def get(id):
    return get_record(id, Currencies, __name__, get.__name__)

@bp.route('/currencies', methods=['POST'])
def save():
    return save_record(SaveCurrencyInput, Currencies, __name__, save.__name__), 201

@bp.route('/currencies/<id>', methods=['PUT'])
def update(id):
    return __update(id, __name__, update.__name__)

@bp.route('/currencies/<id>', methods=['DELETE'])
def delete(id):
    return delete_record(id, Currencies, __name__, delete.__name__), 204

@log_record
def __update(id, service, method):
    try:
        schema = SaveCurrencyInput()
        document = schema.load(request.json)

        data = Currencies.objects(id=id)
        if data: document['id'] = id

        data = Currencies(**document).save()
        data = parser_one_object(data)

        return success_operation(service, method, data)

    except ValidationError as ve:
        return error_operation(service, method, 400, ve)
    except NotUniqueError as nue:
        return error_operation(service, method, 422, nue)
    except Exception as ex:
        return error_operation(service, method, 500, ex)
