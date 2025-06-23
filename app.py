from flask import Flask,redirect,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    sn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'{self.sn} -> {self.title}'

@app.route('/' , methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("posted bro")
        title = request.form['title']
        desc = request.form['desc']
        
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit() 
    all_todo = Todo.query.all()
    return render_template('index.html', all_todo = all_todo)

@app.route('/delete/<int:s>')
def delete(s):
    todo = Todo.query.filter_by(sn=s).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')
    

@app.route('/update/<int:s>')
def update(s):
    todo = Todo.query.filter_by(sn=s).first()
    return render_template('update.html', todo = todo)

@app.route('/update/<int:s>', methods=['POST'])
def final_update(s):
    todo = Todo.query.get_or_404(s)
    todo.title = request.form['title']
    todo.desc = request.form['desc']
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
