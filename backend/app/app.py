from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db_uri = 'mysql+pymysql://user:password@mysql:3306/database?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)


@app.route('/')
def select_sql():

    users = Users.query.all()
    print(users)
    print("ユーザー一覧")

    return render_template('view.html', users=users)
