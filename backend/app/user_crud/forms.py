from flask_wtf.form import FlaskForm
from wtforms.fields import IntegerField, StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, length
from app.config import ROLE_SELECT


class UserForm(FlaskForm):
    name = StringField(
        label="名前",
        validators=[DataRequired(message="必須です。"),
                    length(max=30, message="30文字以内で入力してください。")]
    )
    nickname = StringField(
        label="表示名",
        validators=[DataRequired(message="必須です。")]
    )
    email = StringField(

    )
    student_num = StringField(
        label="学籍番号"
    )
    role_id = SelectField(
        label="属性",
        choices=ROLE_SELECT,
    )
    password = PasswordField(
        label="パスワード",
        validators=[DataRequired(message="必須です。")]
    )
    submit = SubmitField("登録")
