from flask import Flask, render_template
from model import Article_run
from webapp.templates import main_page, index, main

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("main_page.html")

@app.route("/article")
def article():
    # db.session
    return render_template("article.html")

if __name__ == "__main__":
    app.run(debug=True)
