from marshmallow import Schema, fields, validate
from string import ascii_lowercase, ascii_uppercase

class RegisterSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=20))
    password = fields.Str(
        required=True,
        validate=validate.And(
            validate.Length(min=8, max=50),
        ),
        error_messages={
            "validator_failed": "Password must have length of 8-50 characters"
        }
    )


class LoginSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=20))
    password = fields.Str(required=True, validate=validate.Length(min=8, max=50))
