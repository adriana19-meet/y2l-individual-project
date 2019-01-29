from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
# class Product(Base):
#     pass
# class Users(db.Model):
# 	__tablename__="users"
    
#     id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(80), unique=True, nullable=False)
# 	email = db.Column(db.String(120), unique=True, nullable=False)
# 	password = db.Column(db.String(20), unique=True, nullable=False)



# class Posts(db.Model):
# 	__tablename__="posts"
# 	id = db.Column(db.Integer, primary_key=True)
# 	problem= db.Column(db.String(500), unique=True, nullable=False)
#  name = db.Column(db.String(30), unique=True, nullable=False)
# 	Description = db.Column(db.String(1000), unique=True, nullable=False)
# 		fileupload=db.Column(db.file(),unique=False,nullable=True)

class user(Base):
    __tablename__ = "users"
    name = Column(String)
    username = Column(String, primary_key=True)
    password = Column(String)
    

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True, autoincrement=True)
    pname = Column(String)
    problem = Column(String)
    description = Column(String)