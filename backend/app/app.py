from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, logout_user, current_user
from flask_cors import CORS
from app.config import config


db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()


def create_app(config_key):
    app = Flask(__name__)

    app.config.from_object(config[config_key])

    db.init_app(app)
    # csrf.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
    CORS(app)

    from app.user_crud import views as user_crud_views

    app.register_blueprint(user_crud_views.user_crud, url_prefix="/")

    return app
