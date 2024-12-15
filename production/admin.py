from django.contrib import admin
from .models import Team, ProductionRecord

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ProductionRecord)
class ProductionRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'team', 'shift', 'units_produced')
    list_filter = ('date', 'team', 'shift')
