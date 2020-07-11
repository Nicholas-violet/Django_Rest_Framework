from django.shortcuts import render

# Create your views here.

# ============== APIView开始 ==================
"""
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.status import *

class BooksAPIView(APIView):

    # pass
    # 01
    # 返回书本列表数据
    # GET + /books/
    def get(self, request):
        books = BookInfo.objects.all()
        serializer = BookInfoModelSerializer(instance=books, many=True)
        return Response(data=serializer.data,status=HTTP_200_OK)


    # 02
    # 新建一本书
    # POST + /books/
    def post(self, request):
        # pass
        bookinfo = request.data
        serializer = BookInfoModelSerializer(data=bookinfo)
        if not serializer.is_valid():
            return Response(data={'errmsg':'参数有误!'}, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)



class BookAPIView(APIView):
    # pass
    # 01
    # 返回单一数据
    # GET + /books/(?P<pk>\d+)/
    def get(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        serializer = BookInfoModelSerializer(instance=book)
        return Response(data=serializer.data, status=HTTP_200_OK)

    # 02
    # 删除单一数据
    # DELETE + /books/(?P<pk>\d+)/
    def delete(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        book.delete()
        return Response(data=None, status=HTTP_204_NO_CONTENT)


    # 03
    # 全更新,必选传递全部必传字段
    # PUT + /books/(?P<pk>\d+)/
    def put(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        bookinfo = request.data
        serializer = BookInfoModelSerializer(instance=book, data=bookinfo)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)

    # 04
    # 部分更新
    # PATCH + /books/(?P<pk>\d+)/
    def patch(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        newbook = request.data
        serializer = BookInfoModelSerializer(instance=book, data=newbook, partial=True)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)

"""
# ============== APIView结束 ==================


# ============== GenericAPIView开始 ==================
"""
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import *
from .models import *
from .serializers import *
class BooksAPIView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    # 方法:get
    # 获取全部的信息
    def get(self, request):
        # 这一个用到是get_queryset,是一个查询集.二下面获取单一对象的时候,是get_object
        book = self.get_queryset()
        serializer = self.get_serializer(instance=book, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    # 方法post
    # 新建一个单一对象
    def post(self, request):
        # 方法一
        # # 获取前段传值
        # book = request.data
        # # 构建序列化对象
        # book = self.get_serializer(data=book)

        # 方法二
        # 获取前端传值,然后就是构建序列化器对象
        book = self.get_serializer(data=request.data)
        if not book.is_valid():
            return Response(data=book.errors, status=HTTP_400_BAD_REQUEST)

        book.save()
        return Response(data=book.data, status=HTTP_201_CREATED)



class BookAPIView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
    # 方法:get
    # 获取某一个单一元素
    def get(self, request, pk):
        # 1、获取单一对象
        # get_object(): 在一个"查询集"中，默认根据"pk"过滤出唯一对象
        # (1)、该函数从类属性querysey中过滤
        # (2)、默认依据字段pk过滤
        # (3)、默认自居字段的值，是根据命名分组"pk"提取的参数
        book = self.get_object()
        serializer = self.get_serializer(instance=book)
        return Response(data=serializer.data, status=HTTP_200_OK)


    # 方法delete
    # 删除某一个元素
    def delete(self, request, pk):
        book = self.get_object()
        book.delete()
        return Response(data=None, status=HTTP_204_NO_CONTENT)

    # 方法:put
    # 全修改
    def put(self, request, pk, **kwargs):
        partial = kwargs.get('partial', False)
        book = self.get_object()
        serializer = self.get_serializer(instance=book, data=request.data, partial=partial)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)

    # 方法:putch
    # 不完全修改
    # 方法一,直接使用patch
    '''
    def patch(self, request, pk):
        book = self.get_object()
        serializer = self.get_serializer(instance=book, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)
    '''
    # 方法二,用到判定
    def patch(self, request, pk):
        return self.put(request, pk, partial=True)
"""
# ============== GenericAPIView结束 ==================


# ============== 五个Mixin开始 ==================
"""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from .models import *
from .serializers import *

class BooksAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    # 获取全部对象
    def get(self, request):
        return self.list(request)

    # 新建一个对象
    def post(self, request):
        return self.create(request)

class BookAPIView(GenericAPIView, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    # 获取某一个单一对象
    def get(self, request, pk):
        return self.retrieve(request, pk)

    # 删除一个对象
    def delete(self, request, pk):
        return self.delete(request, pk)

    # 全更新某一个对象
    def put(self, request, pk):
        return self.update(request, pk)

    # 不全更新摸一个对象
    def patch(self, request, pk):
        return self.partial_update(request, pk)

"""
# ============== 五个Mixin结束 ==================


# ============== 五个子类结束 ==================
"""
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView, RetrieveAPIView
class BooksAPIView(ListAPIView, CreateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

class BookAPIView(UpdateAPIView, DestroyAPIView, RetrieveAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
"""
# ============== 五个子类结束 ==================



# ============== 模型类视图集开始 ==================
"""
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
# 主要看urls的改变

class BooksModelViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer
"""
# ============== 模型类视图集结束 ==================




# ============== 自定义--模型类视图集开始 ==================

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import *
from .models import *
from .serializers import *

class BooksModelViewSet(ModelViewSet):

    def read(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        serializer = BookInfoModelSerializer(
            instance=book,
            data=request.data,
            partial=True
        )
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)

# ============== 自定义--模型类视图集结束 ==================















