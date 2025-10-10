<<<<<<< HEAD
# Chronos

Quick start
-----------

This project uses Pipenv. From the project root:

1. Install dependencies:

```bash
pipenv install --dev
```

2. (Optional) Activate shell:

```bash
pipenv shell
```

3. Seed the database (destructive — removes `db.sqlite3`):

```bash
# use the Makefile target
make seed
# or directly
chmod +x seed_database.sh
pipenv run bash seed_database.sh
```

4. Start the dev server:

```bash
# foreground
make run
# or background (writes PID to .server_pid and logs to server.log)
make bg
# to stop
make stop
```

5. Test the login endpoint:

```bash
curl -X POST http://127.0.0.1:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"test_login_user","password":"TestPass123"}'
```

Notes
-----
- `ALLOWED_HOSTS` can be configured via the environment variable `ALLOWED_HOSTS` (comma-separated). Defaults to `127.0.0.1,localhost,testserver`.
- The `seed` script deletes the database and `chronosapi/migrations` and recreates/apply migrations before loading fixtures.
- In production, don't use the Django dev server and make sure `DEBUG = False` and `ALLOWED_HOSTS` are set appropriately.
=======
Clipped is a modern social media web app for watch enthusiasts. Built for collectors and casual fans alike, it provides a sleek space to share, discover, and discuss watches — blending design simplicity with powerful web technology.

🌟 Overview

Clipped lets users:

Showcase their personal watch collections

Engage with others through likes, comments, and saves

Browse a community feed of shared timepieces

Enjoy a responsive, elegant user interface built with React

🧰 Tech Stack Category - Technologies Frontend - React, Tailwind CSS, React Router Backend - Django REST Framework Database - SQLite / PostgreSQL Utilities - Axios, Django CORS Headers, REST API Integration Version Control - Git & GitHub
>>>>>>> 74bca01d0986c8e6531ea3ac3a7b1ce07d9c0554
