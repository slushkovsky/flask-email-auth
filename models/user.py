from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from . import _AppSession
from .orm import SQLAlchemyMixin


class UserEmailAuth(_AppSession, SQLAlchemyMixin, UserMixin): 
    __tablename__ = 'users_email_auth'

    id        = Column(Integer, primary_key=True, unique=True)
    password  = Column(String(256))
    email     = Column(String(256), index=True, unique=True)
    confirmed = Column(Boolean, default=False)

    def __init__(self, user_id=None, email=None, password=None): 
        self.password = generate_password_hash(password)
        self.email = email
        self.user_id = user_id

    def check_password(self, password): 
        return check_password_hash(self.password, password)

    @classmethod
    def user_model(cls):
        return cls.user.property.argument

    @classmethod
    def username_max_length(cls):
        user_model = cls.user_model()
        return user_model.__table__.columns.get('username').type.length