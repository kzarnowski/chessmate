from sqlalchemy import Column, Integer, String, Date
from chessmate.models.base import db
from chessmate.models.user import User
from datetime import datetime

class Tournament(db.Model):
    __tablename__ = 'tournament'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50), nullable=False, unique=True)
    city = Column('city', String(20), nullable=False)
    country = Column('country', String(20), nullable=False)
    start_date = Column('start_date', Date, nullable=False)
    end_date = Column('end_date', Date, nullable=False)
    admin_id = Column('admin_id', Integer, nullable=False)

    def is_remove_allowed(self, user: User):
        return user.id == self.admin_id
    
    def is_edit_allowed(self, user: User):
        return user.id == self.admin_id and datetime.today().date() < self.start_date

    def __repr__(self):
        return f"Tournament: {self.id} {self.name}"