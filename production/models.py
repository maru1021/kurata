from django.db import models
from django.utils.timezone import now

# モデル(データベースのテーブルなどを追加したりするところ)
# python manage.py makemigrationsでマイグレーションファイル(データベースへのテーブルの定義ファイルの作成)
# python manage.py migrateでマイグレーションファイルを使用して実際にデータベースにテーブルを追加

# 日毎の班ごとの進捗のシフトの選択肢
class Shift(models.TextChoices):
    DAY = 'Day', '昼勤'
    NIGHT = 'Night', '夜勤'

# 班
class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# 日毎の班ごとの進捗
class ProductionRecord(models.Model):
    date = models.DateField(default=now)  # 生産日
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  # 班
    shift = models.CharField(max_length=10, choices=Shift.choices)  # 昼勤/夜勤
    units_produced = models.PositiveIntegerField()  # 生産台数

    class Meta:
        unique_together = ('date', 'team', 'shift')  # 各班のシフトで1日1レコード

    def __str__(self):
        return f"{self.date} - {self.team.name} - {self.shift}"
