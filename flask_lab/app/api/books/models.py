from pydantic import Field

from flask_lab.app.models import BaseModel


class Book(BaseModel):
    topic: str
    author: str
    genre: str
    text: str
    create_time: int = Field(..., alias="createTime")
    last_edit_time: int = Field(..., alias="updateTime")
