from django.urls import path
from . import views

app_name = 'production'

# http://127.0.0.1:8000/production
# 上記のurl以下のルーティングの設定
urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.team_index, name='team_index'),
    path('teams/list/', views.TeamDetailView.as_view(), name='team_list'),
    path('teams/create/', views.TeamDetailView.as_view(), name='team_create'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),
]

