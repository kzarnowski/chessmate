from typing import List
from ..models.tournament import Tournament
from ..models.base import db

def query_tournaments() -> List[Tournament]:
    return db.session.query(Tournament).all()


def query_tournament(tournament_id: int) -> Tournament:
    tournament = db.session.query(Tournament).filter(Tournament.id == tournament_id).one_or_none()
    if not tournament:
        pass #TODO: Error handling
    return tournament


def create_tournament(tournament_data) -> Tournament:
    tournament = Tournament(**tournament_data)
    db.session.add(tournament)
    db.session.commit()
    return tournament

def remove_tournament(tournament_id: int) -> None:
    tournament = db.session.query(Tournament).filter(Tournament.id == tournament_id).one_or_none()
    if tournament is None:
        return #TODO: Error handling
    if not tournament.is_remove_allowed():
        return #TODO: Error handling
    db.session.delete(tournament)
    db.session.commit()
