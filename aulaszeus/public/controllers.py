# -*- coding: utf-8 -*-
"""
    aulaszeus.public.controllers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    aulaszeus public controllers module

    :copyright: (c) 2016 by Haynesss.
    :license: BSD, see LICENSE for more details.
"""
from flask import render_template, Blueprint

blueprint = Blueprint('public', __name__)


@blueprint.route('/')
def home():
    """return user profle."""
    return render_template('public/index.html')