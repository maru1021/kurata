from django.shortcuts import render
from .models import ProductionRecord

# urls.pyでアクセスされた時のプログラムを書くところ

# http://127.0.0.1:8000/production
# にアクセスされると以下が動作
# ProductionRecord(日毎の進捗)を全て取得し、
# templates/index.html
# を表示させる
def index(request):
    records = ProductionRecord.objects.all()
    return render(request, 'production/index.html', {'records': records})
