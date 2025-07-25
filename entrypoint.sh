#!/bin/bash

# Go to project directory
cd /var/www/Melao

# Run database operations
/venv/bin/python manage.py makemigrations
/venv/bin/python manage.py migrate
/venv/bin/python manage.py collectstatic --noinput

# Set permissions
chown -R :www-data /var/www/Melao
chmod -R 775 /var/www/Melao

if [ -f db.sqlite3 ]; then
    chown :www-data db.sqlite3
    chmod 664 db.sqlite3
fi

# Execute command
exec "$@"