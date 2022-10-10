from flask_lab.app.api.news.services import get_news


def home_news() -> str:
    return f"""
    <h1>NEWS</h1>
    {get_news()}
    <a href=/news/about>Przejdz do about</a>"""


def about_news() -> str:
    return "<a href=/news>Powrót</a>"
