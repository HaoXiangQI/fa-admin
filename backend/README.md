# fa

## 启动项目
在项目根目录输入命令
```shell
uvicorn app.main:app --host 0.0.0.0 --port 8888 --reload
```


## 目录结构
```
.
├── README.md
├── admin                           # 功能模块目录
│   ├── __init__.py
│   ├── crud.py                     # 模型层的curd方法
│   ├── models.py                   # 模型层
│   ├── schemas.py                  # 数据模型
│   ├── urls.py                     # 功能模块路由
│   └── views                       # 视图包
│       ├── __init__.py
│       └── v1.py                   # 视图模块
├── app                             # 框架核心目录 
│   ├── __init__.py
│   ├── core                        # 框架核心组件              
│   │   ├── __init__.py 
│   │   ├── config.py               # 配置类
│   │   └── importer.py        
│   ├── database.py                 # 数据库配置
│   └── main.py                     # 项目入口
├── requirements.txt
├── .env                            # 配置文件
└── tests                           # 测试
  └── __init__.py

```
## 项目配置
配置文件为 项目根目录下的.env

```
# 项目名称
PROJECT_NAME=fa
# 跨域配置
BACKEND_CORS_ORIGINS=["*"]
# 数据库
DATABASE_ENGINE=mysql
DATABASE_USER=root
DATABASE_PASSWORD=123456
DATABASE_HOST=172.18.173.166
DATABASE_PORT=3306
DATABASE_DB=banshi
```