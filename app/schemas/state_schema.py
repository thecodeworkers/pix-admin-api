from marshmallow import Schema, fields

class SaveStateInput(Schema):
    name = fields.Str(required=True)
    country = fields.Str()
    cities = fields.List(fields.Str())
