from flask import Flask , render_template, request, redirect
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import pymysql.cursors

app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    "Ansu": generate_password_hash("Knitter"),
      }

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

connection = pymysql.connect(
    host="10.100.33.60",
    user="abattlessmith",
    password="223185349",
    database="abattlessmith_todo",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True,
    )

todo_list=["Have atleast made my first video game", "Get 1K Money","Have a peaceful life"]

@app.route("/")
def index():
 cursor = connection.cursor()


 cursor.execute("SELECT * FROM `Todos` ORDER BY `Done` ASC;")

 result = cursor.fetchall()

 print(result)
 return render_template("todo.html.jinja", todo_list= result)
 

@app.route("/add", methods =['POST'])
@auth.login_required
def add():
     new_todo = request.form['new_todo']
     todo_list.append(new_todo)
     cursor = connection.cursor()
     cursor.execute("INSERT INTO `Todos`(`description`) VALUES('"+ new_todo +"')")
     return redirect(request.referrer)
     return new_todo

@app.route("/Done", methods=['POST'])
@auth.login_required
def Done():
    todo_list = request.form['todo_list']
    cursor = connection.cursor()
    
    cursor.execute(f"UPDATE `Todos` SET `Done` = 1 WHERE `ID` = {todo_list}")
    
    return redirect("/")
