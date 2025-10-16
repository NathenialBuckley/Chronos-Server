# Chronos Server - Deployment Guide

This guide covers deploying the Chronos Django REST API to production environments.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Environment Configuration](#environment-configuration)
3. [Database Setup](#database-setup)
4. [Static Files](#static-files)
5. [Deployment Platforms](#deployment-platforms)
6. [Post-Deployment Steps](#post-deployment-steps)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

Before deploying, ensure you have:

- Python 3.12+ installed
- PostgreSQL database (recommended for production)
- A production server or cloud platform account
- Your frontend client deployed and accessible

## Environment Configuration

The project uses environment variables for configuration. Create a `.env` file in production with the following variables:

### Required Environment Variables

```bash
# Set to production
DJANGO_ENV=production

# Generate a strong secret key
# Run: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY=your-production-secret-key-here

# Debug should be False in production
DEBUG=False

# Your production domains (comma-separated)
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,api.yourdomain.com

# CORS allowed origins (include your React frontend URL)
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Database URL (PostgreSQL recommended)
DATABASE_URL=postgresql://user:password@host:5432/database_name

# Optional: Set to False if SSL is handled by reverse proxy
SECURE_SSL_REDIRECT=True
```

### Generating a Secret Key

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Database Setup

### PostgreSQL (Recommended)

1. Create a PostgreSQL database:
```bash
createdb chronos_production
```

2. Set the DATABASE_URL environment variable:
```bash
DATABASE_URL=postgresql://username:password@localhost:5432/chronos_production
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. (Optional) Load seed data:
```bash
bash seed_database.sh
```

## Static Files

Static files are served using WhiteNoise for efficient delivery.

### Collect Static Files

Before deploying, collect all static files:

```bash
python manage.py collectstatic --noinput
```

This command collects all static files into the `staticfiles/` directory.

## Deployment Platforms

### Option 1: Heroku

1. **Install Heroku CLI** and login:
```bash
heroku login
```

2. **Create a new Heroku app**:
```bash
heroku create your-app-name
```

3. **Add PostgreSQL addon**:
```bash
heroku addons:create heroku-postgresql:mini
```

4. **Set environment variables**:
```bash
heroku config:set DJANGO_ENV=production
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
heroku config:set CORS_ALLOWED_ORIGINS="https://your-frontend-domain.com"
```

5. **Deploy**:
```bash
git push heroku main
```

6. **Run migrations**:
```bash
heroku run python manage.py migrate
```

7. **Create superuser**:
```bash
heroku run python manage.py createsuperuser
```

### Option 2: DigitalOcean App Platform

1. **Connect your GitHub repository** to DigitalOcean

2. **Configure the app**:
   - Build Command: `pip install -r requirements-prod.txt && python manage.py collectstatic --noinput`
   - Run Command: `gunicorn chronosserver.wsgi:application --config gunicorn_config.py`

3. **Add a PostgreSQL database** through DigitalOcean

4. **Set environment variables** in the App Platform dashboard:
   - `DJANGO_ENV=production`
   - `SECRET_KEY=your-secret-key`
   - `ALLOWED_HOSTS=your-app-domain.ondigitalocean.app`
   - `CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com`
   - `DATABASE_URL` (automatically set by DigitalOcean database)

5. **Deploy** - DigitalOcean will automatically deploy when you push to your repository

### Option 3: AWS (EC2/Elastic Beanstalk)

1. **Elastic Beanstalk Configuration**:
   - Create `.ebextensions/` directory
   - Add configuration for Django static files and environment variables

2. **Initialize EB CLI**:
```bash
eb init -p python-3.12 chronos-server
```

3. **Create environment**:
```bash
eb create chronos-production
```

4. **Set environment variables**:
```bash
eb setenv DJANGO_ENV=production SECRET_KEY="your-secret-key" ALLOWED_HOSTS="your-eb-url.elasticbeanstalk.com"
```

5. **Deploy**:
```bash
eb deploy
```

### Option 4: Self-Hosted Server (Ubuntu/Debian)

1. **Install dependencies**:
```bash
sudo apt update
sudo apt install python3.12 python3-pip postgresql nginx
```

2. **Clone repository**:
```bash
git clone https://github.com/yourusername/Chronos-Server.git
cd Chronos-Server
```

3. **Create virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-prod.txt
```

4. **Set up PostgreSQL**:
```bash
sudo -u postgres createdb chronos_production
sudo -u postgres createuser chronos_user
```

5. **Create .env file** with production settings

6. **Run migrations and collect static**:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

7. **Set up Gunicorn with systemd**:
```bash
sudo nano /etc/systemd/system/chronos.service
```

Add:
```ini
[Unit]
Description=Chronos Django Server
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/Chronos-Server
Environment="PATH=/path/to/Chronos-Server/venv/bin"
ExecStart=/path/to/Chronos-Server/venv/bin/gunicorn chronosserver.wsgi:application --config gunicorn_config.py

[Install]
WantedBy=multi-user.target
```

8. **Set up Nginx**:
```bash
sudo nano /etc/nginx/sites-available/chronos
```

Add:
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location /static/ {
        alias /path/to/Chronos-Server/staticfiles/;
    }

    location /media/ {
        alias /path/to/Chronos-Server/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

9. **Enable and start services**:
```bash
sudo ln -s /etc/nginx/sites-available/chronos /etc/nginx/sites-enabled
sudo systemctl enable chronos
sudo systemctl start chronos
sudo systemctl restart nginx
```

10. **Set up SSL with Let's Encrypt**:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

## Post-Deployment Steps

### 1. Verify Deployment

```bash
curl https://your-domain.com/admin/
```

### 2. Create Admin User

If you haven't already:
```bash
python manage.py createsuperuser
```

### 3. Test Authentication Endpoints

Test registration:
```bash
curl -X POST https://your-domain.com/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123",
    "first_name": "Test",
    "last_name": "User",
    "email": "test@example.com"
  }'
```

Test login:
```bash
curl -X POST https://your-domain.com/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### 4. Update Frontend Configuration

Update your React frontend to use the production API URL:
```javascript
const API_URL = 'https://your-api-domain.com';
```

### 5. Monitor Logs

Monitor application logs for errors:

**Heroku:**
```bash
heroku logs --tail
```

**Self-hosted:**
```bash
sudo journalctl -u chronos -f
```

## Troubleshooting

### Static Files Not Loading

1. Ensure WhiteNoise is in INSTALLED_APPS (it's in settings_base.py)
2. Run `python manage.py collectstatic --noinput`
3. Check that STATIC_ROOT is set correctly

### Database Connection Issues

1. Verify DATABASE_URL is set correctly
2. Check database credentials
3. Ensure database server allows connections from your app server
4. Test connection: `python manage.py dbshell`

### CORS Errors

1. Verify CORS_ALLOWED_ORIGINS includes your frontend URL
2. Check that the protocol (http/https) matches
3. Ensure django-cors-headers is installed

### 500 Internal Server Error

1. Check application logs
2. Verify all environment variables are set
3. Ensure SECRET_KEY is set
4. Check ALLOWED_HOSTS includes your domain

### SSL Certificate Issues

1. Verify SECURE_SSL_REDIRECT setting
2. If using a reverse proxy (nginx), you might need to set `SECURE_SSL_REDIRECT=False`
3. Check that X-Forwarded-Proto header is being passed

## Security Checklist

- [ ] SECRET_KEY is unique and not exposed
- [ ] DEBUG is set to False
- [ ] ALLOWED_HOSTS is properly configured
- [ ] CORS_ALLOWED_ORIGINS only includes trusted domains
- [ ] Database uses strong password
- [ ] SSL/HTTPS is enabled
- [ ] Regular database backups are configured
- [ ] Security updates are applied regularly

## Maintenance

### Database Backups

**Heroku:**
```bash
heroku pg:backups:capture
heroku pg:backups:download
```

**Self-hosted:**
```bash
pg_dump chronos_production > backup_$(date +%Y%m%d).sql
```

### Updating the Application

1. Pull latest changes:
```bash
git pull origin main
```

2. Install dependencies:
```bash
pip install -r requirements-prod.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Collect static files:
```bash
python manage.py collectstatic --noinput
```

5. Restart application:
```bash
# Heroku
heroku restart

# Self-hosted
sudo systemctl restart chronos
```

## Scaling

### Horizontal Scaling

Increase the number of Gunicorn workers by setting the `WEB_CONCURRENCY` environment variable:
```bash
export WEB_CONCURRENCY=4
```

### Database Scaling

Consider upgrading your database plan or implementing read replicas for high-traffic applications.

### Caching

Implement Redis caching for improved performance:
```bash
# Install Redis
pip install django-redis

# Add to settings
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

## Support

For issues or questions:
- Check the [GitHub Issues](https://github.com/yourusername/Chronos-Server/issues)
- Review Django documentation: https://docs.djangoproject.com/
- Review DRF documentation: https://www.django-rest-framework.org/
