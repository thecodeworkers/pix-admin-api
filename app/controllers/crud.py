from flask import request
from marshmallow import ValidationError
from mongoengine.queryset import NotUniqueError
from ..decorators import log_record
from ..utils import *

@log_record
def get_record(id, Collection, service, method):
    try:
        collection = Collection.objects.get(id=id)
        collection = parser_one_object(collection)

        return success_operation(service, method, collection)

    except Collection.DoesNotExist as dne:
        error_operation(service, method, 404, dne)
    except Exception as ex:
        error_operation(service, method, 500, ex)

@log_record
def save_record(Schema, Collection, service, method):
    try:
        schema = Schema()
        document = schema.load(request.json)
        instance = Collection(**document).save()
        data = parser_one_object(instance)

        return success_operation(service, method, data)

    except ValidationError as ve:
        return error_operation(service, method, 400, ve)
    except NotUniqueError as nue:
        return error_operation(service, method, 422, nue)
    except Exception as ex:
        return error_operation(service, method, 500, ex)
