from flask import Blueprint, jsonify, request
from chessmate.services.tournament import (
    query_tournaments,
    query_tournament,
    create_tournament,
    remove_tournament,
    edit_tournament
)
from chessmate.schemas.tournament import TournamentSchema, EditTournamentSchema
from chessmate.models.user import User
from chessmate.views.base import login_required

tournament_bp = Blueprint('tournament', __name__, url_prefix='/tournaments')

@tournament_bp.get('/')
def get_tournaments():
    tournaments = query_tournaments()
    return jsonify(TournamentSchema().dump(tournaments, many=True))

@tournament_bp.get('/<int:tournament_id>')
def get_tournament(tournament_id: int):
    tournament = query_tournament(tournament_id)
    if not tournament:
        return f'Tournament with id={tournament_id} not found', 404
    return jsonify(TournamentSchema().dump(tournament))


@tournament_bp.post('/')
@login_required
def post_tournaments(user: User):
    tournament_data = TournamentSchema().load(request.json)
    new_tournament = create_tournament(tournament_data)
    return jsonify(TournamentSchema().dump(new_tournament)), 201


@tournament_bp.delete('/<int:tournament_id>')
@login_required
def delete_tournament(user: User, tournament_id: int):
    tournament = query_tournament(tournament_id)
    if not tournament.is_remove_allowed(user):
        print("remove not allowed")
        return #TODO: Error handling
    remove_tournament(tournament, user)
    return '', 204


@tournament_bp.put('/<int:tournament_id>')
@login_required
def put_tournament(user: User, tournament_id: int):
    tournament = query_tournament(tournament_id)
    if not tournament.is_edit_allowed(user):
        print("edit not allowed")
        return #TODO: Error handling
    tournament_data = EditTournamentSchema().load(request.json)
    updated_tournament = edit_tournament(tournament, tournament_data)
    return jsonify(TournamentSchema().dump(updated_tournament))
