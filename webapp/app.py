#import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#import sqlite3

#app = Flask(__name__)
app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    #show all todos
    List_tasks = NewRequests.query.all()
    #print(List_tasks)

    return render_template('base.html', List_tasks=List_tasks )



@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    #new_tsk = NewRequests(title='Added task', complete=False)
    new_tsk = NewRequests(title=title, complete=False)
    db.session.add(new_tsk)
    db.session.commit()
    #print(new_tsk)

    return redirect(url_for("index"))

@app.route("/start/<int:task_id>")
def start(task_id):
    tsk = NewRequests.query.filter_by(id=task_id).first()
    tsk.in_progress = not tsk.in_progress
    
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:task_id>")
def update(task_id):
    tsk = NewRequests.query.filter_by(id=task_id).first()
    tsk.complete = not tsk.complete
    
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    tsk = NewRequests.query.filter_by(id=task_id).first()
    db.session.delete(tsk)
    db.session.commit()
    return redirect(url_for("index"))

class NewRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    complete = db.Column(db.Boolean)
    in_progress = db.Column(db.Boolean)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # new_todo = Todo(title='todo 1', complete=False)
        # db.session.add(new_todo)
        # db.session.commit()

    app.run(debug=True)

#python app.py
    

