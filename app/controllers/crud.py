from flask import request
from ..decorators import log_record
from ..utils import *

@log_record
def save_record(Schema, Collection, service, method):
    try:
        schema = Schema()
        document = schema.load(request.json)
        instance = Collection(**document).save()
        data = parser_one_object(instance)

        return success_operation(service, method, data)

    except Exception as ex:
        return error_operation(service, method, 500, ex)
