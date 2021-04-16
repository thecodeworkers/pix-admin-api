from marshmallow import Schema, fields

class SavePermissionInput(Schema):
    service = fields.Str(required=True)
    methods = fields.List(fields.Str())
