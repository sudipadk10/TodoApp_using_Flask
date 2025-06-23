from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    sn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.sn} -> {self.title}'

@app.route('/')
def index():
    # Create and insert a dummy todo
    todo = Todo(title="web development", desc="learn flask for now then dive into django")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        # 💡 This forces SQLAlchemy to register the model
        Todo.__table__
        db.create_all()
        print("✅ Database created at:", os.path.abspath("todo.db"))
        to = Todo(title="test", desc="test desc")
        db.session.add(to)
        db.session.commit()
        print("✅ Dummy to added!")

    app.run(debug=True)
