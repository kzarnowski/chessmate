import functools
from flask import (Blueprint, g, request, session)
from werkzeug.security import check_password_hash, generate_password_hash
from chessmate.db import get_db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    db = get_db()
    if user_id is None:
        g.user = None
    else:
        g.user = db.execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        )


@auth_bp.post('/register')
def register():
    username = request.form.get('username', None)
    password = request.form.get('password', None)
    error = None 
    db = get_db()
    if username and password:
        try:
            db.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, generate_password_hash(password)))
            db.commit()
        except db.IntegrityError:
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
    db = get_db()
    error = None
    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username, )
    ).fetchone()
    if not user:
        error = 'Incorrect username'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password'
    if error is None:
        session.clear()
        session['user_id'] = user['id']
        return 'Logged in', 200
    return error, 401


@auth_bp.post('/logout')
def logout():
    session.clear()
    return '', 204


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return 401
        return view(**kwargs)
    return wrapped_view


    