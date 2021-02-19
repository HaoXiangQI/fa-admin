# 参数序列化
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from admin.models import (
    ProdEdition,
    ProdSubEdition
)


class ProdEditionSchema(BaseModel):
    name: str


class ProdSubEditionSchema(BaseModel):
    name: str
    edition_id: int


ProdEditionDan = pydantic_model_creator(ProdEdition)
ProdSubEditionDan = pydantic_model_creator(ProdSubEdition)
