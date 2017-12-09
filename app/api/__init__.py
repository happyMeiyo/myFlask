#!/usr/bin/env python
# encoding: utf-8

"""
@file: __init__.py.py
@author: ‘Administrator‘
@time: 2017/12/8 21:14
"""

from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users, comments, errors

