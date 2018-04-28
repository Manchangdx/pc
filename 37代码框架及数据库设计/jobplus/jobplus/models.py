from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base:
    __abstract__ = True
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class User(Base):
    ROLE_USER = 11
    ROLE_STAFF = 22
    ROLE_ADMIN = 33
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    email = db.Column(db.String(128), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    real_name = db.Column(db.String(64))
    phone = db.Column(db.Integer)
    work_years = db.Column(db.SmallInteger)
    role = db.Column(db.SmallInteger, default=ROLE_USER)


