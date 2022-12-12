#!/bin/bash

rm db.sqlite3
rm -rf ./chronosapi/migrations
python3 manage.py makemigrations chronosapi
python3 manage.py migrate
python3 manage.py migrate chronosapi
python3 manage.py loaddata users
python3 manage.py loaddata customers
python3 manage.py loaddata tokens
python3 manage.py loaddata watches
python3 manage.py loaddata favoritewatches
python3 manage.py loaddata reviews
python3 manage.py loaddata watchtypes