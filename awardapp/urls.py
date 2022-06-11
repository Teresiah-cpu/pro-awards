# from django.conf.urls import re_path
from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index, name='index'),
]