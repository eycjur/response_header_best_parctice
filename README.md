# Response Header Best Parctice

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

http://localhost:80 からアプリにアクセスできます  

なお、nginxを停止する場合は以下のコマンドを実行してください。

```bash
make nginx-stop
```

## Best Practice

フロントエンドの設定は、 [frontend/nginx.conf](frontend/nginx.conf) を参照してください。
バックエンドの設定は、 [backend/main.py](backend/main.py) を参照してください。
