#! /bin/sh

echo "Waiting for 5 seconds for postgres to start"
sleep 5
python3 manage.py makemigrations
python3 manage.py migrate
if [ "${DJANGO_TESTING}"="true" ]; then
    echo "DJANGO_TESTING is set to true, starting tests"
    python3 manage.py test
else
    echo "Preparations done, starting server"
    python3 manage.py runserver 0.0.0.0:8000
fi
