from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, DateField, FloatField, PasswordField
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

class RaceForm(FlaskForm):
    name = StringField(
        'Название забега',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
        
    )
    distance = FloatField(
        'Дистанция (в км.)',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
        
    )
    date = DateField(
        'Дата забега',
        format='%Y-%m-%d',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    location = StringField(
        'Где будет проходить забег',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    info = TextAreaField(
        'Информация о забеге',
        validators=[DataRequired()],
        render_kw={"class": "form-control", "rows": 5}
    )
    submit = SubmitField(
        'Добавить забег', render_kw={"class": "btn btn-primary"}
    )

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Отправить')
