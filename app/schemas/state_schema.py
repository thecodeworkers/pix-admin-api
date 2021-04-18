from marshmallow import Schema, fields

class SaveStateInput(Schema):
    name = fields.Str(required=True)
    cities = fields.List(fields.Str())
