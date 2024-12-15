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
