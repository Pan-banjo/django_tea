from django.urls import path, include
from . import views


app_name = "courses"

# 路由
urlpatterns = [
    path(r"index2", views.index1, name="index1"),  # 这里不调用视图函数views.index()，可以反解析url
    path(r"index/<int:v1>/<int:v2>", views.index2, name="index2"),
    path('tests/', views.tests),
    # path(r"index", views.index, name="index0")
    path("index3", views.index3, name="index3"),
    path('index', views.index,name="index")
]
