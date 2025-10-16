# Quick Start Deployment Guide

This is a condensed version of the deployment guide for getting started quickly.

## Prerequisites

- Python 3.12+
- PostgreSQL database
- Production server or cloud platform account

## 5-Minute Deployment (Heroku)

### 1. Install and Login to Heroku

```bash
# Install Heroku CLI (if not already installed)
# Visit: https://devcenter.heroku.com/articles/heroku-cli

heroku login
```

### 2. Create App and Database

```bash
# Create Heroku app
heroku create your-chronos-api

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini
```

### 3. Set Environment Variables

```bash
# Generate a secret key first
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Set environment variables (replace values with your own)
heroku config:set DJANGO_ENV=production
heroku config:set SECRET_KEY="your-generated-secret-key"
heroku config:set ALLOWED_HOSTS="your-chronos-api.herokuapp.com"
heroku config:set CORS_ALLOWED_ORIGINS="https://your-frontend-app.com,https://www.your-frontend-app.com"
```

### 4. Deploy

```bash
# Add, commit, and push to Heroku
git add .
git commit -m "Prepare for deployment"
git push heroku main
```

### 5. Initialize Database

```bash
# Run migrations (may happen automatically via Procfile)
heroku run python manage.py migrate

# Create admin user
heroku run python manage.py createsuperuser
```

### 6. Test

```bash
# Check if app is running
heroku open

# View logs
heroku logs --tail
```

Your API is now live at `https://your-chronos-api.herokuapp.com`!

## Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `DJANGO_ENV` | Yes | Environment type | `production` |
| `SECRET_KEY` | Yes | Django secret key | Generate with command above |
| `ALLOWED_HOSTS` | Yes | Allowed domain names | `api.yourdomain.com` |
| `CORS_ALLOWED_ORIGINS` | Yes | Frontend URLs | `https://yourdomain.com` |
| `DATABASE_URL` | Yes* | Database connection | Auto-set by Heroku |
| `DEBUG` | No | Debug mode | `False` (default) |
| `SECURE_SSL_REDIRECT` | No | Force HTTPS | `True` (default) |

*Auto-configured by Heroku PostgreSQL addon

## Quick Local Development Setup

### 1. Install Dependencies

```bash
# Using pipenv (recommended)
pipenv install

# Or using pip
pip install -r requirements.txt
```

### 2. Set Up Environment

```bash
# Copy development environment file
cp .env.development .env
```

### 3. Run Migrations

```bash
# Using pipenv
pipenv run python manage.py migrate

# Or directly
python manage.py migrate
```

### 4. Seed Database (Optional)

```bash
bash seed_database.sh
```

### 5. Run Server

```bash
# Using pipenv
pipenv run python manage.py runserver

# Or using make
make run
```

Server runs at `http://127.0.0.1:8000`

## Connect Your Frontend

Update your React frontend's API URL:

```javascript
// In your frontend config or .env file
const API_URL = process.env.REACT_APP_API_URL || 'https://your-chronos-api.herokuapp.com';
```

## Testing the API

### Test Registration

```bash
curl -X POST https://your-chronos-api.herokuapp.com/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "TestPass123",
    "first_name": "Test",
    "last_name": "User",
    "email": "test@example.com",
    "address": "123 Test St",
    "phone": "1234567890",
    "city": "TestCity",
    "state": "TS",
    "postalCode": "12345"
  }'
```

### Test Login

```bash
curl -X POST https://your-chronos-api.herokuapp.com/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "TestPass123"}'
```

Response will include a token:
```json
{
  "valid": true,
  "token": "your-auth-token",
  "customer_id": 1
}
```

### Test Authenticated Endpoint

```bash
curl https://your-chronos-api.herokuapp.com/watches/ \
  -H "Authorization: Token your-auth-token"
```

## Common Issues

### 1. Static Files 404

**Solution:** Run collectstatic
```bash
heroku run python manage.py collectstatic --noinput
```

### 2. Database Connection Error

**Solution:** Check DATABASE_URL is set
```bash
heroku config:get DATABASE_URL
```

### 3. CORS Errors

**Solution:** Add frontend URL to CORS_ALLOWED_ORIGINS
```bash
heroku config:set CORS_ALLOWED_ORIGINS="https://your-frontend.com"
```

### 4. 500 Internal Server Error

**Solution:** Check logs
```bash
heroku logs --tail
```

## Next Steps

1. Set up custom domain (see full DEPLOYMENT.md)
2. Configure SSL certificate
3. Set up monitoring and logging
4. Implement database backups
5. Configure CI/CD pipeline

For detailed deployment instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md)
