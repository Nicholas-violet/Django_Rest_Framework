

from rest_framework import serializers

class BookInfoSerializers(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(max_length=20, verbose_name='标题')
    bpub_date = serializers.DateField(verbose_name='发布日期')
    bread = serializers.IntegerField(default=0, verbose_name='阅读量')
    bcomment = serializers.IntegerField(default=0, verbose_name='评论量')
    is_delete = serializers.BooleanField(default=False, verbose_name='删除标记')

