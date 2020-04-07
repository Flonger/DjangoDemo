from django.db import models

# Create your models here.
class Student(models.Model):
    # 学生表
    name = models.CharField(max_length=64, verbose_name='姓名')
    sex = models.CharField('性别', max_length=1, choices=(
        ('1','男'),
        ('2','女'),
    ), default='1')
    age = models.PositiveIntegerField('年龄',default=0)
    username = models.CharField('登录名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间',auto_now=True)