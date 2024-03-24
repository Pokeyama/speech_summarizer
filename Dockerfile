#FROM python:3.12-slim-bullseye
#
## 作業ディレクトリの設定
#WORKDIR /app
#
## ホストのrequirements.txtをコンテナにコピー
#COPY requirements.txt .
#
## 必要なパッケージのインストール
#RUN pip install --no-cache-dir -r requirements.txt
#
## コードのコピー
#COPY . .
#
## ボリュームの設定
#VOLUME /out
#
## エントリーポイントの設定
#CMD ["python", "main.py"]
#
