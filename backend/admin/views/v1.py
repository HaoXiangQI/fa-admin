from typing import List

from fastapi import APIRouter
from admin.models import ProdEdition, ProdSubEdition
from admin.schemas import ProdEditionSchema, ProdEditionDan, ProdSubEditionDan, ProdSubEditionSchema

api = APIRouter()


@api.post('/user/login')
async def hello():
    res = 'hello, world'
    return {'data': res}


@api.get('/edition')
async def get_prod_edition():
    """
    获取版本
    """
    res = await ProdEdition.all().prefetch_related("product_sub_edition")
    # print(res)
    return {'data': res}


@api.post('/edition')
async def add_prod_edition(edition: ProdEditionSchema):
    """
    添加版本
    """
    res = await ProdEditionDan.from_tortoise_orm(await ProdEdition.create(name=edition.name))
    return {'data': res}


@api.get('/edition/sub')
async def get_sub_edition():
    """
    获取子版本
    """
    res = await ProdSubEditionDan.from_tortoise_orm(await ProdSubEdition.create(**sub_edition.dict()))

    return {'data': res}


@api.post('/edition/sub')
async def add_prod_sub_edition(sub_edition: ProdSubEditionSchema):
    """
    添加子版本
    """
    res = await ProdSubEditionDan.from_tortoise_orm(await ProdSubEdition.create(**sub_edition.dict()))
    return {'data': res}


@api.get('/edition/permission')
async def get_prod_edition():
    """
    获取权限
    """
    res = None
    return {'data': res}


@api.post('/edition/permission')
async def add_prod_sub_edition():
    """
    添加权限
    """
    res = None
    return {'data': res}
