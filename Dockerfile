# # Используем базовый образ с Python
# FROM python:3.11.4

# # Устанавливаем рабочую директорию в контейнере
# WORKDIR /

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONNUNBUFFERED=1

# # Копируем зависимости проекта и устанавливаем их
# COPY requirements.txt /

# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt 
# RUN python -m venv venv
# RUN /bin/bash -c "source venv/bin/activate"

# # Копируем код проекта в контейнер
# COPY . .

# # COPY .env /

# # # Запускаем приложение (разкомментировать если билдим на прямую только докер контейнер)
# # CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Используем базовый образ с Python
FROM python:3.11.4

# Устанавливаем рабочую директорию в контейнере
WORKDIR /

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Копируем зависимости проекта и устанавливаем их
COPY requirements.txt /

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt 

# Копируем код проекта в контейнер
COPY . .

# Запускаем приложение (разкомментировать если билдим на прямую только докер контейнер)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Запускаем приложение с помощью Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "base.wsgi"]


