import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/Activo")
def activo():
    return render_template("activo.html", page_title="Activo")


@app.route("/Recipes")
def recipe():
    return render_template("recipe.html", page_title="Recipe", list_of_numbers=[1, 2, 3])


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/login")
def login():
    return render_template("login.html", page_title="Login")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0."),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
