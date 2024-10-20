from chessmate.models.base import db
from chessmate.models.player import Player
from chessmate.models.user import User
from sqlalchemy.exc import SQLAlchemyError

def query_players(tournament_id: int):
    try:
        players =  db.session.query(
            Player.id,
            User.id.label('user_id'),
            User.username
        ).join(
            User, User.id == Player.user_id, isouter=True
        ).filter(Player.tournament_id == tournament_id).all()
    except SQLAlchemyError:
        return None #TODO: Error handling
    return players

def query_player(player_id: int):
    try:
        player =  db.session.query(
            Player.id,
            User.id.label('user_id'),
            User.username
        ).join(
            User, User.id == Player.user_id, isouter=True
        ).one_or_none()
    except SQLAlchemyError:
        return None #TODO: Error handling
    return player


def create_player(user: User, tournament_id: int):
    new_player = Player(tournament_id=tournament_id, user_id=user.id)
    try:
        db.session.add(new_player)
        db.session.commit()
    except SQLAlchemyError as e:
        print(e)
        return None #TODO: Error handling
    return new_player

def remove_player(user: User, player_id: int, tournament_id: int):
    player = db.session.query(Player).filter(Player.id == player_id).one_or_none()
    if not player:
        print('player not found')
        return #TODO: Error handling
    if player.is_remove_allowed(user, tournament_id):
        db.session.delete(player)
        db.session.commit()
    else:
        print('forbidden')
        return #TODO: Errror handling