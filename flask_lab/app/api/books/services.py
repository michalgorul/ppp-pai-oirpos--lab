import sqlite3
from datetime import datetime

from flask import Request, redirect, Response, render_template, session

from flask_lab.app.api.books.models import Book
from flask_lab.app.db import DATABASE
from flask_lab.app.utils import dict_to_html


def get_books() -> str:
    con = sqlite3.connect(DATABASE)

    cur = con.cursor()
    cur.execute("select * from books")
    books = cur.fetchall()
    count = f"<h3>Number of books: {len(books)}</h3>"
    l = [
        Book(
            topic=book[0],
            author=book[1],
            genre=book[2],
            text=book[3],
            create_time=int(
                datetime.strptime(book[4], "%Y-%m-%d %H:%M:%S").timestamp()
            ),
            last_edit_time=int(
                datetime.strptime(book[5], "%Y-%m-%d %H:%M:%S").timestamp()
            ),
        ).dict(by_alias=True)
        for book in books
    ]

    table = dict_to_html(l)
    return count + table


def add_book(request: Request) -> str | Response:
    if request.method == "GET":
        if "user" in session:
            return render_template("books/add.html")
        else:
            return redirect("/login")
    else:
        try:
            topic = request.form["topic"]
            author = request.form["author"]
            genre = request.form["genre"]
            text = request.form["text"]
            now = str(datetime.now())[:-7]
            con = sqlite3.connect(DATABASE)
            cur = con.cursor()
            cur.execute(
                "INSERT INTO books ("
                "topic, "
                "author, "
                "genre, "
                "text, "
                "create_time, "
                "last_edit_time) VALUES (?,?,?,?,?,?)",
                (topic, author, genre, text, now, now),
            )
            con.commit()
            con.close()
            return redirect("/")
        except Exception as e:
            return redirect("/")
