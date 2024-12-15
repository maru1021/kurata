from django.http import JsonResponse
from django.shortcuts import render
from .models import ProductionRecord, Team

# urls.pyでアクセスされた時のプログラムを書くところ

# http://127.0.0.1:8000/production
# にアクセスされると以下が動作
# ProductionRecord(日毎の進捗)を全て取得し、
# templates/index.html
# を表示させる
def index(request):
    records = ProductionRecord.objects.all()
    return render(request, 'production/index.html', {'records': records})


def team_index(request):
    if request.method == "GET":
        teams = Team.objects.all()
        return render(request, "production/teams.html", {"teams": teams})

def team_list(request):
    teams = Team.objects.all().values('id', 'name')
    return JsonResponse(list(teams), safe=False)

def team_create(request):
    if request.method == "POST":
        team_name = request.POST.get("name")

        # 重複確認
        if Team.objects.filter(name=team_name).exists():
            return JsonResponse({
                "success": False,
                "message": "その班はすでに登録されています。"
            })

        try:
            Team.objects.create(name=team_name)
            return JsonResponse({
                "success": True,
                "message": "班を登録しました。"
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": f"エラーが発生しました: {str(e)}"
            })
    return JsonResponse({
        "success": False,
        "message": "無効なリクエストです。"
    })

