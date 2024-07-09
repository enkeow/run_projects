from flask import Flask, render_template
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


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Konako325@localhost:5432/postgres'
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/article")
def article():
    # db.session
    return render_template("article.html")


@app.route("/article", methods=["POST"])
def add_article():
    # form = LoginForm()
    #     if form.validate_on_submit():
    # article = Article_run(
    #     title=title,
    #     text=text
    # )
    # db.session.add(article)
    # db.session.commit()
    pass


if __name__ == "__main__":
    app.run(debug=True)
