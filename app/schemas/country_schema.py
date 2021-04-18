from marshmallow import Schema, fields

class SaveCountryInput(Schema):
    name = fields.Str(required=True)
    code = fields.Str(required=True)
    phone_prefix = fields.Str(required=True)
    active = fields.Bool()
    states = fields.List(fields.Str())
