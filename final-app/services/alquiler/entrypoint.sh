#!/bin/sh

echo "Esperando a Postgres..."

while ! nc -z alquiler-db 5432; do
  sleep 0.1
done

echo "PostgreSQL iniciado"

python manage.py run -h 0.0.0.0