VENV := $(shell pipenv --venv 2>/dev/null)
PY := pipenv run python3

.PHONY: run bg stop seed shell

run:
	$(PY) manage.py runserver 127.0.0.1:8000

bg:
	@echo "Starting server in background and logging to server.log"
	@nohup pipenv run python3 manage.py runserver 127.0.0.1:8000 --noreload > server.log 2>&1 & echo $$! > .server_pid

stop:
	@if [ -f .server_pid ]; then \
		pid=$$(cat .server_pid); \
		echo "Killing $$pid"; \
		kill $$pid || true; \
		rm -f .server_pid; \
	else \
		echo "No .server_pid file found; use 'ps aux | grep manage.py' to find running server"; \
	fi

seed:
	chmod +x seed_database.sh && pipenv run bash seed_database.sh

shell:
	pipenv shell
