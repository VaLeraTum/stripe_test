FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY stripes/requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY stripes/ .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0:8000"]
