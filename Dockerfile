# Стадия для сборки фронтенда

FROM node:22-slim as frontend-builder

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ /app/frontend/
COPY frontend/.env.example ./.env
RUN npm run build

RUN [ -d "/app/frontend/dist" ] || (echo "Директория dist не создана" && exit 1)

# Финальная стадия для бэкенда
FROM python:3.10-slim

WORKDIR /app

# Копируем собранные файлы фронтенда
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

# Устанавливаем Python-зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код бэкенда
COPY . .

CMD ["sh", "entrypoint.sh"]
