#!/bin/sh
set -e

echo "Waiting for PostgreSQL..."
until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
  echo "PostgreSQL is unavailable - sleeping"
done

echo "Running makemigrations..."
python manage.py makemigrations accounts profiles blogs events messages_app catches goals gear regulations fish spots core

echo "Running migrate..."
python manage.py migrate

echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000
