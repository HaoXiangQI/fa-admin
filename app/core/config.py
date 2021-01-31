
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator
from pydantic.networks import AnyUrl


# 数据库配置模型
class DataBaseDsn(AnyUrl):
    allowed_schemes = {'postgres', 'postgresql', 'mysql'}
    user_required = True


# 配置类
class Settings(BaseSettings):
    PROJECT_NAME: str
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    BACKEND_CORS_ORIGINS: List[str] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)   

    DATABASE_ENGINE: str
    DATABASE_HOST: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_DB: str
    DATABASE_URI: Optional[DataBaseDsn] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return DataBaseDsn.build(
            scheme=values.get("DATABASE_ENGINE"),
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            path=f"/{values.get('DATABASE_DB') or ''}",
        )

    class Config:
        case_sensitive = True
        env_file = ".env"





settings = Settings()

# if __name__ =="__main__":
#     from pprint import pprint
#     pprint(settings)