#!/bin/bash

docker compose down
docker ps -n 3 -q > /dev/null || docker rm $(docker ps -n 3 -q)
docker rmi -f nginx-docker-compose-showip-app1:latest 
docker rmi -f nginx-docker-compose-showip-app2:latest
docker rmi -f nginx-docker-compose-showip-app3:latest
docker volume rm nginx-docker-compose-showip_volgz 

if [[ $1 = "-r" ]]; then 
    docker-compose up --build
fi
