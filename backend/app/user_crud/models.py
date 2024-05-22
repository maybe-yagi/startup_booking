from app.app import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    mail = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    master = db.Column(db.Boolean)
