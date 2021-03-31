import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/activo/,json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", activo=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/activo.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/Activo")
def activo():
    return render_template("activo.html", page_title="Activo")


@app.route("/Recipes")
def recipe():
    return render_template("recipe.html", page_title="Recipe",)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@ app.route("/member")
def member():
    return render_template("member.html", page_title="member")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0."),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
