from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    title = StringField(
        'Заголовок статьи',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    text = TextAreaField(
        'Текст статьи',
        validators=[DataRequired()],
        render_kw={"class": "form-control text", "rows": 5}
    )
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})