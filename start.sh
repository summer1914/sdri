#!/bin/bash

echo "stop"
docker stop sdri_web_5000
docker stop sdri_db_3306

echo "rm"
docker rm sdri_web_5000
docker rm sdri_db_3306

echo "run"
docker-compose -f docker-compose.yml run --no-deps -d -p 5000:5000 --name sdri_web_5000 web
docker-compose -f docker-compose.yml run --no-deps -d -p 3306:3306 --name sdri_db_3306 db

