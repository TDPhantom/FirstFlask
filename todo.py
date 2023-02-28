from flask import Flask , render_template, request

app = Flask(__name__)

todo_list=["Have atleast made my first video game", "Get 1K Money","Have a peaceful life"]

@app.route("/")
def index():
     return render_template("todo.html.jinja", todo_list= todo_list)


@app.route("/add")
def add():
     new_todo = request.form['new_todo']
     return new_todo