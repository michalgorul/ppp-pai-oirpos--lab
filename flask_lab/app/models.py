from pydantic import BaseModel as Model


class BaseModel(Model):
    class Config:
        allow_population_by_field_name = True
