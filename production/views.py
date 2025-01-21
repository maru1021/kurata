from django.shortcuts import render
from .models import ProductionRecord, Team

# ProductionRecord一覧表示
def index(request):
    records = ProductionRecord.objects.all()
    return render(request, 'production/index.html', {'records': records})

# 班管理ページ
def team_index(request):
    teams = Team.objects.all()
    return render(request, "production/team.html", {"teams": teams})

# 生産数管理ページ
def production_record_index(request):
    production_records = ProductionRecord.objects.all()
    return render(request, "production/production_record.html", {"production_records": production_records})