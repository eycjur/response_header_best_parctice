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
cd frontend
npm run dev &
cd ..

cd backend
python app.py &
cd ..

nginx -c $(pwd)/frontend/nginx.conf

# stop
nginx -s stop
```
