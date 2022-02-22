from django.urls import path, include
from . import views

urlpatterns = [
    # 默认身份验证的url
    path('', include('django.contrib.auth.urls')),
    path("login/",views.User_login),
    # 注册页面
    path('register/', views.register_make, name='register')
    ,path('error/',views.error)
]
