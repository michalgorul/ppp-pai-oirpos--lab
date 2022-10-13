import sqlite3
from typing import List, Optional, Dict, Any

from flask import render_template, redirect, Request, Response, session, request

from flask_lab.app.admin.models import User
from flask_lab.app.db import DATABASE


def user_list() -> List[User]:
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("select * from users_flask")
    users = cur.fetchall()
    return [User(login=user[0], password=user[1], admin=bool(user[2])) for user in users]


def get_users() -> str:
    users = user_list()
    count = f"<h3>Number of users: {len(users)}</h3>"
    head = """
    <table>
        <thead>
          <tr>
             <th>Login</th> <th>Password</th> <th>Admin</th>
          </tr>
       </thead>
       <tbody>
    """
    s = ""
    for i, u in enumerate(users):
        s += f"""
        <tr>
         <th><a href="/users/{u.login}">{u.login}</a></th><td>{u.password}</td><td>{u.admin}</td>
        </tr>
        """
    s += """   
        </tbody>
    </table>"""
    return count + head + s


def add_user(request: Request) -> str | Response:
    if request.method == "GET":
        user = get_curr_user()
        if user.admin is True:
            return render_template("admin/add.html")
        else:
            return redirect("/login")
    else:
        try:
            username = request.form["login"]
            password = request.form["password"]
            admin = request.form.get("admin")
            print(bool(admin))
            new_user = User(login=username, password=password, admin=bool(admin))
            print(new_user)
            con = sqlite3.connect(DATABASE)
            cur = con.cursor()
            cur.execute(
                "INSERT INTO users_flask (" "login, " "password, " "admin) VALUES (?,?,?)",
                (new_user.login, new_user.password, new_user.admin),
            )
            con.commit()
            con.close()
            return redirect("/")
        except Exception as e:
            print(e)
            return redirect("/")


def get_curr_user() -> Optional[User]:
    curr_user = None
    l = user_list()
    for user in l:
        if user.login in session:
            curr_user = user
            break
    return curr_user


def get_user_data() -> Dict[str, Any]:
    curr_user = get_curr_user()
    if curr_user:
        text_login = "Logout"
        link_login = "/logout"
    else:
        text_login = "Login"
        link_login = "/login"

    if curr_user and curr_user.admin is True:
        text_admin = "Users"
        link_admin = "/users"
    else:
        text_admin = ""
        link_admin = ""

    return {
        "text_login": text_login,
        "link_login": link_login,
        "text_admin": text_admin,
        "link_admin": link_admin,
    }


def show_user(login) -> Response | str:
    user = get_curr_user()
    if user.admin is True:
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        query = f"select * from users_flask where login = '{login}'"
        print(query)
        cur.execute(query)
        user = cur.fetchone()
        s = f"""
        <p><b>Username</b>: {user[0]}</p>
        <p><b>Password</b>: {user[1]}</p>
        <p><b>Admin</b>: {bool(user[2])}</p>
        <a href="/"><h3>Home</h3></a>"""
        return s
    else:
        return redirect("/login")
