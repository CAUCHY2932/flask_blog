# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/12/31 10:03
"""
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()

# app = Flask(__name__)
# app.config['SECRET_KEY'] = '06470cbc026cb70715a1a1c6cd115d80d4e67e38dbc35aaa09e02c6cd0b472b2'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#
# db.init_app(app)
# login_manager.init_app(app)
# bcrypt.init_app(app)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '06470cbc026cb70715a1a1c6cd115d80d4e67e38dbc35aaa09e02c6cd0b472b2'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    return app


app = create_app()

from . import routes
