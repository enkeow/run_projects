from flask import Flask, render_template, flash, request
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

from model import Article_run
app.secret_key = 'dovlatov-chemodan'

@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/article", methods=["POST", "GET"])
def add_article():
    form = LoginForm()
    if request.method == "GET":
        return render_template("article.html", form=form)
    elif request.method == 'POST':
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
            return render_template('main_page.html', form=form)
    return render_template('main_page.html', form=form)


@app.route('/articles')
def articles_page():
    articles = Article_run.query.order_by(Article_run.id.desc()).limit(3).all()
    return render_template('article_page.html', articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
