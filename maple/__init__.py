#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-05-20 12:35:52 (CST)
# Last Update:星期二 2016-6-14 23:20:15 (CST)
#          By:jianglin
# Description:
# **************************************************************************
from flask import Flask, g
from maple.extensions import (register_login, register_redis, register_mail)
from maple.extensions import (register_form, register_babel, register_principal,
                            register_jinja2, register_db, register_maple)
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy


def create_app():

    app = Flask(__name__)
    app.config.from_object('config.config')
    return app


def register(app):
    # register_db(db, app)
    register_form(app)
    register_principal(app)
    register_babel(app)
    register_jinja2(app)
    register_maple(app)
    register_routes(app)


def register_routes(app):
    from maple.forums.views import site
    app.register_blueprint(site, url_prefix='')
    from maple.board.views import site
    app.register_blueprint(site, url_prefix='/<parent_b>')
    from maple.user.views import site
    app.register_blueprint(site, url_prefix='/u/<user_url>')
    from maple.topic.views import site
    app.register_blueprint(site, url_prefix='')
    from maple.mine.views import site
    app.register_blueprint(site, url_prefix='/user')
    from maple.setting.views import site
    app.register_blueprint(site, url_prefix='/setting')
    from maple.tag.views import site
    app.register_blueprint(site, url_prefix='/t')
    import maple.auth.auth
    import maple.admin.admin


app = create_app()
db = SQLAlchemy(app)
mail = register_mail(app)
login_manager = register_login(app)
redis_data = register_redis(app)
register(app)


@app.before_request
def before_request():
    from maple.forums.forms import SortForm
    g.user = current_user
    g.sort_form = SortForm()
