from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField
from ..utils.query_set import RefQuerySet, override_list_to_json
from ..config.constant import DATABASE_RESOURCES
from .cities import Cities

class States(Document):
    country = ReferenceField('Countries', dbref=False)
    name = StringField(min_length=2, max_length=100, required=True)
    cities = ListField(ReferenceField(Cities, dbref=False))
    created_at = DateTimeField()

    meta = {
        'db_alias': DATABASE_RESOURCES,
        'queryset_class': RefQuerySet
    }

    def to_json(self):
        return override_list_to_json(self)
