from flask import Flask, render_template, flash
from model import (
    db,
    User,
    Race,
    Club_run,
    Article_run,
    Race_user,
    Club_run_user
)
from flask_migrate import Migrate

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

from forms import LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Konako325@localhost:5432/postgres'
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/article")
def article():
    db.session
    return render_template("article.html")


@app.route("/article", methods=["POST"])
def add_article():
    form = LoginForm()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        article= Article_run(
            title=title,
            text=text
        )
        db.session.add(article)
        db.session.commit()
        flash('Статья успешно добавлена на сайт')
        return render_template('articles.html', form=form)
    #return render_template('add_article.html', form=form)

 

if __name__ == "__main__":
    app.run(debug=True)
