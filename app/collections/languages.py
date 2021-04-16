from mongoengine import Document, StringField, BooleanField, DateTimeField
from ..utils.query_set import override_save, override_to_json
from ..config.constant import DATABASE_RESOURCES

class Languages(Document):
    name = StringField(min_length=2,max_length=100, required=True)
    prefix = StringField(min_length=2,max_length=5, required=True, unique=True)
    active = BooleanField(default=True)
    created_at = DateTimeField()

    meta = {'db_alias': DATABASE_RESOURCES}

    def save(self, *args, **kwargs):
        return override_save(self, Languages, *args, **kwargs)

    def to_json(self):
        return override_to_json(self)
