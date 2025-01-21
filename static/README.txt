staticフォルダ内のファイル変更時には以下のコマンドを実行して更新する
docker-compose exec web python manage.py collectstatic --noinput