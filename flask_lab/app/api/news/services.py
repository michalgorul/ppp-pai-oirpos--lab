import sqlite3
from datetime import datetime

from flask_lab.app.api.news.models import News
from flask_lab.app.db import DATABASE
from flask_lab.app.utils import dict_to_html


def get_news() -> str:
    con = sqlite3.connect(DATABASE)

    cur = con.cursor()
    cur.execute("select * from news")
    news = cur.fetchall()
    count = f"<h3>Number of news: {len(news)}</h3>"
    l = [
        News(
            topic=new[0],
            author=new[1],
            text=new[2],
            create_time=int(datetime.strptime(new[3], "%Y-%m-%d %H:%M:%S").timestamp()),
            last_edit_time=int(datetime.strptime(new[4], "%Y-%m-%d %H:%M:%S").timestamp()),
        ).dict(by_alias=True)
        for new in news
    ]
    table = dict_to_html(l)
    return count + table
