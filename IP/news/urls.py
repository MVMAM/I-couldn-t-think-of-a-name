from django.urls import path
from .views import *


urlpatterns = [
    path('', news_home, name="news_home"),
    path('create_news/', create_news, name="create_news"),
]
