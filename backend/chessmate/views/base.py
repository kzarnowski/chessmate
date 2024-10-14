import functools
from flask import g

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            return 'Login required', 401
        return view(g.user, *args, **kwargs)
    return wrapped_view
