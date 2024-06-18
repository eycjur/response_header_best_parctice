# API Sample

このリポジトリはレスポンスヘッダーの設定を確認するためのサンプルです。

## Setup

```bash
cd frontend
npm install
cd ..

cd backend
pip install -r requirements.txt
cd ..

# install nginx
# ex. brew install nginx(mac)
```

## Run Server

```bash
make frontend-start
make backend-start
make nginx-start
```

nginxを停止する場合は以下のコマンドを実行してください。

```bash
make nginx-stop
```
