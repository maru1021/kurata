from django.contrib import admin
from django.urls import path
from django.urls import include
from production import views


# アクセスされたurlによって使用するurls.pyを切り替える
# adminはデータベースを管理するためのページにアクセスできる
urlpatterns = [
    path('', include('production.urls')),
    path('admin/', admin.site.urls),
    path('production/', include('production.urls')),
]
