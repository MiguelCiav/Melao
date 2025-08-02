#!/bin/bash

# Go to project directory
cd /var/www/Melao

# Run database operations
/venv/bin/python manage.py makemigrations
/venv/bin/python manage.py migrate
/venv/bin/python manage.py collectstatic --noinput

chown -R :www-data /var/www/Melao/
chmod -R 777 /var/www/Melao/

# Execute command
exec "$@"