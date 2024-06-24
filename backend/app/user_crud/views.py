from flask import request

from flask import Blueprint, render_template, redirect, url_for, jsonify
from flask_login import LoginManager, login_required, logout_user, current_user

from app.app import db
from app.user_crud.models import Users
from app.user_crud.forms import UserForm


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
        "nickname": user.nickname,
        "email": user.email,
        "role_id": user.role_id,
        } for user in users]
    # return jsonify(users=users_list)
    # バックエンドテスト用
    return render_template("user_crud/index.html", users_list=users_list)


@user_crud.route("/user_register", methods=["POST"])
def user_register():
    data = request.json
    if 'password' not in data:
        return jsonify({'error': 'Password is required'}), 400

    user = Users(
        name=data['name'],
        nickname=data['nickname'],
        email=data['email'],
        student_num=data['student_num'],
        role_id=data['role_id']
    )
    user.password = data['password']

    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201
