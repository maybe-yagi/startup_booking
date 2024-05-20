from flask import request

from flask import Blueprint, render_template, redirect, url_for

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
    return render_template("index.html", users=users)


@user_crud.route("/user_register", methods=["POST", "GET"])
def user_register():
    form = UserForm()
    if form.validate_on_submit():
        user = Users(
            name=form.name.data,
            age=form.age.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_crud.users"))

    return render_template("user_register.html", form=form)
