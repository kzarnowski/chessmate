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
    followers = (db.session
        .query(User)
        .join(Follower, User.id == Follower.follower_id)
        .filter(Follower.following_id == user_id)
        .all()
    )
    return followers


def query_following(user_id: int) -> List[User]:
    following = (db.session
        .query(User)
        .join(Follower, User.id == Follower.following_id)
        .filter(Follower.follower_id == user_id)
        .all()
    )
    return following

def create_follower(following_id: int, follower_id: int):
    if following_id == follower_id:
        return #TODO: Error handling
    follower_exists = db.session.query(Follower).filter(
        Follower.follower_id == follower_id,
        Follower.following_id == following_id
    ).one_or_none()
    if (follower_exists):
        return #TODO: Error handling
    follower = Follower(following_id=following_id, follower_id=follower_id)
    db.session.add(follower)
    db.session.commit()

def remove_follower(following_id: int, follower_id: int):
    if following_id == follower_id:
        return #TODO: Error handling
    db.session.query(Follower).filter_by(following_id=following_id, follower_id=follower_id).delete()
    db.session.commit()