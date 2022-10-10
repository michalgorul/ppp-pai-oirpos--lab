from flask import Response, Request, request

from flask_lab.app.api.books.services import get_books, add_book


def home_books() -> str:
    return f"""
    <h1>BOOKS</h1>
    {get_books()}
    <a href="/books/add"><h3>Add new book</h3></a>
    <a href="/"><h3>Home</h3></a>"""


def about_books() -> str:
    return f"<p>{list(range(100))}</p"


def create_book() -> Response:
    return add_book(request)
