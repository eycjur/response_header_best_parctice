.PHONY: start-nginx
start-nginx:
	nginx -c $(shell pwd)/frontend/nginx.conf

.PHONY: stop-nginx
stop-nginx:
	nginx -s stop

.PHONY: restart-nginx
restart-nginx: stop-nginx start-nginx

.PHONY: start-frontend
start-frontend:
	cd frontend && npm run dev

.PHONY: start-backend
start-backend:
	cd backend && python main.py
