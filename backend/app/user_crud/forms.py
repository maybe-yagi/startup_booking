from flask_wtf.form import FlaskForm
from wtforms.fields import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    name = StringField(
        label="名前",
        validators=[DataRequired(message="必須です。")]
    )
    age = IntegerField(
        label="年齢",
        validators=[DataRequired(message="必須です。")]
    )
    submit = SubmitField("登録")
