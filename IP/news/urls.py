from django.urls import path
from .views import *


urlpatterns = [
    path('', news_home, name="news_home"),
]
