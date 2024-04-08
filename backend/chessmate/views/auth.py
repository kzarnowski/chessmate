from flask import (Blueprint, g, request, session)
from werkzeug.security import check_password_hash, generate_password_hash
from ..models.base import db
from ..models.user import User
from ..schemas.auth import RegisterSchema, LoginSchema

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@auth_bp.post('/register')
def register():
    register_data = RegisterSchema().load(request.json)
    username = register_data['username']
    password = register_data['password']
    try:
        new_user = User(username=username, password=generate_password_hash(password))
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
    user = db.session.query(User).filter(User.username == username).one_or_none()
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
    