from flask import Response, request

from flask_lab.app.admin.services import add_user, get_users, show_user


def home_users() -> str:
    return f"""
    <h1>USERS</h1>
    {get_users()}
    <a href="/users/add"><h3>Add new user</h3></a>
    <a href="/"><h3>Home</h3></a>"""


def create_user() -> Response:
    return add_user(request)


def view_user() -> Response:
    return show_user(username=username)
