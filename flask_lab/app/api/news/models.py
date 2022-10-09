from pydantic import Field

from flask_lab.app.models import BaseModel


class News(BaseModel):
    topic: str
    author: str
    text: str
    create_time: int = Field(..., alias="createTime")
    last_edit_time: int = Field(..., alias="updateTime")
