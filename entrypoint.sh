#! /bin/sh

echo "Waiting for 5 seconds for postgres to start"
sleep 5
python3 manage.py migrate

echo "Preparations done, starting server"
python3 manage.py runserver 0.0.0.0:8000
