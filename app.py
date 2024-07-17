from flask import Flask, render_template, flash, request, redirect, url_for
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

from forms import LoginForm, RaceForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Konako325@localhost:5432/postgres'
db.init_app(app)
migrate = Migrate(app, db)

from model import Article_run, Race
app.secret_key = 'dovlatov-chemodan'


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/add_article", methods=["GET", "POST"])
def add_article():
    form = LoginForm()
    if request.method == "GET":
        return render_template("article.html", form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            text = form.text.data
            article = Article_run(
                title=title,
                text=text
            )
            db.session.add(article)
            db.session.commit()
            #flash('Статья успешно добавлена на сайт')
            return redirect(url_for('main_page'))


@app.route('/articles/')
def articles_page():
    articles = Article_run.query.order_by(Article_run.id.desc()).limit(6).all()
    return render_template('article_page.html', articles=articles)


@app.route('/articles/<int:article_id>')
def article_id(article_id):
    article = Article_run.query.get_or_404(article_id)
    return render_template('article_id.html', article=article)


@app.route('/club_run')
def club_run():
    club = Club_run.query.all()
    return render_template('Club_run.html', club=club)


@app.route('/add_race', methods=['POST', 'GET'])
def add_race():
    form = RaceForm()
    if request.method == 'GET':
        return render_template('add_race.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            race = Race(name=form.name.data,
                        distance=form.distance.data,
                        date=form.date.data,
                        location=form.location.data,
                        info=form.info.data)
            db.session.add(race)
            db.session.commit()
            flash('Забег успешно добавлен!')
            return redirect(url_for('main_page'))
        else:
            return render_template('add_race.html', form=form)




@app.route('/races/')
def races_page():
    races = Race.query.order_by(Race.id.desc()).all()
    return render_template('races_page.html', races=races)


if __name__ == "__main__":
    app.run(debug=True)
