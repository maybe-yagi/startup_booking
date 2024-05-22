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
    return render_template("home.html")


@user_crud.route("/users")
def users():
    users = Users.query.all()
    users_list = [{
        "id": user.id,
        "name": user.name,
        "nickname": user.nickname,
        "email": user.email,
        "role": user.role_id,
        } for user in users]
    return jsonify(users=users_list)


@user_crud.route("/user_register", methods=["POST", "GET"])
def user_register():
    data = request.get_json()
    name = data['name']
    nickname = data['nickname']
    email = data['email']
    student_num = data['student_num']
    role_id = data['role_id']
    password = data['password']

    return render_template("user_register.html", form=form)
