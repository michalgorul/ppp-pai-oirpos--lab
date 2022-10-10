from flask_lab.app.api.news.services import get_news


def home_news() -> str:
    return f"""
    <h1>NEWS</h1>
    {get_news()}
    <a href="/"><h3>Home</h3></a>"""


def about_news() -> str:
    return "<a href=/news>Powrót</a>"
