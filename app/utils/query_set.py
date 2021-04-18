from mongoengine import QuerySet, Document
from bson.json_util import dumps
from .parser import parser_one_object
import datetime

class RefQuerySet(QuerySet):
    def to_json(self):
        data = "[%s]" % (",".join([value.to_json() for value in self]))
        return data

def override_save(instance, Collection, *args, **kwargs):
    if not instance.created_at:
        instance.created_at = datetime.datetime.now()
    return super(Collection, instance).save(*args, **kwargs)

def override_to_json(instance):
    data = instance.to_mongo()

    if 'created_at' in instance:
        data['created_at'] = instance.created_at.isoformat()

    return dumps(data)

def override_list_to_json(instance):
    data = instance.select_related()

    if 'created_at' in data:
        if 'created_at' in instance:
            data.created_at = instance.created_at.isoformat()

    data = {
        key if key != 'id' else '_id': [parser_one_object(old_data) for old_data in data[key] if isinstance(old_data, Document)]
        if isinstance(data[key], list) else str(data[key].id)
        if isinstance(data[key], Document) else data[key] for key in data
    }

    return dumps(data)
