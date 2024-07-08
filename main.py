from flask import Flask, render_template
from model import Article_run
from webapp.templates import main_page, index, main

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
