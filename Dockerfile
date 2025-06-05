# Базовый образ с Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект внутрь контейнера
COPY . .

# Открываем порт
EXPOSE 5000

# Команда запуска приложения
CMD ["python3", "app.py"]
