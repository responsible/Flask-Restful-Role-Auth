__author__ = 'responsible'
from App import db
from flask.ext.security import UserMixin, RoleMixin
from passlib.handlers.django import django_pbkdf2_sha256

roles_users = db.Table('roles_users',  # 用户权限中间表
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):  # 权限表
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description


class User(db.Model, UserMixin):  # 用户表
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(11), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, username=None, password=None, active=True):
        self.username = username
        self.password = django_pbkdf2_sha256.encrypt(password)
        self.active = True

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter(User.username == username).one()
        if user and django_pbkdf2_sha256.verify(password, user.password):  # 自行选择密码算法
            return user
