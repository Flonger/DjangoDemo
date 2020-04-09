# Generated by Django 2.2 on 2020-04-08 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weibo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weibouser',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '删除'), (1, '正常'), (2, '限制用户')], default=1, verbose_name='用户状态'),
        ),
    ]
