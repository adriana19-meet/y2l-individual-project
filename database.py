from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# def function(parameter):
#     pass

# def __init__(self, name, email, password, ):
# 	self.name=name
# 	self.email=email  
# 	self.password=password
#     pass
		
# def __init__(self, problem, name, Description, fileupload ):
# 	self.problem=problem
# 	self.name=name  
# 	self.Description=Description
# 	self.fileupload=fileupload
		
# db.create_all()

def add_user(name, username , password):
	add_user = user(
		name = name,
		username = username,
		password = password)
	session.add(add_user)
	session.commit()

def add_problem(pname, problem, description):
	add_problem = Problem(
		pname = pname,
		problem = problem,
		description = description)
	session.add(add_problem)
	session.commit()


# def add_person(Email,Password):
# 	person = per(
# 		Email = Email,
# 		Password = Password)
# 	session.add(person)
# 	session.commit()	
	
def get_one(id):
	get = session.query(Problem).filter_by(id=id).first()
	return get_one

def get_info():
	info = session.query(Problem).all()
	return info