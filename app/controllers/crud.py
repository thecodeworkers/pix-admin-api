from flask import request
from marshmallow import ValidationError
from mongoengine.queryset import NotUniqueError
from ..decorators import log_record
from ..utils import *

@log_record
def table_record(pipeline, sort_criteria, Collection, service, method):
    try:
        valid_scope(service, method)
        search, page, per_page = unpack_url_params()

        pipeline = pipeline(search) + pagination(page, per_page, sort_criteria)
        results = Collection.objects().aggregate(pipeline)
        results = default_paginate_schema(results, page, per_page)

        return success_operation(service, method, results)

    except Exception as err:
        return rewrite_exception(service, method, err)

@log_record
def get_record(id, Collection, service, method):
    try:
        valid_scope(service, method)
        document = Collection.objects.get(id=id)
        document = parser_one_object(document)

        return success_operation(service, method, document)

    except Collection.DoesNotExist as dne:
        return error_operation(service, method, 404, dne)
    except Exception as ex:
        return rewrite_exception(service, method, ex)

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
    except Exception as ex:
        return rewrite_exception(service, method, ex)

@log_record
def update_record(id, Schema, Collection, service, method):
    try:
        valid_scope(service, method)

        schema = Schema()
        document = schema.load(request.json)

        data = Collection.objects(id=id)
        if data: document['id'] = id

        data = Collection(**document).save()
        data = parser_one_object(data)

        return success_operation(service, method, data)

    except ValidationError as ve:
        return error_operation(service, method, 400, ve)
    except NotUniqueError as nue:
        return error_operation(service, method, 422, nue)
    except Exception as ex:
        return rewrite_exception(service, method, ex)

@log_record
def delete_record(id, Collection, service, method):
    try:
        valid_scope(service, method)
        document = Collection.objects.get(id=id)
        document.delete()

        return success_operation(service, method)

    except Collection.DoesNotExist as dne:
        return error_operation(service, method, 404, dne)
    except Exception as ex:
        return rewrite_exception(service, method, ex)
