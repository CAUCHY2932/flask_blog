# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/12/31 14:39
"""

from flask import Blueprint


errors = Blueprint('errors', __name__)


from . import handler
