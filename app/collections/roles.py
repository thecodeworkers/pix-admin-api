from mongoengine import Document, StringField, ListField, DateTimeField
from bson import json_util
from ..config.constant import DATABASE_USERS
import datetime

class Roles(Document):
    name = StringField(min_length=2, max_length=255, required=True, unique=True)
    code = StringField(min_length=1, max_length=4, required=True, unique=True)
    description = StringField(max_length=300)
    scopes = ListField(StringField(max_length=100))
    created_at = DateTimeField()

    meta = {'db_alias': DATABASE_USERS}

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        return super(Roles, self).save(*args, **kwargs)

    def to_json(self):
        data = self.to_mongo()
        data['created_at'] = self.created_at.isoformat()

        return json_util.dumps(data)
