from sqlalchemy import Column, Integer, String, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from . import _AppSession
from .orm import SQLAlchemyMixin

class UserMixin(object):
    id       = Column(Integer, primary_key=True, unique=True)
    password = Column(String(256))
    email    = Column(String(256), index=True, unique=True)

    def __init__(self, email=None, password=None): 
        self.password = generate_password_hash(password)
        self.email = email

    def check_password(self, password): 
        return check_password_hash(self.password, password)


class UserEmailAuth(_AppSession, SQLAlchemyMixin, UserMixin): 
    __tablename__ = 'users_email_auth'

    @classmethod
    def user_model(cls):
        return cls.user.property.argument

    @classmethod
    def username_max_length(cls):
        user_model = cls.user_model()
        return user_model.__table__.columns.get('username').type.length