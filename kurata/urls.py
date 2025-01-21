from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings

# アクセスされたurlによって使用するurls.pyを切り替える
# adminはデータベースを管理するためのページにアクセスできる
urlpatterns = [
    path('', include('production.urls')),
    path('admin/', admin.site.urls),
    path('production/', include('production.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]