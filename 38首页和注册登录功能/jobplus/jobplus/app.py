from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from .models import db, User
from .config import configs

def register_blueprints(haha):
    from .handlers import front, admin
    for i in (front, admin):
        haha.register_blueprint(i)

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    lm = LoginManager()
    lm.init_app(app)

    @lm.user_loader
    def user_loader(id):
        return User.query.get(id)

    lm.login_view = 'front.login'

def create_app(c):
    app = Flask(__name__)
    app.config.from_object(configs.get(c))
    register_extensions(app)
    register_blueprints(app)
    return app
