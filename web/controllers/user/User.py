#!/usr/bin/env python
# coding: utf-8
# Date  : 2020/7/28
# Author: zhangyi 
# Email : 450245556@qq.com

from flask import Blueprint, render_template

route_user = Blueprint('user_page', __name__)


@route_user.route("/login")
def login():
    return render_template('user/login.html')
