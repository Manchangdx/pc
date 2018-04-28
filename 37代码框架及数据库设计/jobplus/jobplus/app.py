from flask import Flask
from flask_migrate import Migrate
from .models import db, User
from .config import configs

def register_blueprints(haha):
    from .handlers import front, admin
    for i in (front, admin):
        haha.register_blueprint(i)



def create_app(c):
    app = Flask(__name__)
    app.config.from_object(configs.get(c))
    register_blueprints(app)
    db.init_app(app)
    Migrate(app, db)
    return app
