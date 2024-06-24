from datetime import datetime

from app.app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False)
    student_num = db.Column(db.String(255))
    role_id = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.now)
    password_hash = db.Column(db.String(255), nullable=False)

    # パスワードセットのプロパティ
    @property
    def password(self):
        raise AttributeError("読み取り不可")

    # パスワードのセット
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # パスワードのチェック
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # ニックネームの重複チェック
    def is_duplicate_nickname(self):
        return Users.query.filter_by(nickname=self.nickname).first() is not None


# ログインユーザーの特定
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
