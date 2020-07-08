from django.db import models

# Create your models here.
# from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers
# Create your models here.
class BookInfo(models.Model):
    """图书模型类"""
    btitle = models.CharField(max_length=20, verbose_name='标题')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        db_table = 'tb_books'

    def __str__(self):
        return self.btitle



'''
class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)
'''


class HeroInfo(models.Model):
    """英雄模型类"""
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='备注')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    hbook = models.ForeignKey('BookInfo', related_name='heros', on_delete=models.CASCADE, verbose_name='所属图书')

    class Meta:
        db_table = 'tb_heros'

    def __str__(self):
        return self.hname
