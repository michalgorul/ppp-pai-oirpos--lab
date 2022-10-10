import sqlite3
from typing import List

from flask_lab.app.api.books.models import Book
from flask_lab.app.db import DATABASE


def get_books() -> List[Book]:
    con = sqlite3.connect(DATABASE)

    cur = con.cursor()
    cur.execute("select * from books")
    books = cur.fetchall()
    book_list = List[Book]
    for book in books:
        book_list.append(Book(author=book[0], text=book[1], topic=book[2], genre=book[3]))
    print(book_list)
    return book_list
