# -- coding: utf-8 --
# python3.7.8
# @Time : 2021-02-18 17:40
# @Author : QiHaoXiang
from tortoise import Model, fields


class Event(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    datetime = fields.DatetimeField(null=True)

    class Meta:
        table = "event"

    def __str__(self):
        return self.name
