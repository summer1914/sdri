from flask import session, redirect, url_for, g
from functools import wraps


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print (session)
        if session.get('user_id', None) is not None:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return inner
