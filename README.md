# str-django-application

small demo application for managing user accounts using django

## Setup through docker-compose

If you have `docker-compose` installed you can simply start the environment through docker.

In this case, you **need** to set the env variable `DOCKER_POSTGRES_PASS` to provide a password to the Postgres database and the django application.

```bash

# set the password for postgres and django
$ export DOCKER_POSTGRES_PASS="mysupersecretpassword"

# start the containers
$ docker-compose up
```

The application container will wait for 5 seconds, since postgres takes a short time for the process to accept new connections.

## Setup using virtual env and Postgres

### Prepare virtual environment

```bash
# Create virtual environment
$ python3 -m venv venv

# Activate virtual environment
$ source venv/bin/activate

# Upgrade pip to newest version
$ pip install --upgrade pip


# Install requirements from text file
$ pip install -r requirements.txt

```

### Postgres instruction (macos big sur)

```bash
# install postgres via homebrew
$ brew install postgres

# create database for django
$ createdb django

# start postgres service through homebrew service manager
$ brew service start postgres
```

## Start

```bash

# execute migrations on first-start
$ python manage.py migrate

# start django server
$ python manage.py runserver

```

## Environment variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| *DJANGO_DB_HOST* | Hostname of database server | localhost |
| *DJANGO_DB_PORT* | Port for database server | 5432 |
| *DJANGO_DB_USER* | Username to connect to database | empty string |
| *DJANGO_DB_PASS* | Password for database authentication | empty string |

In a terminal you can set an environment variable via `export` e.g.

```bash
# Set database hostname (or IP)
$ export DJANGO_DB_HOST="192.168.0.20"

# Set database port
$ export DJANGO_DB_PORT="35432"
```

## Running tests

To run the tests, you can execute the bash script called `run_tests.sh`

It will use `docker-compose` to run the services specified in `docker-compose-testing.yaml`

The test-runner container will wait for 5 seconds, since postgres takes a short time for the process to accept new connections.
