# -*- coding: utf-8 -*-
"""
    aulaszeus.extensions
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    AulasZeus extensions module

    :copyright: (c) 2016 by Haynesss.
    :license: BSD, see LICENSE for more details.
"""
from flask_mongoengine import MongoEngine
from flask_mail import Mail
from flask_assets import Environment
from flask_cache import Cache
from flask_bootstrap import Bootstrap

mail = Mail()
db = MongoEngine()
assets = Environment()
cache = Cache()
bootstrap = Bootstrap()