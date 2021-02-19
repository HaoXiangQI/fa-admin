# -- coding: utf-8 --
# python3.7.8
# @Time : 2021-02-18 17:15
# @Author : QiHaoXiang
from fastapi import APIRouter
from app.core.importer import import_path

router = APIRouter()
router.include_router(import_path('admin'))


if __name__ == '__main__':
    print(import_path('admin'))