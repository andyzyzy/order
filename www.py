# -*- coding: utf-8 -*-
from application import app
from web.controllers.index import route_index
from web.controllers.user.User import route_user
from web.controllers.static import route_static
app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_user, url_prefix="/user")
app.register_blueprint(route_static, url_prefix="/static")