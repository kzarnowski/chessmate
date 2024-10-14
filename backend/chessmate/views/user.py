from flask import Blueprint, jsonify, request

from chessmate.models.user import User
from ..services.user import create_follower, query_user, query_followers, query_following
from ..schemas.user import UserSchema
from .base import login_required

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.get('/<int:user_id>')
def get_user(user_id: int):
    user = query_user(user_id)
    return jsonify(UserSchema().dump(user))


@user_bp.get('<int:user_id>/followers')
def get_followers(user_id: int):
    followers = query_followers(user_id)
    return jsonify(UserSchema().dump(followers, many=True))


@user_bp.get('<int:user_id>/following')
def get_following(user_id: int):
    following = query_following(user_id)
    return jsonify(UserSchema().dump(following, many=True))



@user_bp.post('<int:user_id>/following')
@login_required
def post_follow(user: User, user_id: int):
    if user.id != user_id:
        pass #TODO: Error handling
    following_id = request.json["following_id"]
    create_follower(following_id, user_id)
    return ''
