# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Chronos is a Django REST Framework API for a watch collection/marketplace application. Users can manage watches, create reviews, add favorites, and receive suggestions. The backend uses SQLite for development and token-based authentication.

## Architecture

### Core Components

- **chronosserver/**: Django project configuration
  - `settings.py`: Configured with DRF, TokenAuthentication, CORS for React client at localhost:3000
  - `urls.py`: Main URL routing with DRF router and auth endpoints at `/register/` and `/login/`

- **chronosapi/**: Main application module
  - `models/`: Domain models with Django ORM
    - `Customer`: Extends Django User with OneToOne relationship, includes address/contact info and profile image
    - `Watch`: User-created watches with WatchType FK, owned by Customer
    - `WatchType`: Category model for watches
    - `Suggestion`: Admin-suggested watches (separate from user watches)
    - `Review`: User reviews on watches
    - `FavoriteWatch`: Many-to-many join table for customer favorites
  - `views/`: DRF ViewSets with custom actions
    - All views use DRF ViewSets with standard CRUD methods
    - `CustomerView.currentCustomer`: Custom action (GET/PUT) to retrieve/update authenticated user's profile
    - Authentication required by default (REST_FRAMEWORK settings), except `/login/` and `/register/`
  - `fixtures/`: Seed data in JSON format (users, customers, tokens, watches, etc.)

### Authentication Flow

- Registration: POST to `/register/` creates User + Customer, returns token
- Login: POST to `/login/` authenticates and returns token
- All API endpoints require `Authorization: Token <token>` header (except auth endpoints)
- Test user available after seeding: `test_login_user` / `TestPass123`

### Database Seeding

The `seed_database.sh` script:
1. Deletes `db.sqlite3` and `chronosapi/migrations/`
2. Creates fresh migrations with `makemigrations chronosapi`
3. Runs migrations
4. Loads fixtures in specific order (users → customers → tokens → watchtypes → watches → suggestions → favoritewatches → reviews)

## Development Commands

### Environment Setup

```bash
# Install dependencies (includes autopep8, pylint, pylint-django)
pipenv install --dev

# Activate virtual environment (optional)
pipenv shell
```

### Database Management

```bash
# Reset and seed database (destructive - removes db.sqlite3 and migrations)
make seed
# or
pipenv run bash seed_database.sh

# Create migrations only
pipenv run python3 manage.py makemigrations chronosapi

# Apply migrations only
pipenv run python3 manage.py migrate
```

### Running the Server

```bash
# Run in foreground
make run
# or
pipenv run python3 manage.py runserver 127.0.0.1:8000

# Run in background (logs to server.log, PID in .server_pid)
make bg

# Stop background server
make stop
```

### Testing

```bash
# Run all tests
pipenv run python3 manage.py test chronosapi

# Run specific test
pipenv run python3 manage.py test chronosapi.tests.TestClassName
```

### Code Quality

```bash
# Format with autopep8
pipenv run autopep8 --in-place --aggressive --aggressive <file>

# Lint with pylint
pipenv run pylint chronosapi/
```

## Configuration Notes

- **ALLOWED_HOSTS**: Set via environment variable `ALLOWED_HOSTS` (comma-separated). Defaults to `127.0.0.1,localhost,testserver`
- **CORS**: Configured for `http://localhost:3000` and `http://127.0.0.1:3000`
- **Database**: SQLite (`db.sqlite3`) - for production use PostgreSQL or similar
- **Authentication**: DRF TokenAuthentication is the default authentication class

## API Endpoints

- `/register/` (POST, no auth): Create new user account
- `/login/` (POST, no auth): Authenticate and get token
- `/customers/` (ViewSet): Customer CRUD
- `/customers/currentCustomer/` (GET/PUT): Retrieve or update authenticated user's profile
- `/watches/` (ViewSet): Watch CRUD
- `/watchtypes/` (ViewSet): WatchType CRUD
- `/suggestions/` (ViewSet): Suggestion CRUD
- `/reviews/` (ViewSet): Review CRUD
- `/favoritewatches/` (ViewSet): FavoriteWatch CRUD

All ViewSet routes follow DRF conventions (list, retrieve, create, update, destroy).
