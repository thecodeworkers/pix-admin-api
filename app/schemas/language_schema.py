from marshmallow import Schema, fields

class SaveLanguageInput(Schema):
    name = fields.Str(required=True)
    prefix = fields.Str(required=True)
    active = fields.Bool()
