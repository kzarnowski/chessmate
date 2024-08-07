from flask import Blueprint, jsonify
from ..services.user import query_user, query_followers, query_following
from ..schemas.user import UserSchema
from base import login_required

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



@user_bp.post('<int:user_id/follow')
@login_required
def post_follow(follower_id: int, user_id: int):
    