# -- coding: utf-8 --
# python3.7.8
# @Time : 2021-02-18 13:28
# @Author : QiHaoXiang
from aerich.models import MAX_VERSION_LENGTH
from tortoise import Tortoise, run_async, Model, fields

TORTOISE_ORM = {
    "connections": {"default": "mysql://root:123456@127.0.0.1:3306/qhx"},
    "apps": {
        "models": {
            "models": ["__main__"],
            "default_connection": "default",
        },
    },
}
class Aerich(Model):
    version = fields.CharField(max_length=MAX_VERSION_LENGTH)
    app = fields.CharField(max_length=20)
    content = fields.JSONField()

    class Meta:
        ordering = ["-id"]


async def run():
    await Tortoise.init(config=TORTOISE_ORM)
    aerich = await Aerich.all().first()
    from pprint import pprint
    pprint(aerich.content)

if __name__ == '__main__':
    run_async(run())




