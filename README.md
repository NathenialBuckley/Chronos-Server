# Chronos - Watch Collection API

Chronos is a Django REST Framework API for a watch collection and marketplace application. Built for watch enthusiasts, collectors, and casual fans, it provides a robust backend for managing watch collections, reviews, favorites, and suggestions.

## Features

- User authentication with token-based auth
- Watch collection management
- User reviews and ratings
- Favorite watches functionality
- Admin-curated watch suggestions
- RESTful API with Django REST Framework
- CORS support for React frontend

## Tech Stack

- **Backend Framework**: Django 5.2+ with Django REST Framework
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: Token-based authentication
- **API**: RESTful API with DRF ViewSets
- **Static Files**: WhiteNoise for efficient serving
- **WSGI Server**: Gunicorn for production

## Quick Start (Development)

### Prerequisites

- Python 3.12+
- pipenv (recommended) or pip

### Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd Chronos-Server
```

2. **Install dependencies**:
```bash
pipenv install --dev
# or with pip
pip install -r requirements.txt
```

3. **(Optional) Activate virtual environment**:
```bash
pipenv shell
```

4. **Seed the database** (creates test data):
```bash
make seed
# or directly
bash seed_database.sh
```

This script will:
- Delete existing `db.sqlite3` and migrations
- Create fresh migrations
- Apply migrations
- Load fixture data (users, watches, types, reviews, etc.)

5. **Run the development server**:
```bash
# Foreground
make run
# or
pipenv run python manage.py runserver

# Background (logs to server.log)
make bg

# Stop background server
make stop
```

Server runs at `http://127.0.0.1:8000`

### Test the API

**Test login** (after seeding):
```bash
curl -X POST http://127.0.0.1:8000/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test_login_user","password":"TestPass123"}'
```

**Test registration**:
```bash
curl -X POST http://127.0.0.1:8000/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass",
    "first_name": "Test",
    "last_name": "User",
    "email": "test@example.com",
    "address": "123 Main St",
    "phone": "1234567890",
    "city": "TestCity",
    "state": "TS",
    "postalCode": "12345"
  }'
```

## API Endpoints

All endpoints except `/register/` and `/login/` require authentication via `Authorization: Token <token>` header.

| Endpoint | Methods | Description |
|----------|---------|-------------|
| `/register/` | POST | Create new user account (no auth required) |
| `/login/` | POST | Authenticate and receive token (no auth required) |
| `/customers/` | GET, POST, PUT, DELETE | Customer CRUD operations |
| `/customers/currentCustomer/` | GET, PUT | Get/update authenticated user profile |
| `/watches/` | GET, POST, PUT, DELETE | Watch CRUD operations |
| `/watchtypes/` | GET, POST, PUT, DELETE | Watch type/category operations |
| `/suggestions/` | GET, POST, PUT, DELETE | Admin watch suggestions |
| `/reviews/` | GET, POST, PUT, DELETE | Watch reviews |
| `/favoritewatches/` | GET, POST, DELETE | User favorite watches |
| `/admin/` | GET, POST | Django admin interface |

## Project Structure

```
Chronos-Server/
├── chronosserver/          # Django project configuration
│   ├── settings.py         # Settings router (dev/prod)
│   ├── settings_base.py    # Shared settings
│   ├── settings_dev.py     # Development settings
│   ├── settings_prod.py    # Production settings
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI configuration
├── chronosapi/             # Main application
│   ├── models/             # Database models
│   ├── views/              # API ViewSets
│   ├── fixtures/           # Seed data
│   └── migrations/         # Database migrations
├── staticfiles/            # Collected static files (production)
├── media/                  # User uploaded files
├── requirements.txt        # Python dependencies
├── requirements-prod.txt   # Production dependencies
├── Pipfile                 # Pipenv configuration
├── manage.py               # Django management script
├── gunicorn_config.py      # Gunicorn configuration
├── Procfile                # Heroku deployment config
└── seed_database.sh        # Database seeding script
```

## Configuration

### Environment Variables

