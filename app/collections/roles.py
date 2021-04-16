from mongoengine import Document, StringField, ListField, DateTimeField
from ..config.constant import DATABASE_USERS
import datetime

class Roles(Document):
    name = StringField(min_length=2, max_length=255, required=True, unique=True)
    code = StringField(min_length=1, max_length=4, required=True, unique=True)
    description = StringField(max_length=300)
    scopes = ListField(StringField(max_length=100))
    created_at = DateTimeField(default=datetime.datetime.now)

    meta = {'db_alias': DATABASE_USERS}
