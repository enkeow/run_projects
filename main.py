from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("main_page.html")

@app.route("/article")
def article():
    db.
    return render_template("article.html")

if __name__ == "__main__":
    app.run(debug=True)
