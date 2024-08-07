from .base import db
from sqlalchemy import Column, Integer

class Follower(db.Model):
    __tablename__ = 'follower'

    user_id = Column('user_id', Integer, nullable=False, primary_key=True)
    follower_id = Column('follower_id', Integer, nullable=False, primary_key=True)

