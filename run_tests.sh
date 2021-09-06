#! /bin/bash

DOCKER_POSTGRES_PASS="test-runner-pw"
docker-compose -f docker-compose-testing.yaml up --exit-code-from test_runner --build --remove-orphans
