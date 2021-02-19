from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings, validator
from pydantic.networks import AnyUrl

from app.db.database import DataBaseSettings
import app.settings as sett
# 数据库配置模型
class DataBaseDsn(AnyUrl):
    allowed_schemes = {'postgres', 'postgresql', 'mysql'}
    user_required = True


# 配置类
class Settings(BaseSettings):
    """
    docs
    """
    PROJECT_NAME: str
    VERSION: str
    BACKEND_CORS_ORIGINS: List[str] = []
    APPS: Optional[List[str]]
    MIDDLEWARE: Optional[List[str]]
    # USE_MIGRATIONS: bool = True

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # 数据库
    DATABASE_ENGINE: str
    DATABASE_HOST: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_DB: str
    DATABASE_URI: Optional[DataBaseDsn] = None
    DATABASE_SETTINGS: Optional[DataBaseDsn] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        """
        生成数据库访问url
        :param v:
        :param values:
        :return:
        """
        if isinstance(v, str):
            return v
        return DataBaseDsn.build(
            scheme=values.get("DATABASE_ENGINE"),
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            path=f"/{values.get('DATABASE_DB') or ''}",
        )

    # @validator("APPS")
    # def check_app_importable(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
    #     pass

    @validator('DATABASE_SETTINGS')
    def assemble_db_config(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        """
        生成数据库访问url
        :param v:
        :param values:
        :return:
        """
        if isinstance(v, str):
            return v

        models: list = values.get('APPS')
        # 是否使用迁移工具
        # if values.get('USE_MIGRATIONS'):
        #     models.append('aerich')

        for i in range(len(models)):
            models[i] += '.models'

        return DataBaseSettings(**{
            "connections": {"default": str(values.get('DATABASE_URI'))},
            "apps": {
                "models": {
                    "models": models,
                    "default_connection": "default",
                },
            },
        }).dict()
        # return {'hello': 'world'}

    class Config:
        """
        配置信息
        """
        # 大小写敏感
        case_sensitive = True
        # 配置文件
        env_file = ".env"


# settings = Settings()
