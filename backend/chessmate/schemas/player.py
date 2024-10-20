from marshmallow import Schema
from marshmallow.fields import Int, Str

class PlayerSchema(Schema):
    id = Int(dump_only=True)
    user_id = Int(dump_only=True, data_key="userId")
    tournament_id = Int(dump_only=True, data_key="tournamentId")
    username = Str(dump_only=True)
