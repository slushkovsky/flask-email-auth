from sqlalchemy import Column, Integer, String, ForeignKey

from email_auth.models import _AppSession
from email_auth.models.orm import SQLAlchemyMixin

class UserMixin(object):
    id       = Column(Integer, primary_key=True, unique=True)
    password = Column(String(256))
    email    = Column(String(256), index=True, unique=True)

class UserEmailAuth(_AppSession, SQLAlchemyMixin, UserMixin): 
    __tablename__ = 'users_email_auth'

    @classmethod
    def user_model(cls):
        return cls.user.property.argument

    @classmethod
    def username_max_length(cls):
        user_model = cls.user_model()
        return user_model.__table__.columns.get('username').type.length