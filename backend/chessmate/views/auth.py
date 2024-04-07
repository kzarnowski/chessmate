from flask import (Blueprint, g, request, session)
from werkzeug.security import check_password_hash, generate_password_hash
from ..models.base import db
from ..models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)
        print(type(g.user))


@auth_bp.post('/register')
def register():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    error = None 
    if username and password:
        try:
            new_user = User(username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
        except db.IntegrityError as e:
            error = f"User {username} already exists"
        else:
            return f'User {username} created', 201
    elif not username:
        error = 'Username is required'
    else:
        error = 'Password is required'
    if error:
        return error, 404


@auth_bp.post('/login')
def login():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    error = None
    user = db.session.query(User).filter(User.username == username).one_or_none()
    if not user:
        error = 'Incorrect username'
    elif user.id == session.get('user_id'):
        error = f'User {user.username} is already logged in'
    elif not check_password_hash(user.password, password):
        error = 'Incorrect password'
    if error is None:
        session.clear()
        session['user_id'] = user.id
        return 'Logged in', 200
    return error, 401


@auth_bp.post('/logout')
def logout():
    if 'user_id' not in session:
        return 'User is not logged in', 404
    session.clear()
    return '', 204
    