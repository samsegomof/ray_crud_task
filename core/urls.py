from django.urls import re_path, include

from . import views

urlpatterns = [
    re_path('login', views.login),
    re_path('sign_up', views.sign_up),
    re_path('test_token', views.test_token),
    re_path('api', include('blog.urls')),
]
