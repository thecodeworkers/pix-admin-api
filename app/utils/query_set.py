from bson import json_util
import datetime

def override_save(instance, Collection, *args, **kwargs):
    if not instance.created_at:
        instance.created_at = datetime.datetime.now()
    return super(Collection, instance).save(*args, **kwargs)

def override_to_json(instance):
    data = instance.to_mongo()
    data['created_at'] = instance.created_at.isoformat()

    return json_util.dumps(data)
