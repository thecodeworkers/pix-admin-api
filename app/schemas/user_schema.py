from marshmallow import Schema, fields, validate

class SaveUserInput(Schema):
    email = fields.Str(required=True)
    username = fields.Str()
    password = fields.Str(required=True, validate=validate.Length(min=8))
    role = fields.Str(required=True)
