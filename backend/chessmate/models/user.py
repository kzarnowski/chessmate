from sqlalchemy import Integer, String, Column
from .base import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(20), nullable=False)
    password = Column('password', String(50), nullable=False)