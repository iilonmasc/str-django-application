# str-django-application

small demo application for managing user accounts using django

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
