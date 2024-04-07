from sqlalchemy import Column, Integer, String, Date
from .base import db

class Tournament(db.Model):
    __tablename__ = 'tournament'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50), nullable=False, unique=True)
    city = Column('city', String(20), nullable=False)
    country = Column('country', String(20), nullable=False)
    start_date = Column('start_date', Date, nullable=False)
    end_date = Column('end_date', Date, nullable=False)
    admin_id = Column('admin_id', Integer, nullable=False)

    def __repr__(self):
        return f"Tournament: {self.id} {self.name}"

