from flask import Blueprint, jsonify

from chessmate.models.user import User
from chessmate.schemas.player import PlayerSchema
from chessmate.services.player import create_player, query_players, remove_player, query_player
from chessmate.views.base import login_required

player_bp = Blueprint('player', __name__, url_prefix='/<int:tournament_id>/players')

@player_bp.get('/')
def get_players(tournament_id: int):
    players = query_players(tournament_id)
    return jsonify(PlayerSchema().dump(players, many=True, exclude=("tournament_id")))

@player_bp.get('/<int:player_id>')
def get_player(tournament_id: int, player_id: int):
    player = query_player(player_id)
    return jsonify(PlayerSchema().dump(player))



@player_bp.post('/')
@login_required
def post_players(user: User, tournament_id: int):
    player = create_player(user=user, tournament_id=tournament_id)
    if not player:
        return 'Error creating player' #TODO: Error handling
    return jsonify({'id': player.id}), 201



@player_bp.delete('/<int:player_id>')
@login_required
def delete_player(user: User, tournament_id: int, player_id: int):
    remove_player(user=user, tournament_id=tournament_id, player_id=player_id)
    return '', 204
    