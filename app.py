from flask import Flask , render_template,request,redirect,url_for,session
#from flask.ext.sqlachemy 
import database
from database import get_one, get_info
import sqlalchemy
import os 
# from flask.ext.heroku
# import heroku 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
# db=sqlalchemy(app)


    


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')





@app.route("/signin1" , methods=["GET" , "POST"])
def signin1():
    print("signin1")
    print(request.method)
    if request.method =="GET":
        return render_template("signin1.html")
    else:    
        print(1)
        Email=request.form['Email']
        print(2)
        print(request.form)
        Password=request.form['Password']
        print(3)
        # database.add_person( Email, Password)
        print("made it this far")

        return render_template('add.html')
        
    

    return render_template('signin1.html')


@app.route("/signup", methods=["GET","POST"] )
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method =="POST":
        name = request.form['name']
        username = request.form['Username']
        password = request.form['Password']
        database.add_user(name, username , password) 

        return render_template('signin1.html')

@app.route("/add", methods=["GET" , "POST"])
def add():
    # print("add")
    # print(request.method)
    if request.method =="GET":
        return render_template("add.html")
    elif request.method == "POST":
        pname = request.form["pname"]
        problem = request.form["problem"]
        description = request.form["description"]
        database.add_problem(pname , problem , description)
        info = database.get_info()
        # print(pname, problem, description)       
        return redirect(url_for('problems', info = info))
        

@app.route("/problems", methods=["GET","POST"])
def problems():
    info=database.get_info()
    return render_template("problems.html",info =info)
    
        

# @app.route("/createuser" ,methods=['POST'] )
# def createuser():
#     data=request.data
#     name=request.form['name']
#     email=request.form['email']
#     password=request.form['password']



        
    



    

    

#     user= Users(name, email,password)

#    (db.Model):


# 	db.session.add(user)
# 	db.session.commit()
    # return render_template('home.html')

# @app.route("/posts", methods=['POST'])
# def posts():
#     # data=request.data
#     problem=request.form['problem']
#     pname=request.form['name']
#     description=request.form['description']
#     # fileupload=request.form['fileupload']
#     post = add_problem(problem,pname,description)
#     database.session.add(post)
#     database.session.commit()
#     # return render_template('home.html' )
#     return redirect(url_for(problems))
# 








if __name__=="__main__":
    app.run(debug=True)





















