from marshmallow import Schema, fields

class SaveRoleInput(Schema):
    name = fields.Str(required=True)
    code = fields.Str(required=True)
    description = fields.Str()
    scopes = fields.List(fields.Str())
