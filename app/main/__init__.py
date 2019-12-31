# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/12/31 14:38
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import routes
