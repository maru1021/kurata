# ベースイメージ
FROM python:3.10

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# サーバー起動コマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