The project uses environment variables for configuration. Set `DJANGO_ENV` to switch between development and production:

**Development** (default):
- Uses SQLite database
- DEBUG mode enabled
- Permissive CORS settings for localhost

**Production**:
- Requires PostgreSQL (or DATABASE_URL)
- DEBUG disabled
- Enhanced security settings
- Requires all environment variables to be set

See `.env.example` for all available configuration options.

### CORS Configuration

By default, the API allows requests from:
- `http://localhost:3000`
- `http://127.0.0.1:3000`

For production, set `CORS_ALLOWED_ORIGINS` environment variable with your frontend URLs.

## Development

### Database Management

**Create migrations**:
```bash
pipenv run python manage.py makemigrations chronosapi
```

**Apply migrations**:
```bash
pipenv run python manage.py migrate
```

**Reset and seed database**:
```bash
make seed
```

### Testing

```bash
# Run all tests
pipenv run python manage.py test chronosapi

# Run specific test
pipenv run python manage.py test chronosapi.tests.TestClassName
```

### Code Quality

```bash
# Format code
pipenv run autopep8 --in-place --aggressive --aggressive <file>

# Lint code
pipenv run pylint chronosapi/
```

## Deployment

### Quick Deployment to Heroku

See [DEPLOYMENT_QUICK_START.md](./DEPLOYMENT_QUICK_START.md) for a 5-minute deployment guide.

### Full Deployment Guide

See [DEPLOYMENT.md](./DEPLOYMENT.md) for comprehensive deployment instructions covering:
- Heroku
- DigitalOcean
- AWS Elastic Beanstalk
- Self-hosted servers (Ubuntu/Debian)

### Deployment Checklist

Use [DEPLOYMENT_CHECKLIST.md](./DEPLOYMENT_CHECKLIST.md) to ensure you don't miss any steps.

### Pre-Deployment Steps

1. **Install production dependencies**:
```bash
pip install -r requirements-prod.txt
```

2. **Set environment variables** (see `.env.example`)

3. **Collect static files**:
```bash
python manage.py collectstatic --noinput
```

4. **Run migrations**:
```bash
python manage.py migrate
```

5. **Create superuser**:
```bash
python manage.py createsuperuser
```

## Frontend Integration

This API is designed to work with a React frontend. Update your frontend configuration to point to the API:

```javascript
// Development
const API_URL = 'http://127.0.0.1:8000';

// Production
const API_URL = process.env.REACT_APP_API_URL || 'https://your-api-domain.com';
```

## Authentication Flow

1. **Register**: POST to `/register/` with user details
2. **Receive token**: Token is returned in response
3. **Login**: POST to `/login/` with username and password
4. **Use token**: Include `Authorization: Token <token>` header in all subsequent requests

Example authenticated request:
```bash
curl https://api.yourdomain.com/watches/ \
  -H "Authorization: Token your-auth-token-here"
```

## Security Notes

- Never commit `.env` files or secrets to version control
- Always use `DEBUG=False` in production
- Generate a strong `SECRET_KEY` for production
- Use HTTPS in production
- Keep dependencies up to date
- Use PostgreSQL (not SQLite) in production
- Implement regular database backups

## Troubleshooting

### Common Issues

**Database locked error**:
- SQLite doesn't handle concurrent writes well. Use PostgreSQL in production.

**CORS errors**:
- Ensure your frontend URL is in `CORS_ALLOWED_ORIGINS`
- Check that the protocol (http/https) matches

**Authentication errors**:
- Verify token is being sent in `Authorization` header
- Check token format: `Token <token>` (not `Bearer <token>`)

**Static files not loading**:
- Run `python manage.py collectstatic`
- Verify `STATIC_ROOT` and `STATIC_URL` settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Run linter and tests
6. Submit a pull request

## License

[Your license here]

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Review the [CLAUDE.md](./CLAUDE.md) for project guidance
- Check the [DEPLOYMENT.md](./DEPLOYMENT.md) for deployment help

---

Built with Django REST Framework
