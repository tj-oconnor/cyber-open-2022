FROM python:3-alpine

# Install packages
RUN apk add --update --no-cache supervisor npm jq gcc musl-dev libffi-dev g++

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install Flask Flask-SQLAlchemy Flask-Migrate pywebpush apscheduler
RUN pip install gunicorn

# Copy flag
COPY flag.txt /flag.txt

# add user
RUN adduser -D -u 1000 -g 1000 -s /bin/sh www

# Setup app
RUN mkdir -p /app

# Switch working environment
WORKDIR /app

# Add application
COPY challenge .
RUN chown -R www: /app

# Generate VAPID keys for web push
RUN npm install -g web-push
RUN web-push generate-vapid-keys --json > /vapid.json

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# Expose port the server is reachable on
EXPOSE 1337

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]