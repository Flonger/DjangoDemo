from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from oauth.models import Student
from pets.models import Pet


class Product(models.Model):
    #商品表
    name = models.CharField('商品名称',max_length=64)

    collections = GenericRelation('Collection')



class Store(models.Model):
    # 店铺表
    name = models.CharField('店铺名称',max_length=64)


class Collection(models.Model):
    # 收藏表
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    obj_id = models.IntegerField('关联的ID')
    content_obj = GenericForeignKey('content_type', 'obj_id')

    created_at = models.DateTimeField('收藏时间', auto_now_add=True)
