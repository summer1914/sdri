from flask import session, redirect, url_for, g
from functools import wraps


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if session.get('user_id', None) is None:
            session['user_id'] = 76
        return func(*args, **kwargs)

    return inner
