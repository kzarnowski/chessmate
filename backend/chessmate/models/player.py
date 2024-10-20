from chessmate.models.base import db
from chessmate.models.user import User
from chessmate.models.tournament import Tournament
from sqlalchemy import Column, Integer, Table

class Player(db.Model):
    __tablename__ = 'player'

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, nullable=False)
    tournament_id = Column('tournament_id', Integer, nullable=False)

    def is_remove_allowed(self, user: User, tournament_id: int):
        if self.user_id == user.id:
            return True
        tournament = db.session.query(Tournament).filter(Tournament.id == self.tournament_id).one_or_none()
        if not tournament:
            return False #TODO: Error handling: tournament not found
        return self.tournament_id == tournament_id and user.id == tournament.admin_id
