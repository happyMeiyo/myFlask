#!/usr/bin/env python
# encoding: utf-8

"""
@file: posts.py
@author: ‘Administrator‘
@time: 2017/12/8 21:14
"""
from flask import jsonify, request, g, abort, url_for, current_app
from . import api
from ..models import Post, Permission
from ..decorators import permission_required
from .. import db


@api.route('/posts/', methods=['POST'])
@permission_required(Permission.WRITE_ARTICLES)
def new_post():
    post = Post.from_json(request.json)
    post.author = g.current_user
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 201, \
        {'Location': url_for('api.get_post', id=post.id, _external=True)}