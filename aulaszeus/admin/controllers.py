# -*- coding: utf-8 -*-
"""
    aulaszeus.admin.controllers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    aulaszeus admin controllers module

    :copyright: (c) 2016 by Haynesss.
    :license: BSD, see LICENSE for more details.
"""
from flask import current_app, render_template, Blueprint, jsonify
from flask.ext.security import roles_required
from aulaszeus.users import models

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@roles_required('admin')
@blueprint.route('/users')
def get_users():
    """return users in admin."""
    current_app.logger.debug(u'Get all users in admin.')
    users = models.User.objects()
    return render_template('admin/users/list.html', users=users)

@roles_required('admin')
@blueprint.route('/')
def admin_page():
    """return users in admin."""
    current_app.logger.debug(u'Get all users in admin.')
    return render_template('admin/index.html')

@roles_required('admin')
@blueprint.route('/users/active/<pk>')
def active_user(pk):
    """."""
    user = models.User.objects.get_or_404(pk=pk)
    if user.active:
        user.active = False
    else:
        user.active = True
    user.save()
    return jsonify(data=user.active)
