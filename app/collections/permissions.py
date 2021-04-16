from mongoengine import Document, StringField, ListField
from ..config.constant import DATABASE_USERS

class Permissions(Document):
    service = StringField(min_length=2, max_length=255, required=True, unique=True)
    methods = ListField(StringField(max_length=100))

    meta = {'db_alias': DATABASE_USERS}
