from marshmallow import Schema, fields

class SaveCityInput(Schema):
    name = fields.Str(required=True)
    state = fields.Str()
