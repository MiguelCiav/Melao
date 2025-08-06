FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PROJECT_NAME=Melao \
    APP_NAME=melaoapp

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    apache2 \
    libapache2-mod-wsgi-py3 \
    virtualenv \
    && rm -rf /var/lib/apt/lists/*

# Create project directory
RUN mkdir /var/www/${PROJECT_NAME}
WORKDIR /var/www/${PROJECT_NAME}

# Create virtual environment
RUN virtualenv /venv

# Install Django
RUN /venv/bin/pip install django

# Install apps
RUN /venv/bin/pip install django-widget-tweaks

# Copy Apache configuration
COPY djangoproject.conf /etc/apache2/sites-available/djangoproject.conf

# Enable site and disable default
RUN a2ensite djangoproject.conf && \
    a2dissite 000-default.conf

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80
ENTRYPOINT ["/entrypoint.sh"]
CMD ["apache2ctl", "-D", "FOREGROUND"]