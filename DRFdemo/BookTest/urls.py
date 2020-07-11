from django.urls import path,re_path

from . import views

# urlpatterns是被Django自动识别的路由列表变量：定义该应用的所有路由信息
urlpatterns = [
    # # 函数视图路由语法：
    # # path('网络地址正则表达式', 函数视图名),
    # re_path(r'^books/$', views.BooksAPIView.as_view()),
    # # path('books/(?P<pk>\d+)', views.BooksAPIView.as_view()),
    # re_path(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view()),


    # ================== 模型类视图集开始 ==================

    #
    # # GET + /books/ = self.list 返回列表
    # # POST + /books/ = self.create 新建单一
    # re_path(r'^books/$', views.BooksModelViewSet.as_view(
    #     {
    #         'get':'list',
    #         'post':'create'
    #      }
    # )),
    #
    # # GET + /books/(?P<pk>\d+)/ = self.retrieve
    # # PUT + /books/(?P<pk>\d+)/ = self.update
    # # PATCH + /books/(?P<pk>\d+)/ = self.partial_update
    # # DELETE + /books/(?P<pk>\d+)/ = self.destroy
    #
    # re_path(r'^books/(?P<pk>\d+)/$', views.BooksModelViewSet.as_view(
    #     {
    #         'get':'retrieve',
    #         'put':'update',
    #         'patch':'partial_update',
    #         'delete':'destroy'
    #     }
    # )),

    # ================== 模型类视图集结束 ==================

    # ================== 用户自定义的模型类视图集结束 ==================

    re_path(r'^books/(?P<pk>\d+)/$', views.BooksModelViewSet.as_view({
        'patch':'read'
    })),
    # ================== 用户自定义的模型类视图集结束 ==================
]