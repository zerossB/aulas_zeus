# -*- coding: utf-8 -*-
"""
    aulaszeus.users.forms
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    aulaszeus user forms module

    :copyright: (c) 2016 by Haynesss.
    :license: BSD, see LICENSE for more details.
"""
from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField, \
    FileField, FormField
from wtforms.validators import DataRequired, Email, Length, EqualTo, \
    ValidationError
from flask_security.forms import ConfirmRegisterForm, LoginForm

class CustomLoginForm(LoginForm):
    """Custom LoginForm"""
    email = StringField("Email")
    password = PasswordField("Senha")
    remember = BooleanField("Lembre-se de mim")

class ExtendedRegisterForm(ConfirmRegisterForm):
    """Custom Register Form."""
    fullname = StringField("Nome Completo", validators=[DataRequired(message="O nome Completo é obrigatório")])
    email = StringField("Email", validators=[Email("E-mail é obrigatório")])
    password = PasswordField("Senha", validators=[Length(min=6, max=20,
        message="A senha deve conter de %(min)d á %(max)d caracteres | Dica: Utilize letras, numeros e simbolos" )])
    submit = SubmitField("Registrar")

class AddressRegisterForm(Form):
    tipo = StringField()
    endereco = StringField()
    cidade = StringField()
    estado = StringField()
    bairro = StringField()
    complemento = StringField()
    cep = StringField()
    numero = StringField()

class ProfileForm(Form):
    imagem = FileField('Imagem')
    fullname = StringField('Nome Completo')
    username = StringField('Username')
    endereco = FormField(AddressRegisterForm, default=lambda: {})
    submit = SubmitField("Enviar Dados")

    """def validate_endereco(form, field):
        field.data = {}

    def validate_image(form, field):
        if field.data:
            field.data = re.sub()"""
