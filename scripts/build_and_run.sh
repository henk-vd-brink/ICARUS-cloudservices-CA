#!/bin/bash

docker-compose -f docker-compose.build.yaml build
docker-compose --env-file .example.env up