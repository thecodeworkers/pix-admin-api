from mongoengine import Document, StringField, BooleanField, ListField, ReferenceField, DateTimeField
from ..utils.query_set import RefQuerySet, override_list_to_json, override_save
from ..config.constant import DATABASE_RESOURCES
from .states import States

class Countries(Document):
    name = StringField(min_length=2, max_length=100, required=True)
    code = StringField(min_length=2, max_length=2, required=True, unique=True, sparse=True)
    phone_prefix = StringField(min_length=2, max_length=10, required=True)
    active = BooleanField(default=True)
    states = ListField(ReferenceField(States, dbref=False))
    created_at = DateTimeField()

    meta = {
        'db_alias': DATABASE_RESOURCES,
        'queryset_class': RefQuerySet
    }

    def save(self, *args, **kwargs):
        return override_save(self, Countries, *args, **kwargs)

    def to_json(self):
        return override_list_to_json(self)
