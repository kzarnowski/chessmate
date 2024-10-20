from marshmallow import Schema, fields, validate
from chessmate.schemas.validators import start_date_validator


class TournamentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=5, max=50))
    city = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    country = fields.Str(required=True, validate=validate.Length(min=1, max=20))
    start_date = fields.Date(format='iso', required=True, validate=start_date_validator, data_key="startDate")
    end_date = fields.Date(format='iso', required=True, data_key="endDate")
    admin_id = fields.Int(required=True, data_key="adminId")
