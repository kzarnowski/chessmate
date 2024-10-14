from marshmallow import ValidationError, validate
from datetime import date

def start_date_validator(start_date: str):
    if start_date < date.today():
        raise ValidationError("Start date must be today or later")
