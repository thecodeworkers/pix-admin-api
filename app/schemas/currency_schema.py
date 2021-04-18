from marshmallow import Schema, fields

class SaveCurrencyInput(Schema):
    name = fields.Str(required=True)
    color = fields.Str(required=True)
    gradients = fields.List(fields.Str())
    active = fields.Bool()
    type = fields.Str(required=True)
    symbol = fields.Str(required=True)
    price = fields.Float()
