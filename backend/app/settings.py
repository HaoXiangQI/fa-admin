# -- coding: utf-8 --
# python3.7.8
# @Time : 2021-02-18 9:47
# @Author : QiHaoXiang
from app.core.config import Settings

# setting_dict = {
#
# }
"""
apps 解析app中的urls和models
"""
apps = [
    'admin'
]

# middleware = [
#     'test'
# ]

settings = Settings(
    APPS=apps
)

# if __name__ == '__main__':
#     from pprint import pprint
#     pprint(apps)
    # pprint(Settings(APPS=apps))
