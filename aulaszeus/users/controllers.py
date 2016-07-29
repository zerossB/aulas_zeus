# -*- coding: utf-8 -*-
"""
    aulaszeus.users.controllers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    aulaszeus user controllers module

    :copyright: (c) 2016 by Haynesss.
    :license: BSD, see LICENSE for more details.
"""
from flask import current_app, render_template, Blueprint, request, flash, \
    redirect, send_file, url_for
from flask_security import login_required, current_user
from flask_wtf import Form
from aulaszeus.users import forms, models

blueprint = Blueprint('users', __name__, url_prefix='/users')

@blueprint.route('/profile')
@login_required
def profile():
    """return user profle."""
    current_app.logger.debug(u'Get profile user.')
    return render_template('users/profile.html')

@blueprint.route('/profile/edit', methods=["GET", "POST"])
@login_required
def profile_edit():
    current_app.logger.debug(u'User Profile Edit.')
    form = forms.ProfileForm(obj=current_user)

    if form.validate_on_submit():
        instance = models.User.objects.get(pk=current_user.pk)
        image_data = request.files.get(form.imagem.name)
        if image_data:
            if instance.imagem:
                instance.imagem.delete()
            instance.imagem.put(image_data)
            del form.imagem
        else:
            del form.imagem

        form.populate_obj(instance)
        instance.save()
        flash('Perfil Atualizado com sucesso!', 'success')
        return redirect(url_for("users.profile"))

    return render_template('users/edit.profile.html', form=form)

@blueprint.route('/profile/image', methods=["GET", "POST"])
@login_required
def profile_image():
    instace = models.User.objects.get_or_404(pk=current_user.pk)
    return send_file(instace.imagem.thumbnail, mimetype='image')
