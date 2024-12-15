from django.urls import path
from . import views

# http://127.0.0.1:8000/production
# 上記のurl以下のルーティングの設定
urlpatterns = [
    path('', views.index, name='index'),
]
