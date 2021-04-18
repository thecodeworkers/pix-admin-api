from mongoengine import Document, StringField, DecimalField, DateTimeField
from ..utils.query_set import override_save, override_to_json
from ..config.constant import DATABASE_LOGS

class AdminLogs(Document):
    user = StringField()
    ip_address = StringField(required=True)
    log_type = StringField(required=True, choices=('INFO', 'ERROR'))
    service = StringField(required=True)
    method = StringField(required=True)
    details = StringField()
    time_execute = DecimalField(precision=8)
    created_at = DateTimeField()

    meta = {'db_alias': DATABASE_LOGS}

    def save(self, *args, **kwargs):
        return override_save(self, AdminLogs, *args, **kwargs)

    def to_json(self):
        return override_to_json(self)
