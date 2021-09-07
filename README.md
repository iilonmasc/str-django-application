# str-django-application

small demo application for managing user accounts using django

## Setup through docker-compose

```bash

# set oauth client id
$ export DJANGO_SSO_CLIENT_ID="myOauthClientID"

# set oauth client secret
$ export DJANGO_SSO_CLIENT_SECRET="mySecretOauthClientSecret"

# set the password for postgres and django
$ export DOCKER_POSTGRES_PASS="mysupersecretpassword"

# start the containers
$ docker-compose up
```

The application container will wait for 5 seconds, since postgres takes a short time for the process to accept new connections.

You need to set a redir_url in GCP when creating the OAuth Webclient there. For local testing you may use `http://localhost:8000/accounts/google/login/callback/`

## Environment variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| *DJANGO_DB_HOST* | Hostname of database server | localhost |
| *DJANGO_DB_PORT* | Port for database server | 5432 |
| *DJANGO_DB_USER* | Username to connect to database | empty string |
| *DJANGO_DB_PASS* | Password for database authentication | empty string |
| *DJANGO_SSO_CLIENT_ID* | OAuth Client ID | empty string |
| *DJANGO_SSO_CLIENT_SECRET* | Secret for OAuth Client | empty string |

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
