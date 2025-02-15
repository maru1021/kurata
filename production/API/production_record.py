from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from urllib.parse import parse_qs
from ..models import ProductionRecord, Team

# 生産情報管理クラス
@method_decorator(csrf_exempt, name='dispatch')  # PUT/DELETE時に必要
class ProductionRecordDetailView(View):
    # データの取得
    def get(self, request):
        # 生産状況一覧を取得
        production_records = ProductionRecord.objects.all().select_related('team').values(
            'id', 'date','team__id', 'team__name', 'shift', 'units_produced'
        )

        return JsonResponse(list(production_records), safe=False)

    # データの登録
    def post(self, request):
        date = request.POST.get("date")
        team_id = request.POST.get("team_id")
        shift = request.POST.get("shift")
        units_produced = request.POST.get("units_produced")

        if ProductionRecord.objects.filter(date=date, team__id=team_id, shift=shift).exists():
            return JsonResponse({
                "success": False,
                "error_field": "teamSelect",
                "message": "同じ日付、班、シフトのレコードがすでに存在します。"
            })

        team = get_object_or_404(Team, pk=team_id)

        try:
            ProductionRecord.objects.create(
                date=date,
                team=team,
                shift=shift,
                units_produced=int(units_produced)
            )

            return JsonResponse({
                "success": True,
                "message": "生産記録を登録しました。"
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
            date = data.get("date", [""])[0].strip()
            team_id = data.get("team_id", [""])[0].strip()
            shift = data.get("shift", [""])[0].strip()
            units_produced = data.get("units_produced", [""])[0].strip()

            # 重複確認
            if ProductionRecord.objects.filter(date=date, shift=shift, team__id=team_id).exclude(pk=pk).exists():
                return JsonResponse({
                    "success": False,
                    "error_field": "teamSelect",
                    "message": "その班の進捗はすでに登録されています。"
                })

            # 更新処理
            productionrecord = ProductionRecord.objects.get(pk=pk)
            productionrecord.date = date
            productionrecord.team = Team.objects.get(pk=team_id)
            productionrecord.shift = shift
            productionrecord.units_produced = int(units_produced)
            productionrecord.save()

            return JsonResponse({
                "success": True,
                "message": "班が更新されました"
            })
        except ProductionRecord.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "指定された生産情報が存在しません。"
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": f"エラーが発生しました: {str(e)}"
            })

    def delete(self, request, pk):
        try:
            team = ProductionRecord.objects.get(pk=pk)
            team.delete()
            return JsonResponse({
                "success": True,
                "message": "班が削除されました"
            })
        except ProductionRecord.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "指定された班が存在しません。"
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": f"エラーが発生しました: {str(e)}"
            })

