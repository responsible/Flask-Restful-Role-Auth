__author__ = 'responsible'
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import SQLAlchemyUserDatastore, Security
from App import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

from App.models import User, Role, roles_users
from App.routes import api

# Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security().init_app(app, user_datastore, register_blueprint=False)

# init database data
try:
    db.create_all()
    db.session.add(User("test1", "test1"))
    db.session.add(User("test2", "test2"))
    db.session.add(Role("admin", "管理员"))
    db.session.commit()
    db.engine.execute(roles_users.insert(), user_id=1, role_id=1)
    db.session.commit()
except:
    pass