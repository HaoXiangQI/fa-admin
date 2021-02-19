# -- coding: utf-8 --
# python3.7.8
# @Time : 2021-02-19 9:32
# @Author : QiHaoXiang
from app.db.migrations.cli import migration_cli
import sys


def commond_line():
    sys.path.insert(0, ".")
    # 数据库迁移命令
    migration_cli()
