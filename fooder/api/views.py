# fooder/api/views.py
# Copyright (C) 2014-2015 the Kim authors and contributors
# <see AUTHORS file>
#
# This module is part of Kim and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from flask import Blueprint, jsonify

from fooder.models.food import get_vegetables

api_mod = Blueprint('api', __name__)


@api_mod.route('/')
def home():

    return jsonify({'foo': 'bar'}), 200


@api_mod.route('/vegetables')
def vegetables():

    objs = get_vegetables()
    data = {'objects': [{'id': v.id,
                         'name': v.name,
                         'description': v.description,
                         'category': v.category} for v in objs]}
    return jsonify(data), 200
