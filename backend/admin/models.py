# -- coding: utf-8 --
# python3.7.8
# @Time : 2021-02-18 17:40
# @Author : QiHaoXiang
from tortoise import Model, fields


class ProdEdition(Model):
    """
    版本表
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    product_sub_edition: fields.ReverseRelation["ProdSubEdition"]

    class Meta:
        table = "prod_edition"


class ProdSubEdition(Model):
    """
    子版本表
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)

    edition: fields.ForeignKeyRelation[ProdEdition] = fields.ForeignKeyField(
        "models.ProdEdition", related_name="product_sub_edition", db_constraint=False
    )
    feature: fields.ManyToManyRelation["ProdFeature"] = fields.ManyToManyField(
        "models.ProdFeature", related_name="feature", through="prod_feature_subedition", db_constraint=False
    )

    class Meta:
        table = "prod_sub_edition"


class ProdPermission(Model):
    """
    权限表
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    path = fields.CharField(max_length=255)

    class Meta:
        table = "prod_permission"


class ProdFeature(Model):
    """
    功能表
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)

    permission: fields.ManyToManyRelation[ProdPermission] = fields.ManyToManyField(
        "models.ProdPermission", related_name="permission", through="prod_feature_permission", db_constraint=False
    )

    class Meta:
        table = "prod_feature"