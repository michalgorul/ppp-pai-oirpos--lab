from typing import List

from flask_lab.app.api.books.services import get_books


def home_books() -> str:
    return f"""
    <h1>BOOKS</h1>
    {get_books()}
    <a href=/books/about>Przejdz do about</a>"""


def about_books() -> str:
    return f"<p>{list(range(100))}</p"
