from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from app.settings import settings
from app import urls


# todo 文档服务器

def get_application():
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION
    )

    # 路由配置
    register_router(_app)

    # 跨域配置
    register_cors(_app)

    # 数据库配置
    register_database(_app)
    # 日志配置
    # register_logging(_app)

    return _app


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
    # app.middleware()


def register_router(_app: FastAPI) -> None:
    _app.include_router(urls.router)


# todo
def register_database(_app: FastAPI) -> None:
    """
    数据库配置 现在的配置入口当前包下的database.py中
    :param _app:
    :return:
    """
    register_tortoise(_app, config=settings.DATABASE_SETTINGS)
    # logging.info("database init")


# todo
# def register_logging(_app: FastAPI) -> None:
#     """
#     日志配置
#     :param _app:
#     :return:
#     """
#     pass


app = get_application()
