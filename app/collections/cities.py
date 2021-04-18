from mongoengine import Document, ReferenceField, StringField, DateTimeField
from bson.json_util import dumps
from ..utils.query_set import RefQuerySet
from ..config.constant import DATABASE_RESOURCES

class Cities(Document):
    name = StringField(min_length=2, max_length=100, required=True)
    state = ReferenceField('States', dbref=False)
    created_at = DateTimeField()

    meta = {
        'db_alias': DATABASE_RESOURCES,
        'queryset_class': RefQuerySet
    }

    def to_json(self):
        data = self._data

        data['state'] = str(data['state'].id)
        data['_id'] = data['id']
        del data['id']

        return dumps(data)
