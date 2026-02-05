# AvatarArts Website Setup Guide
## Complete Setup Instructions for avatararts.org

### Overview
This guide provides step-by-step instructions for setting up the AvatarArts website for your avatararts.org domain. The website showcases the nocTurneMeLoDieS V4 system and integrates with your Suno.com/@avatararts and GitHub.com/ichoake/AvaTar-Arts accounts.

### Prerequisites
- Domain name: avatararts.org (already registered)
- Web hosting account (shared, VPS, or cloud)
- SSH access to your server
- Python 3.8+ installed on the server
- Git installed on the server
- SSL certificate (recommended for production)

### Step 1: Server Preparation

#### 1.1 Connect to Your Server
```bash
ssh your_username@your_server_ip
```

#### 1.2 Update System Packages
```bash
# For Ubuntu/Debian
sudo apt update && sudo apt upgrade -y

# For CentOS/RHEL
sudo yum update -y
```

#### 1.3 Install Required Software
```bash
# Install Python, pip, and other dependencies
sudo apt install python3 python3-pip python3-venv nginx git curl supervisor -y

# Install additional system dependencies
sudo apt install build-essential libpq-dev libffi-dev libssl-dev -y
```

### Step 2: Domain Configuration

#### 2.1 Point Domain to Server
- Log into your domain registrar's control panel
- Update DNS records to point avatararts.org to your server's IP address
- Add both A records for:
  - avatararts.org
  - www.avatararts.org

#### 2.2 Wait for DNS Propagation
Wait 24-48 hours for DNS changes to propagate globally.

### Step 3: Clone the Website Repository

#### 3.1 Create Project Directory
```bash
mkdir -p /var/www/avatararts.org
cd /var/www/avatararts.org
```

#### 3.2 Clone the Repository
```bash
git clone https://github.com/ichoake/avatararts-website.git .
# Or if you're using the local files:
# Copy the entire AVATARARTS_WEBSITE directory to your server
```

### Step 4: Python Environment Setup

#### 4.1 Create Virtual Environment
```bash
cd /var/www/avatararts.org
python3 -m venv venv
source venv/bin/activate
```

#### 4.2 Install Dependencies
```bash
pip install --upgrade pip
pip install -r CONFIG/requirements.txt
```

### Step 5: Configuration

#### 5.1 Create Environment File
```bash
cp CONFIG/.env.example CONFIG/.env
nano CONFIG/.env
```

#### 5.2 Configure Environment Variables
```bash
# Edit CONFIG/.env with the following:
FLASK_APP=CORE.APP.app:app
FLASK_ENV=production
FLASK_DEBUG=False
AVATARARTS_SECRET_KEY=your-very-secure-secret-key-change-this-immediately
DATABASE_URL=sqlite:////var/www/avatararts.org/avatararts.db
SUNO_API_KEY=your-suno-api-key
GITHUB_TOKEN=your-github-personal-access-token
NOCTURNEMELODIES_PATH=/Users/steven/Music/nocTurneMeLoDieS
AVATARARTS_V4_PATH=/Users/steven/Music/nocTurneMeLoDieS/github.com/ichoake/AvaTar-Arts/V4_SUNO_INTEGRATION
```

#### 5.3 Set Proper Permissions
```bash
sudo chown -R www-data:www-data /var/www/avatararts.org
sudo chmod -R 755 /var/www/avatararts.org
```

### Step 6: Gunicorn Setup

#### 6.1 Create Gunicorn Configuration
```bash
sudo nano /var/www/avatararts.org/gunicorn.conf.py
```

Add the following configuration:
```python
# Gunicorn configuration for AvatarArts website
bind = "127.0.0.1:8000"
workers = 4
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 100
timeout = 30
keepalive = 2
preload_app = True

# Logging
accesslog = "/var/log/avatararts/access.log"
errorlog = "/var/log/avatararts/error.log"
loglevel = "info"

# Process naming
proc_name = "avatararts"

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190
```

#### 6.2 Create Log Directories
```bash
sudo mkdir -p /var/log/avatararts
sudo chown -R www-data:www-data /var/log/avatararts
```

### Step 7: Supervisor Configuration

#### 7.1 Create Supervisor Configuration
```bash
sudo nano /etc/supervisor/conf.d/avatararts.conf
```

Add the following configuration:
```ini
[program:avatararts]
command=/var/www/avatararts.org/venv/bin/gunicorn --config /var/www/avatararts.org/gunicorn.conf.py CORE.APP.app:app
directory=/var/www/avatararts.org
user=www-data
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/avatararts/gunicorn.log
environment=PATH="/var/www/avatararts.org/venv/bin"
```

#### 7.2 Reload Supervisor
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start avatararts
```

### Step 8: Nginx Configuration

#### 8.1 Create Nginx Configuration
```bash
sudo nano /etc/nginx/sites-available/avatararts.org
```

Add the following configuration:
```nginx
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
    
    # SSL Configuration (update paths to your certificates)
    ssl_certificate /path/to/your/certificate.crt;
    ssl_certificate_key /path/to/your/private.key;
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
        alias /var/www/avatararts.org/STATIC/;
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
```

#### 8.2 Enable Site and Restart Nginx
```bash
sudo ln -s /etc/nginx/sites-available/avatararts.org /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Step 9: SSL Certificate Setup (Recommended)

