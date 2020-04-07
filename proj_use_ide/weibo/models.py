from django.db import models

# Create your models here.
class WeiboUser(models.Model):
    username = models.CharField('用户名', max_length=64)
    password = models.CharField('密码', max_length=256)
    nickname = models.CharField('昵称', max_length=64)

    class Meta:
        db_table = 'weibo_user'


class Weibo(models.Model):
    content = models.CharField('微博内容', max_length=500)
    user = models.ForeignKey(WeiboUser, verbose_name='用户', on_delete=models.CASCADE)
    created_time = models.DateTimeField('发布时间',auto_now_add=True)
    source = models.CharField('发布来源', null=True, blank=True, max_length=100)
    class Meta:
        db_table = 'weibo'

class WeiboImg(models.Model):
    weibo = models.ForeignKey(Weibo,  on_delete=models.CASCADE)
    image = models.ImageField(upload_to='weibo', verbose_name='图片')
    class Meta:
        db_table = 'weibo_img'

class Comment(models.Model):
    content = models.CharField('评论内容', max_length=100)
    created_time = models.DateTimeField('评论时间',auto_now_add=True)
    user = models.ForeignKey(WeiboUser, verbose_name='评论用户', on_delete=models.CASCADE)
    weibo = models.ForeignKey(Weibo,verbose_name='关联微博', on_delete=models.CASCADE)
    class Meta:
        db_table = 'weibo_comment'

class Friend(models.Model):
    user_from = models.ForeignKey(WeiboUser, verbose_name='关注人', related_name='user_from', on_delete=models.CASCADE)
    user_to = models.ForeignKey(WeiboUser, verbose_name='被关注人', related_name='user_to', on_delete=models.CASCADE)
    created_time = models.DateTimeField('关注时间',auto_now_add=True)
    class Meta:
        db_table = 'weibo_friend'

# user = WeiboUser()
# user.user_from.xx
# user.user_to.xx