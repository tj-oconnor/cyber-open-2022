FROM python:3.7-alpine

# Install packages
RUN apk add --update --no-cache supervisor python3-dev tor torsocks

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install Flask
RUN pip install gunicorn

# Add user
RUN adduser -D -u 1000 -g 1000 -s /bin/sh www

# Copy flag
COPY flag.txt /app/flag.txt

# Setup app
RUN mkdir -p /app && mkdir -p /app/service_dir

# Switch working environment
WORKDIR /app

# Add application
COPY challenge .
RUN chown -R www:www . && chmod 700 /app/service_dir

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# Expose port the server is reachable on
EXPOSE 1337

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]