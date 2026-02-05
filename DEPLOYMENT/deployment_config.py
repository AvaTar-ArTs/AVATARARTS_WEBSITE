# AvatarArts Website Deployment Configuration
# Deployment files for avatararts.org

# 1. Gunicorn Configuration (gunicorn.conf.py)
"""
Gunicorn configuration for AvatarArts website
"""

# Server socket
bind = "0.0.0.0:8000"
backlog = 2048

# Worker processes
workers = 4
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 100
timeout = 30
keepalive = 2
preload_app = True

# Restart workers after this many requests, to help prevent memory leaks
max_requests = 1000

# Daemon
daemon = False
pidfile = "/tmp/avatararts.pid"
user = None
group = None
tmp_upload_dir = None

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "avatararts"

# SSL
keyfile = None
certfile = None


# 2. Nginx Configuration (nginx.conf)
"""
Nginx configuration for AvatarArts website
This assumes the Flask app is running on port 8000
"""

nginx_config = """
upstream avatararts_app {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name avatararts.org www.avatararts.org;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name avatararts.org www.avatararts.org;
    
    # SSL Configuration
    ssl_certificate /path/to/ssl/certificate.crt;
    ssl_certificate_key /path/to/ssl/private.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384;
    ssl_prefer_server_ciphers off;
    
    # Security Headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
    
    # Logging
    access_log /var/log/nginx/avatararts_access.log;
    error_log /var/log/nginx/avatararts_error.log;
    
    # Serve static files directly through nginx
    location /static {
        alias /path/to/avatararts/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    # Pass requests to Gunicorn
    location / {
        proxy_pass http://avatararts_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeout settings
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
}
"""


# 3. Docker Configuration (Dockerfile)
dockerfile_content = '''
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \\
    && apt-get install -y --no-install-recommends \\
        postgresql-client \\
        gcc \\
        g++ \\
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Create uploads directory
RUN mkdir -p /app/STATIC/uploads

# Expose port
EXPOSE 8000

# Run gunicorn
CMD ["gunicorn", "--config", "gunicorn.conf.py", "CORE.APP.app:app"]
'''


# 4. Docker Compose Configuration (docker-compose.yml)
docker_compose_content = '''
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://avatararts:password@db:5432/avatararts
    depends_on:
      - db
    volumes:
      - ./STATIC/uploads:/app/STATIC/uploads
    restart: unless-stopped

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=avatararts
      - POSTGRES_USER=avatararts
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    restart: unless-stopped

volumes:
  postgres_data:
'''


# 5. Environment Variables (.env.example)
env_example_content = '''
# AvatarArts Website Environment Variables

# Flask Configuration
FLASK_APP=CORE.APP.app:app
FLASK_ENV=production
FLASK_DEBUG=False

# Secret Key (change this in production!)
AVATARARTS_SECRET_KEY=your-super-secret-key-change-this-in-production

# Database Configuration
DATABASE_URL=postgresql://avatararts:password@localhost/avatararts

# Suno Integration
SUNO_API_KEY=your-suno-api-key

# GitHub Integration
GITHUB_TOKEN=your-github-token

# Email Configuration (if using email)
MAIL_USERNAME=your-email@example.com
MAIL_PASSWORD=your-email-password

# Redis Configuration
REDIS_URL=redis://localhost:6379/0

# nocTurneMeLoDieS Path
NOCTURNEMELODIES_PATH=/Users/steven/Music/nocTurneMeLoDieS
AVATARARTS_V4_PATH=/Users/steven/Music/nocTurneMeLoDieS/github.com/ichoake/AvaTar-Arts/V4_SUNO_INTEGRATION
'''


# 6. Deployment Script (deploy.sh)
deployment_script_content = '''
#!/bin/bash

# AvatarArts Deployment Script

set -e  # Exit on any error

echo "Starting AvatarArts deployment..."

# Pull latest changes
git pull origin main

# Install/update dependencies
pip install -r requirements.txt

# Run database migrations (if using database)
# flask db upgrade

# Collect static files (if using static file management)
# flask collect-static

# Restart application server
sudo systemctl restart avatararts

# Reload Nginx configuration
sudo nginx -t && sudo systemctl reload nginx

echo "Deployment completed successfully!"
'''


# 7. Systemd Service File (avatararts.service)
systemd_service_content = '''
[Unit]
Description=AvatarArts Website
After=network.target

[Service]
Type=notify
User=www-data
Group=www-data
WorkingDirectory=/path/to/avatararts
EnvironmentFile=/path/to/avatararts/.env
ExecStart=/usr/local/bin/gunicorn --config gunicorn.conf.py CORE.APP.app:app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
'''

# Print all configuration files for reference
print("=== GUNICORN CONFIGURATION ===")
print("# File: gunicorn.conf.py")
print("# This configuration should be placed in the root directory of the project")
print()

print("=== NGINX CONFIGURATION ===")
print("# File: /etc/nginx/sites-available/avatararts")
print("# Enable with: sudo ln -s /etc/nginx/sites-available/avatararts /etc/nginx/sites-enabled/")
print()

print("=== DOCKERFILE ===")
print("# File: Dockerfile")
print("# Build with: docker build -t avatararts .")
print()

print("=== DOCKER COMPOSE ===")
print("# File: docker-compose.yml")
print("# Run with: docker-compose up -d")
print()

print("=== ENVIRONMENT VARIABLES ===")
print("# File: .env (copy from .env.example and customize)")
print()

print("=== DEPLOYMENT SCRIPT ===")
print("# File: deploy.sh")
print("# Make executable: chmod +x deploy.sh")
print()

print("=== SYSTEMD SERVICE ===")
print("# File: /etc/systemd/system/avatararts.service")
print("# Enable with: sudo systemctl enable avatararts")
print()