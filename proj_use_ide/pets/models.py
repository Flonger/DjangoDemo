from django.db import models

# Create your models here.

class CommnUtils(models.Model):
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)
    class Meta:
        abstract = True

class Host(CommnUtils):
    name = models.CharField('主人名字',max_length=64)
    class Meta:
        db_table = 'hosts'

class Pet(CommnUtils):
    name = models.CharField('宠物名',max_length=64)
    sex = models.CharField('性别', max_length=1, choices=(
        ('1','公'),
        ('2','母'),
    ), default='1')
    age = models.PositiveIntegerField('年龄',default=0)
    host_id = models.CharField('主人id',max_length=64)
    hosts = models.ManyToManyField(Host)
    class Meta:
        db_table = 'pets'
        ordering = ['-updated_at']