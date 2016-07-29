# -*- coding: utf-8 -*-
"""
    aulaszeus.config
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    AulasZeus config module

    :copyright: (c) 2016 by Haynesss.
    :license: BSD, see LICENSE for more details.
"""
import os
import logging

from pymongo.uri_parser import parse_uri


class Config:
    """Config."""

    def __init__(self):
        """Init."""
        self.DEBUG = False
        self.TESTING = False
        self.PRODUCTION = False
        self.SITE_NAME = "AulasZeus"
        self.SITE_LOGO = "/static/img/logo_zeus.svg"
        self.SECRET_KEY = '49f37f000379c8167cac8aad4a425132095e08ea62a0aed713b4744c90aa2275'
        self.LOG_LEVEL = logging.DEBUG
        self.WTF_CSRF_ENABLED = True

        # Mongodb support
        self.MONGODB_SETTINGS = self.mongo_from_uri(
            'mongodb://localhost:27017/aulaszeus'
        )

        self.SYS_ADMINS = ['errors@lab804.com.br']  # E-mails to send errors
        self.BOOTSTRAP_SERVE_LOCAL = True
        self.GOOGLE_ANALYTICS_ID = None  # Analytics U-XXXX-YY
        self.CACHE_TYPE = "simple"
        self.PER_PAGE = 10  # Pagination per page

        # Configured Email
        self.DEFAULT_MAIL_SENDER = 'AulasZeus < no-reply@lab804.com.br >'
        self.MAIL_SERVER = 'mail.lab804.com.br'
        self.MAIL_PORT = 587
        self.MAIL_USE_SSL = False
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = 'no-reply@lab804.com.br'
        self.MAIL_PASSWORD = ''

        # Flask-Security setup
        self.SECURITY_EMAIL_SENDER = 'AulasZeus < no-reply@lab804.com.br >'
        self.SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
        self.SECURITY_PASSWORD_SALT = '4b5ea79011674b34b3440482272396c6'

        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
        self.SECURITY_CONFIRMABLE = False
        self.SECURITY_REGISTERABLE = True
        self.SECURITY_RECOVERABLE = True
        self.SECURITY_TRACKABLE = True
        self.SECURITY_CHANGEABLE = True
        self.SECURITY_SEND_REGISTER_EMAIL = False

        # flask security routes
        self.SECURITY_URL_PREFIX = '/auth'
        self.SECURITY_POST_LOGIN_VIEW = '/'
        self.SECURITY_POST_LOGOUT_VIEW = '/auth/login'
        self.SECURITY_POST_REGISTER_VIEW = '/'
        self.SECURITY_POST_CONFIRM_VIEW = '/auth/login'

        # Security Email Subjects
        self.SECURITY_EMAIL_SUBJECT_REGISTER = 'AulasZeus - Bem Vindo'
        self.SECURITY_EMAIL_SUBJECT_CONFIRM = 'AulasZeus - Por favor confirme seu email'
        self.SECURITY_EMAIL_SUBJECT_PASSWORDLESS = u'AulasZeus - Instruções para acesso'
        self.SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE = 'AulasZeus - Sua senha foi redefinida'
        self.SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE = 'AulasZeus - Sua senha foi alterada'
        self.SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = u'AulasZeus - Instruções de redefinição de senha'

        # Security Mensagens
        self.SECURITY_MSG_INVALID_PASSWORD = (u'Senha inválida.', 'error')
        self.SECURITY_MSG_UNAUTHORIZED = (
            u'Você não tem permissão para acessar esta área.', 'error')
        self.SECURITY_MSG_CONFIRM_REGISTRATION = (
            u'Obrigado. Instruções de confirmação foram enviado para %(email)s.',
            'success')
        self.SECURITY_MSG_EMAIL_CONFIRMED = (
            u'Obrigado. Seu email foi confirmado.', 'success')
        self.SECURITY_MSG_ALREADY_CONFIRMED = (
            u'Seu email já foi confirmado.', 'info')
        self.SECURITY_MSG_INVALID_CONFIRMATION_TOKEN = (
            u'Token de confirmação inválido.', 'error')
        self.SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED = (
            u'%(email)s já está associado a uma conta.', 'error')
        self.SECURITY_MSG_PASSWORD_MISMATCH = (
            u'Senha não corresponde.', 'error')
        self.SECURITY_MSG_RETYPE_PASSWORD_MISMATCH = (
            u'Senha não corresponde.', 'error')
        self.SECURITY_MSG_INVALID_REDIRECT = (
            u'Redirecionamento Redirections outside the domain are forbidden',
            'error')
        self.SECURITY_MSG_PASSWORD_RESET_REQUEST = (
            u'Instruções para resetar sua senha foram enviadas para %(email)s.',
            'info')
        self.SECURITY_MSG_PASSWORD_RESET_EXPIRED = (
            u'Você não resetou sua senha dentro %(within)s. Novas instuções foram enviadas para %(email)s.',
            'error')
        self.SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN = (
            u'Token inválido para resetar a senha.', 'error')
        self.SECURITY_MSG_CONFIRMATION_REQUIRED = (
            u'Email requer confirmação.', 'error')
        self.SECURITY_MSG_CONFIRMATION_REQUEST = (
            u'Confirmation instructions have been sent to %(email)s.', 'info')
        self.SECURITY_MSG_CONFIRMATION_EXPIRED = (
            u'Você não confirmou o e-mail dentro %(within)s. Novas instuções foram enviadas para %(email)s.',
            'error')
        self.SECURITY_MSG_LOGIN_EXPIRED = (
            u'Você não pode acessar %(within)s. Novas instruções foram enviadas para %(email)s.',
            'error')
        self.SECURITY_MSG_LOGIN_EMAIL_SENT = (
            u'Instruções para efetuar o login foram enviadas para %(email)s.',
            'success')
        self.SECURITY_MSG_INVALID_LOGIN_TOKEN = (
            u'Token de login inválido.', 'error')
        self.SECURITY_MSG_DISABLED_ACCOUNT = (u'Conta desabilitada.', 'error')
        self.SECURITY_MSG_EMAIL_NOT_PROVIDED = (u'Email não fornecido', 'error')
        self.SECURITY_MSG_INVALID_EMAIL_ADDRESS = (
            u'Endereço de email inválido.', 'error')
        self.SECURITY_MSG_PASSWORD_NOT_PROVIDED = (
            u'Senha não fornecida.', 'error')
        self.SECURITY_MSG_PASSWORD_NOT_SET = (
            u'Nenhuma senha fornecida para esse usuário.', 'error')
        self.SECURITY_MSG_PASSWORD_INVALID_LENGTH = (
            u'A senha deve possuir no minímo 6 caracteres.', 'error')
        self.SECURITY_MSG_USER_DOES_NOT_EXIST = (
            u'Email especificado não existe.', 'error')
        self.SECURITY_MSG_INVALID_PASSWORD = (u'Senha inválida.', 'error')
        self.SECURITY_MSG_PASSWORDLESS_LOGIN_SUCCESSFUL = (
            u'Você logou com sucesso.', 'success')
        self.SECURITY_MSG_PASSWORD_RESET = (
            u'Você resetou sua senha com sucesso e já logou automaticamente.',
            'success')
        self.SECURITY_MSG_PASSWORD_IS_THE_SAME = (
            u'Sua senha deve ser diferente da senha antiga.', 'error')
        self.SECURITY_MSG_PASSWORD_CHANGE = (
            u'Você alterou a senha com sucesso.', 'success')
        self.SECURITY_MSG_LOGIN = (
            u'Por favor logue-se para ter acesso a essa página.', 'info')
        self.SECURITY_MSG_REFRESH = (
            u'Por favor reautentique para acessar essa página.', 'info')

    @staticmethod
    def mongo_from_uri(uri):
        config = parse_uri(uri)
        conn_settings = {
            'db': config['database'],
            'username': config['username'],
            'password': config['password'],
            'host': config['nodelist'][0][0],
            'port': config['nodelist'][0][1]
        }
        return conn_settings


class Dev(Config):
    """Development Config."""

    def __init__(self):
        super(Dev, self).__init__()
        self.DEBUG = True
        self.TESTING = False
        self.ENVIROMENT = "Development"


class Prod(Config):
    """Production Config."""

    def __init__(self):
        super(Prod, self).__init__()
        self.DEBUG = False
        self.TESTING = False
        self.ENVIROMENT = "Production"
        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = False
        self.SECURITY_CONFIRMABLE = True
        self.LOG_LEVEL = logging.INFO
        self.CACHE_TYPE = "simple"  # MEMCACHE
        self.BOOTSTRAP_SERVE_LOCAL = False

enviroment = os.getenv('ENVIROMENT', 'DEV').lower()

if enviroment == 'prod':
    app_config = Prod()
else:
    app_config = Dev()