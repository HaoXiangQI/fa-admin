# 路由管理

from admin.views import v1
from fastapi import APIRouter

path = APIRouter()
path.include_router(v1.api)
