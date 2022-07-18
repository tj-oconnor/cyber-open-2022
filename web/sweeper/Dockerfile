FROM python:3-alpine

# Install packages
RUN apk add --update --no-cache supervisor g++

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install Flask Flask-Session flask-sock
RUN pip install gunicorn

# Copy flag
COPY flag.txt /flag.txt
RUN chmod 444 /flag.txt

# add user
RUN adduser -D -u 1000 -g 1000 -s /bin/sh www

# Setup app
RUN mkdir -p /app

# Switch working environment
WORKDIR /app

# Add application
COPY challenge .
RUN chmod -R 755 /app

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# Expose port the server is reachable on
EXPOSE 1337

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]