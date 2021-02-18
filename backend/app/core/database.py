# -- coding: utf-8 --
# python3.7.8
# @Time : 2021-02-18 10:56
# @Author : QiHaoXiang
from typing import List

from pydantic import BaseModel, AnyUrl


# 数据库配置模型
class DataBaseDsn(AnyUrl):
    allowed_schemes = {'postgres', 'postgresql', 'mysql'}
    user_required = True


class DataModels(BaseModel):
    models: List[str]
    default_connection: str = "default"


class DataApps(BaseModel):
    models: DataModels


class DataBaseSettings(BaseModel):
    connections: dict
    apps: DataApps

# if __name__ == '__main__':
#     print(DataBaseSettings(**TORTOISE_ORM))
# Connection(**{"connections": {"default": "mysql://root:123456@127.0.0.1:3306/test"}})
# for k, v in {"default": "mysql://root:123456@127.0.0.1:3306/test"}.items():
#     print(v)
