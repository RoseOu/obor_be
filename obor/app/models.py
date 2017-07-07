# coding: utf-8
"""
sql models

    use: Flask-SQLAlchemy
    -- http://flask-sqlalchemy.pocoo.org/2.1/

"""

from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin, current_user
from wtforms.validators import Email
from datetime import datetime

# permissions
class Permission:
    """
    1. COMMENT: 0x01
    2. MODERATE_COMMENTS: 0x02
    3. ADMINISTER: 0x04
    """
    COMMENT = 0x01
    MODERATE_COMMENTS = 0x02
    ADMINISTER = 0x04


# user roles
class Role(db.Model):
    """
    1. User: COMMENT
    2. Moderator: MODERATE_COMMENTS
    3. Administrator: ADMINISTER
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.COMMENT, True),
            'Moderator': (Permission.COMMENT |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (
                Permission.COMMENT |
                Permission.MODERATE_COMMENTS |
                Permission.ADMINISTER,
                False
            )
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model, UserMixin):
    """user"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(164), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'),default=1)
    password_hash = db.Column(db.String(164))

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def is_admin(self):
        if self.role_id == 2:
            return True
        return False

    def __repr__(self):
        return "<User %r>" % self.username


class AnonymousUser(AnonymousUserMixin):
    """ anonymous user """
    def is_admin(self):
        return False

login_manager.anonymous_user = AnonymousUser

class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer,primary_key=True)
    sort = db.Column(db.Integer,default=1)
    chinese = db.Column(db.String(192),default="")
    chinese_audio = db.Column(db.String(448),default="")
    english = db.Column(db.String(192),default="")
    english_audio = db.Column(db.String(448),default="")
    russian = db.Column(db.String(192),default="")
    russian_audio = db.Column(db.String(448),default="")
    arabic = db.Column(db.String(192),default="")
    arabic_audio = db.Column(db.String(448),default="")
    german = db.Column(db.String(192),default="")
    german_audio = db.Column(db.String(448),default="")
    video_url = db.Column(db.String(448),default="")

    def __repr__(self):
        return "<Word %r>" % self.chinese

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer,primary_key=True)
    kind = db.Column(db.Integer,default=1)
    title = db.Column(db.String(192),default="")
    date = db.Column(db.String(64),default="")
    article_url = db.Column(db.String(448),default="")
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<Article %r>" % self.title

class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer,primary_key=True)
    img_url = db.Column(db.String(192),default="")
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<Show %r>" % self.id

class Carousel(db.Model):
    __tablename__ = 'carousels'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(192),default="")
    img_url = db.Column(db.String(192),default="")
    article_url = db.Column(db.String(448),default="")
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<Carousel %r>" % self.title

class Qrcode(db.Model):
    __tablename__ = 'qrcodes'
    id = db.Column(db.Integer,primary_key=True)
    img_url = db.Column(db.String(192),default="")
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def __repr__(self):
        return "<Qrcode %r>" % self.id
