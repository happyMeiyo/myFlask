# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     decorators.
   Description :
   Author :       Meiyo
   date：          2017/12/10
-------------------------------------------------
   Change Activity:
                   2017/12/10:
-------------------------------------------------
"""
from functools import wraps
from flask import g
from .errors import forbidden

__author__ = 'Meiyo'


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return decorated_function
    return decorator