# -*- coding:utf-8 -*-
"""
    :author: young
    :DATE: 2019/12/31 19:18
"""
from flask import request, render_template

from app.models import Post
from . import main


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='关于')
