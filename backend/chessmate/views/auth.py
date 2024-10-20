from flask import (Blueprint, g, request, session)
from werkzeug.security import check_password_hash, generate_password_hash
from chessmate.models.base import db
from chessmate.models.user import AuthUser
from chessmate.schemas.auth import RegisterSchema, LoginSchema

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = AuthUser.query.get(user_id)


@auth_bp.post('/register')
def register():
    register_data = RegisterSchema().load(request.json)
    username = register_data['username']
    password = register_data['password']
    try:
        new_user = AuthUser(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
    except db.IntegrityError as e:
        return f"User {username} already exists", 404
    return f'User {username} created', 201
        

@auth_bp.post('/login')
def login():
    login_data = LoginSchema().load(request.json)
    username = login_data['username']
    password = login_data['password']
    user = db.session.query(AuthUser).filter(AuthUser.username == username).one_or_none()
    if not user:
        return 'Incorrect username', 401
    elif user.id == session.get('user_id'):
        return f'User {user.username} is already logged in', 404
    elif not check_password_hash(user.password, password):
        return 'Incorrect password', 401
    session.clear()
    session['user_id'] = user.id
    return 'Logged in', 200


@auth_bp.post('/logout')
def logout():
    if 'user_id' not in session:
        return 'User is not logged in', 404
    session.clear()
    return '', 204

    