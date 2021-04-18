from flask import request
from marshmallow import ValidationError
from mongoengine.queryset import NotUniqueError
from ..decorators import log_record
from ..utils import *

@log_record
def get_record(id, Collection, service, method):
    try:
        valid_scope(service, method)
        document = Collection.objects.get(id=id)
        document = parser_one_object(document)

        return success_operation(service, method, document)

    except Collection.DoesNotExist as dne:
        return error_operation(service, method, 404, dne)
    except ReferenceError as re:
        return error_operation(service, method, 401, re)
    except Exception as ex:
        return error_operation(service, method, 500, ex)

@log_record
def save_record(Schema, Collection, service, method):
    try:
        valid_scope(service, method)

        schema = Schema()
        document = schema.load(request.json)
        instance = Collection(**document).save()
        data = parser_one_object(instance)

        return success_operation(service, method, data)

    except ValidationError as ve:
        return error_operation(service, method, 400, ve)
    except NotUniqueError as nue:
        return error_operation(service, method, 422, nue)
    except ReferenceError as re:
        return error_operation(service, method, 401, re)
    except Exception as ex:
        return error_operation(service, method, 500, ex)

@log_record
def update_record(id, Schema, Collection, service, method):
    try:
        valid_scope(service, method)

        schema = Schema()
        document = schema.load(request.json)
        document = update_or_create(Collection, {'id': id}, document)
        data = parser_one_object(document)

        return success_operation(service, method, data)

    except ValidationError as ve:
        return error_operation(service, method, 400, ve)
    except NotUniqueError as nue:
        return error_operation(service, method, 422, nue)
    except Exception as ex:
        return error_operation(service, method, 500, ex)

@log_record
def delete_record(id, Collection, service, method):
    try:
        valid_scope(service, method)
        document = Collection.objects.get(id=id)
        document.delete()

        return success_operation(service, method)

    except Collection.DoesNotExist as dne:
        return error_operation(service, method, 404, dne)
    except ReferenceError as re:
        return error_operation(service, method, 401, re)
    except Exception as ex:
        return error_operation(service, method, 500, ex)
