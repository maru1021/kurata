from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from urllib.parse import parse_qs
from ..models import Team

# 班管理クラス
@method_decorator(csrf_exempt, name='dispatch')  # PUT/DELETE時に必要
class TeamDetailView(View):
    # データの取得
    def get(self, request, pk=None):
        # pkがない場合、班一覧を取得
        if pk is None:
            teams = Team.objects.all().values()
            return JsonResponse(list(teams), safe=False)

        # pkがある場合、特定の班情報を取得
        team = get_object_or_404(Team, pk=pk)
        return JsonResponse({
            "id": team.id,
            "name": team.name
        })

    # データの登録
    def post(self, request):
        team_name = request.POST.get("name", "").strip()

        # 重複確認
        if Team.objects.filter(name=team_name).exists():
            return JsonResponse({
                "success": False,
                "error_field": "teamName",
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

    # データの編集
    def put(self, request, pk):
        try:
            data = parse_qs(request.body.decode('utf-8'))
            team_name = data.get("name", [""])[0].strip()

            # 重複確認
            if Team.objects.filter(name=team_name).exclude(pk=pk).exists():
                return JsonResponse({
                    "success": False,
                    "error_field": "teamName",
                    "message": "その班はすでに登録されています。"
                })

            # 更新処理
            team = Team.objects.get(pk=pk)
            team.name = team_name
            team.save()

            return JsonResponse({
                "success": True,
                "message": "班が更新されました"
            })
        except Team.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "指定された班が存在しません。"
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": f"エラーが発生しました: {str(e)}"
            })

    def delete(self, request, pk):
        try:
            team = Team.objects.get(pk=pk)
            team.delete()
            return JsonResponse({
                "success": True,
                "message": "班が削除されました"
            })
        except Team.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "指定された班が存在しません。"
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": f"エラーが発生しました: {str(e)}"
            })

