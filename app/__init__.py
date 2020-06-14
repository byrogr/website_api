from flask import Flask
from flask_restful import Api

from app.db import db
from app.api.resources import api_v1
from app.ext import ma, migrate


def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    Api(app, catch_all_404s=True)

    app.url_map.strict_slashes = False
    app.register_blueprint(api_v1)

    return app
