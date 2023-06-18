#!/bin/bash

docker compose down
docker ps -n 3 -q > /dev/null || docker rm $(docker ps -n 3 -q)
docker rmi -f ecs-ecr-docker-nginx-showip-app1:latest 
docker rmi -f ecs-ecr-docker-nginx-showip-app2:latest
docker rmi -f ecs-ecr-docker-nginx-showip-app3:latest
docker volume rm ecs-ecr-docker-nginx-showip_volgz 

if [[ $1 = "-r" ]]; then 
    docker-compose up --build
fi