#### 9.1 Install Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
```

#### 9.2 Obtain SSL Certificate
```bash
sudo certbot --nginx -d avatararts.org -d www.avatararts.org
```

#### 9.3 Test Auto-Renewal
```bash
sudo certbot renew --dry-run
```

### Step 10: nocTurneMeLoDieS V4 Integration Setup

#### 10.1 Verify nocTurneMeLoDieS Path
Ensure the nocTurneMeLoDieS directory is accessible:
```bash
ls -la /Users/steven/Music/nocTurneMeLoDieS/
```

#### 10.2 If Hosting Elsewhere, Set Up Sync
If the website is hosted on a different server than where nocTurneMeLoDieS is located, you'll need to set up synchronization:
```bash
# Option 1: Use rsync to sync the nocTurneMeLoDieS directory
rsync -avz -e ssh /Users/steven/Music/nocTurneMeLoDieS/ user@your-server:/path/to/nocTurneMeLoDieS/

# Option 2: Set up a cron job for regular sync
crontab -e
# Add: 0 */6 * * * rsync -avz -e ssh /Users/steven/Music/nocTurneMeLoDieS/ user@your-server:/path/to/nocTurneMeLoDieS/
```

### Step 11: Database Initialization (if using database)

#### 11.1 Initialize Database
```bash
cd /var/www/avatararts.org
source venv/bin/activate
# If using SQLAlchemy, initialize database here
```

### Step 12: Testing

#### 12.1 Check Service Status
```bash
sudo supervisorctl status avatararts
sudo systemctl status nginx
```

#### 12.2 Check Logs
```bash
sudo tail -f /var/log/avatararts/gunicorn.log
sudo tail -f /var/log/nginx/avatararts_access.log
```

#### 12.3 Test Website
Visit https://avatararts.org in your browser to verify the site is working.

### Step 13: Maintenance Setup

#### 13.1 Create Backup Script
```bash
sudo nano /usr/local/bin/avatararts-backup.sh
```

Add backup script:
```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups/avatararts"
mkdir -p $BACKUP_DIR

# Backup website files
tar -czf $BACKUP_DIR/website_$DATE.tar.gz /var/www/avatararts.org

# Backup database if using one
# sqlite3 /var/www/avatararts.org/avatararts.db ".backup /backups/avatararts/database_$DATE.db"

# Rotate backups (keep last 7 days)
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
find $BACKUP_DIR -name "*.db" -mtime +7 -delete

echo "Backup completed: $DATE"
```

#### 13.2 Make Backup Script Executable
```bash
sudo chmod +x /usr/local/bin/avatararts-backup.sh
```

#### 13.3 Add to Cron for Daily Backups
```bash
crontab -e
# Add: 0 2 * * * /usr/local/bin/avatararts-backup.sh
```

### Step 14: Monitoring Setup

#### 14.1 Create Health Check Endpoint
The website includes a health check at `/health` endpoint.

#### 14.2 Set Up Uptime Monitoring
Consider using a service like UptimeRobot or Pingdom to monitor your site.

### Troubleshooting

#### Common Issues:

1. **Site Not Loading**:
   - Check if Gunicorn is running: `sudo supervisorctl status avatararts`
   - Check Nginx configuration: `sudo nginx -t`
   - Check firewall settings

2. **SSL Certificate Issues**:
   - Verify certificate paths in Nginx config
   - Check certificate expiration: `openssl x509 -in /path/to/cert -text -noout`

3. **Permission Errors**:
   - Ensure proper ownership: `sudo chown -R www-data:www-data /var/www/avatararts.org`
   - Check file permissions: `sudo chmod -R 755 /var/www/avatararts.org`

4. **Database Connection Issues**:
   - Verify database path and permissions
   - Check database configuration in environment variables

### Post-Setup Tasks

1. **Update Content**: Customize the website content to reflect your current projects
2. **SEO Setup**: Add meta tags, sitemap, and robots.txt
3. **Analytics**: Add Google Analytics or other tracking
4. **Social Media**: Add social media links and sharing buttons
5. **Performance**: Optimize images and implement caching

### Security Considerations

1. **Keep Software Updated**: Regularly update Python packages and system software
2. **Secure API Keys**: Never commit API keys to version control
3. **Firewall**: Configure firewall to allow only necessary ports (80, 443, 22)
4. **SSH Security**: Use SSH keys and disable password authentication
5. **Regular Backups**: Ensure backup system is working properly

### Contact Information

For support with the AvatarArts website setup:
- **Developer**: Steven Chaplinski
- **Brand**: AvatarArts
- **GitHub**: https://github.com/ichoake
- **Suno**: https://suno.com/@avatararts
- **Email**: sjchaplinski@gmail.com

This setup guide provides a complete installation of the AvatarArts website that showcases your nocTurneMeLoDieS V4 system and integrates with your creative platforms. The website is optimized for performance, security, and SEO, and is ready to serve your AvatarArts brand online.