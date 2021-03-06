from flask import Flask, render_template
from .extensions import (login_manager, db, mail, serializer,
                         compress)

from .models import *

from .controllers.pages import pages_blueprint
from .controllers.users import users_blueprint

import sys
import logging


BLUEPRINTS = (
    pages_blueprint,
    users_blueprint,
)


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    configure_blueprints(app, BLUEPRINTS)
    configure_extensions(app)
    configure_error_handlers(app)

    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)

    return app


def configure_extensions(app):
    # flask-login
    login_manager.login_view = 'users.login'
    login_manager.login_message = 'Log in required.'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    login_manager.init_app(app)

    # flask-sqlalchemy
    db.init_app(app)

    # flask-mail
    mail.init_app(app)

    # serialize
    serializer.init_app(app)  # in app/serialize.py

    # flask-compress
    compress.init_app(app)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

