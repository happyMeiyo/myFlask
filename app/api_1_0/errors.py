#!/usr/bin/env python
# encoding: utf-8

"""
@file: errors.py
@author: ‘Administrator‘
@time: 2017/12/8 21:15
"""

from flask import jsonify
from . import api
from app.exceptions import ValidationError


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status = 400
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status = 403
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status = 401
    return response


def page_not_found(message):
    response = jsonify({'error': 'page_not_found', 'message': message})
    response.status = 404
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])




