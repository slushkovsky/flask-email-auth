from sqlalchemy import Column, String, Integer

from app import db

class Base(db.Model):
	__abstract__ = True

class User(Base):
	__tablename__ = 'users'

	id         = Column(Integer, primary_key=True, unique=True)
	first_name = Column(String(64))
	last_name  = Column(String(64))

	def __init__(self, *args, **kwargs): 
		super().__init__(*args, **kwargs)
