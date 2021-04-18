from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField
from ..utils.query_set import RefQuerySet, override_list_to_json, override_save
from ..config.constant import DATABASE_RESOURCES
from .cities import Cities

class States(Document):
    name = StringField(min_length=2, max_length=100, required=True)
    country = ReferenceField('Countries', dbref=False)
    cities = ListField(ReferenceField(Cities, dbref=False))
    created_at = DateTimeField()

    meta = {
        'db_alias': DATABASE_RESOURCES,
        'queryset_class': RefQuerySet
    }

    def save(self, *args, **kwargs):
        return override_save(self, States, *args, **kwargs)

    def to_json(self):
        return override_list_to_json(self)
