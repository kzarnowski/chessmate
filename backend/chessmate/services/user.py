from ..models.base import db
from ..models.user import User
from ..models.follower import Follower
from typing import List


def query_user(user_id: int) -> User:
    user = db.session.query(User).filter(User.id == user_id).one_or_none()
    if not user:
        pass #TODO: Error handling
    return user


def query_followers(user_id: int) -> List[User]:
    followers = db.session.query(Follower).filter(Follower.user_id == user_id).all()
    return followers


def query_following(user_id: int) -> List[User]:
    following = db.session.query(Follower).filter(Follower.follower_id == user_id).all()
    return following