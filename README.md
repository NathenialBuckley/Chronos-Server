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