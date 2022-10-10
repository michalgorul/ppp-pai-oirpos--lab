import os

from flask import Flask, render_template, session
from flask_session import Session

from flask_lab.app.api.books import resources as books_resources
from flask_lab.app.authentication import resources as auth_resources
from flask_lab.app.db import db_setup

app = Flask(__name__)
sess = Session()

app.add_url_rule("/db", view_func=db_setup)

app.add_url_rule("/books", view_func=books_resources.home_books)
app.add_url_rule("/books/add", view_func=books_resources.create_book, methods=["GET", "POST"])
app.add_url_rule("/books/about", view_func=books_resources.about_books)

app.add_url_rule("/login", view_func=auth_resources.login, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=auth_resources.logout, methods=["GET", "POST"])


template_dir = os.path.abspath("../../flask_lab/templates")
app.template_folder = template_dir


@app.route("/")
def index() -> str:
    if "user" in session:
        text = "Logout"
        link = "/logout"
    else:
        text = "Login"
        link = "/login"
    return render_template("index.html", text=text, link=link)


if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.config["SESSION_TYPE"] = "filesystem"
    sess.init_app(app)
    app.config.from_object(__name__)
    app.run(debug=True, use_reloader=True)
