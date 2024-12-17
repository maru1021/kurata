from django.shortcuts import render
from .models import ProductionRecord, Team

# ProductionRecord一覧表示
def index(request):
    records = ProductionRecord.objects.all()
    return render(request, 'production/index.html', {'records': records})

# Team一覧ページ
def team_index(request):
    teams = Team.objects.all()
    return render(request, "production/teams.html", {"teams": teams})