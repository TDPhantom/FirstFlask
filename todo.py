from flask import Flask , render_template, request, redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)


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
def add():
     new_todo = request.form['new_todo']
     todo_list.append(new_todo)
     cursor = connection.cursor()
     cursor.execute("INSERT INTO `Todos`(`description`) VALUES('"+ new_todo +"')")
     return redirect(request.referrer)
     return new_todo

