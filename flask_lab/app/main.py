import os

from flask import Flask, render_template
from flask_lab.app.api.books import resources as books_resources
from flask_lab.app.api.news import resources as news_resources
from flask_lab.app.db import db_setup

app = Flask(__name__)

app.add_url_rule("/db", view_func=db_setup)

app.add_url_rule("/books", view_func=books_resources.home_books)
app.add_url_rule("/books/about", view_func=books_resources.about_books)

app.add_url_rule("/news", view_func=news_resources.home_news)
app.add_url_rule("/news/about", view_func=news_resources.about_news)

template_dir = os.path.abspath('../../flask_lab/templates')
app.template_folder = template_dir


@app.route("/")
def index() -> str:
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

