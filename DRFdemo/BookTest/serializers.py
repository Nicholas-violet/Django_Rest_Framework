

# 针对BookInfo模型类数据，定义一个BookInfoSerializer序列化器
# 来对BooKinfo数据进行序列化操作
'''
from rest_framework import serializers

# # 我们自己心里清楚，这个序列化器是针对BookInfo的！！！
# class BookInfoSerializer(serializers.Serializer):
#     # 通过指定同名类属性的形式，来定义转化结果字典中的属性
#
#     btitle = serializers.CharField()
#     bpub_date = serializers.DateField()
#     bread = serializers.IntegerField()
#     bcomment = serializers.IntegerField()
#     is_delete = serializers.BooleanField()
#     image = serializers.ImageField()


class HeroInfoSerializer2(serializers.Serializer):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)


# 定义一个针对btitle的校验函数
# def check_btitle(value):
#     # 参数value：经过前序校验之后的btitle数据
#     # 我们通过抛出ValidationError异常表示校验失败！！
#     # 返回值无
#
#     # 如果"django"字符串不再value中，表示不符合格式
#     # {"btitle": "围城"}
#     if "django" not in value:
#         # 不是一本关于django的书
#         raise serializers.ValidationError("这不是一本关于djangod的书！")



class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    # read_only设置为True表示该字段只作用于序列化，反序列化的时候直接忽略
    id = serializers.IntegerField(label='ID', read_only=True)

    # write_only设置为True表示该字段只作用于反序列化，序列化的时候直接忽略
    btitle = serializers.CharField(label='名称',
                                   max_length=20,
                                   min_length=2,

                                   # validators约束条件指定多个针对当前字段的校验函数
                                   # validators=[check_btitle]
    )


    bpub_date = serializers.DateField(label='发布日期', required=True)

    bread = serializers.IntegerField(label='阅读量', required=False, min_value=0)
    bcomment = serializers.IntegerField(label='评论量', required=False, min_value=0)
    image = serializers.ImageField(label='图片', required=False, allow_null=True)
    is_delete  =serializers.BooleanField(required=False)

    # heros隐藏字段，多个从表HeroInfo对象
    # heros = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # heros = serializers.StringRelatedField(many=True)
    # heros = HeroInfoSerializer2(many=True)



class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )

    # HeroInfo的固有字段/属性
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    is_delete = serializers.BooleanField()

    # 外间关联属性
    # hbook是当前英雄对象关联的"唯一"的主表"BookInfo对象"

    # (1)如果想把关联字段，序列化成关联对象数据的主键; read_only=True当前字段只作用于序列化操作
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)

    # (2) 把关联字段，序列化成它的__str__方法返回的结果
    # {
    #     "hname": xxx,
    #     "hgener": xxx,
    #     ...
    #     "hbook": "射雕英雄传"
    # }
    hbook = serializers.StringRelatedField() # 无约束条件，默认read_only=True

    # (3) 关联字段自定义序列化
    # {
    #     "hname": xxx,
    #     "hgener": xxx,
    #     ...
    #     "hbook": {"btitle": xxx, "bpub_date": xxx}
    # }
    # hbook = BookInfoSerializer()

'''

"""
使用模型类序列化器
"""


from rest_framework import serializers
from .models import *

# serializers.Serializer ---- 自定义序列化器所继承的
# serializers.ModelSerializer ---- 专门针对模型类数据的序列化器


# 定义一个针对BookInfo的模型类序列化器
class BookInfoModelSerializer(serializers.ModelSerializer):
    # 可以通过在序列化器中手动自定映射的字段

    # 对于非主键的隐藏字段
    # heros = serializers.StringRelatedField(many=True)

    # 手动定义的字段，会覆盖自动映射的字段
    # btitle = serializers.CharField(min_length=2, max_length=20, required=True)

    class Meta:
        model = BookInfo # 声明当前序列化器操作的目标模型类
        fields = "__all__" # 声明操作的模型类的字段为所有：把所有的字段映射到序列化器中
        # fields = ['id', 'btitle', 'bpub_date', 'bread'] # 指定字段映射
        # exclude = ['image'] # 除了image字段，其他的字段映射到序列化器中

        # 对模型类序列化器自动构建的约束条件进行修订
        extra_kwargs = {
            "bread": {"min_value": 0}, # 把bread字段的min_value约束条件设置为0
            # "required": True,
        }

        # 批量地把一些字段设置为read_only=True
        # read_only_fields = ['id', 'bread']


class HeroInfoModelSerializer(serializers.ModelSerializer):
    # 外间关联字段，自动映射的类型是PrimaryKeyRelatedField

    # 关联对象的主键隐藏字段不会自动映射
    hbook_id = serializers.IntegerField()

    class Meta:
        model = HeroInfo
        fields = "__all__"
