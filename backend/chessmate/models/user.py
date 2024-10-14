from sqlalchemy import Integer, String, Column
from .base import db
from .follower import Follower



class User(db.Model):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(20), nullable=False)
    

    def get_followers(self):
        return db.session.query(User.id, User.username).join(Follower).filter(Follower.user_id == self.id)
    
    def get_following(self):
        return db.session.query(User.id, User.username).join(Follower).filter(Follower.follower_id == self.id)

class AuthUser(User):
    password = Column('password', String(50), nullable=False)
