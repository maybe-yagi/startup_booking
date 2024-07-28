from flask import request

from flask import Blueprint, render_template, redirect, url_for, jsonify
from flask_login import LoginManager, login_required, logout_user, current_user

from app.app import db
from app.user_crud.models import Users
from app.user_crud.forms import UserForm
import re


user_crud = Blueprint(
    "user_crud",
    __name__,
    template_folder="templates",
)


@user_crud.route("/")
def index():
    return render_template("user_crud/home.html")


@user_crud.route("/users")
def users():
    users = Users.query.all()
    users_list = [{
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role_id": user.role_id,
        } for user in users]
    return jsonify(users=users_list)
    # バックエンドテスト用
    # return render_template("user_crud/index.html", users_list=users_list)


# ユーザー登録
# def is_school_email(email):
#     return re.match(r'^[a-zA-Z0-9._%+-]+@numazu\.kosen-ac\.jp$') is not None


@user_crud.route("/user_register", methods=["POST"])
def user_register():
    data = request.json
    if 'password' not in data:
        return jsonify({'error': 'Password is required'}), 400
    #if not is_school_email(data['email']):
    #    return jsonify({'message': 'error'})

    user = Users(
        name=data['name'],
        email=data['email'],
        role_id=data['role_id']
    )
    user.password = data['password']

    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201


@user_crud.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "hello"})
