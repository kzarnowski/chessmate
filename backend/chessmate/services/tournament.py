from typing import List
from chessmate.models.tournament import Tournament
from chessmate.models.user import User
from chessmate.models.base import db
from sqlalchemy.exc import SQLAlchemyError

def query_tournaments() -> List[Tournament]:
    try:
        tournaments = db.session.query(Tournament).all()
    except SQLAlchemyError:
        return None #TODO: Error handling
    return tournaments


def query_tournament(tournament_id: int) -> Tournament:
    try:
        tournament = db.session.query(Tournament).filter(Tournament.id == tournament_id).one_or_none()
    except SQLAlchemyError:
        return None #TODO: Error handling
    if not tournament:
        return None #TODO: Error handling
    return tournament


def create_tournament(tournament_data) -> Tournament:
    tournament = Tournament(**tournament_data)
    try:
        db.session.add(tournament)
        db.session.commit()
    except SQLAlchemyError:
        return None #TODO: Error handling
    return tournament

def remove_tournament(tournament: Tournament, user: User) -> None:
    try:
        db.session.delete(tournament)
        db.session.commit()
    except SQLAlchemyError:
        return #TODO: Error handling

def edit_tournament(tournament: Tournament, tournament_data: dict) -> Tournament:
    try:
        for field, value in tournament_data.items():
            setattr(tournament, field, value)
        db.session.commit()
    except SQLAlchemyError as e:
        print(e)
        return #TODO: Error handling
    return tournament