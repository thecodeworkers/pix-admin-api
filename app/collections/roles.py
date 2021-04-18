from mongoengine import Document, StringField, ListField, DateTimeField
from ..utils.query_set import override_save, override_to_json
from ..config.constant import DATABASE_USERS

class Roles(Document):
    name = StringField(min_length=2, max_length=255, required=True, unique=True)
    code = StringField(min_length=1, max_length=4, required=True, unique=True)
    description = StringField(max_length=300)
    scopes = ListField(StringField(max_length=100))
    created_at = DateTimeField()

    meta = {'db_alias': DATABASE_USERS}

    def save(self, *args, **kwargs):
        return override_save(self, Roles, *args, **kwargs)

    def to_json(self):
        return override_to_json(self)
