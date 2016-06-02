from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

from email_auth.models.user import UserMixin

Base = declarative_base()

class User(Base, UserMixin):
	__tablename__ = 'users'

	first_name = Column(String(64))
	last_name  = Column(String(64))
