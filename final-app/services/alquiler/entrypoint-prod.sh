#!/bin/sh

echo "Esperando a Postgres..."

while ! nc -z alquiler-db 5432; do
  sleep 0.1
done

echo "PostgreSQL inicializado"

gunicorn -b 0.0.0.0:5000 manage:app