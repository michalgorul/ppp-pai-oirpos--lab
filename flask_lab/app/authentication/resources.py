from flask import session, request, render_template, redirect

from flask_lab.app.admin.models import User
from flask_lab.app.admin.services import get_curr_user, user_list


def login() -> str:
    if request.method == "GET":
        return render_template("authentication/login.html")
    else:
        try:
            users = user_list()
            username = request.form["login"]
            password = request.form["password"]
            user_logged = None

            for u in users:
                if u.login == username and u.password == password:
                    session[u.login] = u.login
                    user_logged = u
                    break

            if user_logged:
                return "Session was created <br> <a href='/'> Home </a>"
            else:
                raise Exception
        except Exception:
            return "Session was not created <br> <a href='/'> Home </a>"


def logout() -> str:
    curr_user = get_curr_user()

    if curr_user and curr_user.login in session:
        try:
            session.pop(curr_user.login)
        except KeyError:
            pass
    else:
        redirect("index.html")
    return "Logged out <br>  <a href='/'> Home </a>"
