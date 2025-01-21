from django.urls import path
from . import views
from .API.team import TeamDetailView
from .API.production_record import ProductionRecordDetailView

app_name = 'production'

# http://127.0.0.1:8000/production
# 上記のurl以下のルーティングの設定
urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team_index, name='team_index'),
    path('team/list/', TeamDetailView.as_view(), name='team_list'),
    path('team/create/', TeamDetailView.as_view(), name='team_create'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('production_record/', views.production_record_index, name='production_record_index'),
    path('production_record/list/', ProductionRecordDetailView.as_view(), name='production_record_list'),
    path('production_record/create/', ProductionRecordDetailView.as_view(), name='production_record_create'),
    path('production_record/<int:pk>/', ProductionRecordDetailView.as_view(), name='production_record_detail'),
]

