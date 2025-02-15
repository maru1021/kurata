from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.views import View
from ..models import ProductionRecord, Team

# 生産情報管理クラス
class ProductionRecordGraphView(View):
    # データの取得
    def get(self, request):
        return render(request, "production/production_record_graph.html")

    # データの登録
    def post(self, request):
        end_date = request.POST.get("date")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        start_date = (end_date - timedelta(days=30))
        team_id = request.POST.get("team_id")
        shift = request.POST.get("shift")

        try:
            production_records = ProductionRecord.objects.select_related('team').filter(date__range=[start_date, end_date]).order_by("date")
            grouped_data = (
                production_records
                .values("date", "team__name")
                .annotate(total_units=Sum("units_produced"))
            )

            all_dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
            all_dates_str = [date.strftime("%Y-%m-%d") for date in all_dates]

            # チームごとのデータ初期化
            chart_data = {team: [0] * len(all_dates) for team in set(record["team__name"] for record in grouped_data)}

            # データを埋める
            for record in grouped_data:
                team_name = record["team__name"]
                record_date_str = record["date"].strftime("%Y-%m-%d")
                index = all_dates_str.index(record_date_str)
                chart_data[team_name][index] = record["total_units"]

            # 結果を構造化
            chart_data = {
                "dates": all_dates_str,
                "data": chart_data
            }

            return JsonResponse({
                "success": True,
                "data": chart_data
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": f"エラーが発生しました: {str(e)}"
            })