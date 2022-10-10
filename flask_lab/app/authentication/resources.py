from flask import session, request, render_template

from config import settings


def login() -> str:
    if request.method == "GET":
        return render_template("authentication/login.html")
    else:
        try:
            if (
                request.form["login"] == settings.login
                and request.form["password"] == settings.pswd
            ):
                session["user"] = "username"
                return "Session was created <br> <a href='/'> Home </a>"
            else:
                return "Session was not created <br> <a href='/'> Home </a>"
        except Exception:
            return "Session was not created <br> <a href='/'> Home </a>"


def logout() -> str:
    if "user" in session:
        session.pop("user")
    else:
        redirect("index.html")

    return "Logged out <br>  <a href='/'> Home </a>"
