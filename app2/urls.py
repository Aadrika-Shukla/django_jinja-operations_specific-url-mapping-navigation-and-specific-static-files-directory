'''specific url mapping for app2'''
from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('second/',second,name='second'),
]