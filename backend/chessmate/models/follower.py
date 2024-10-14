from .base import db
from sqlalchemy import Column, Integer

class Follower(db.Model):
    __tablename__ = 'follower'

    following_id = Column('following_id', Integer, nullable=False, primary_key=True)
    follower_id = Column('follower_id', Integer, nullable=False, primary_key=True)
