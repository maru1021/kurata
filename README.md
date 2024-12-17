ローカルでの動作
pythonのインストール
https://www.python.org/downloads/

以下コマンドプロンプトでの操作
python --version
と打ってバージョンが出てくればOK

仮想環境の作成
python -m venv 仮想環境名(英数字で自由に命名可能)

仮想環境に入る
myenv\Scripts\activate

pip(pythonのモジュールなどを管理するやつ)を最新にする
pip install --upgrade pip

django(pythonのサーバーサイドのプログラムを作成するフレームワーク、データベースの制御などができる)のインストール
pip install django

django-admin --version
と打ってバージョンが出てくればOK

フォルダの移動
cd プロジェクトを作成するフォルダ

djangoのプロジェクトを作成
django-admin startproject myproject

python manage.py runserver
と打った後に
http://127.0.0.1:8000/
にアクセスし、ページが表示されればOK

アプリケーションの作成
python manage.py startapp アプリケーション名

モデルの作成(データベースのテーブル)
 python manage.py makemigrations
 python manage.py migrate

マスターユーザーの作成
 python manage.py createsuperuser



codespaceでの動作方法
docker compose up --build

ターミナルを一つ追加後
docker compose exec web python manage.py migrate

見本をダウンロードする方法
gitをインストール
https://git-scm.com/

git clone https://github.com/maru1021/kurata