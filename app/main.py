from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.importer import import_path



def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    # 路由配置
    register_router(_app)

    # 跨域配置
    register_router(_app)

    # 日志配置
    register_logging(_app)


    return _app



def register_router(_app: FastAPI) -> None:
    """
    注册路由
    :param _app:
    :return:
    """
    # 项目API
    _app.include_router(import_path('admin.urls'))


def register_cors(_app: FastAPI) -> None:
    """
    跨域配置
    :param _app:
    :return:
    """
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# todo
def register_database(_app:FastAPI) -> None:
    """
    数据库配置 现在的配置入口当前包下的database.py中
    :param _app:
    :return:
    """
    @_app.on_event('startup')
    def init_db():
        pass

# todo
def register_logging(_app: FastAPI) -> None:
    """
    日志配置
    :param _app:
    :return:
    """
    pass

app = get_application()