#!/bin/sh

BASE_DIR=/home/dali/WORK/work04

mkdir -p $BASE_DIR
cp templates/.gitignore ${BASE_DIR}
cp templates/README.md ${BASE_DIR}

services="auth atelier catalogue vehicule rdv"
for s in $(echo $services) 
do
    mkdir -p "${BASE_DIR}/services/$s-service/src"
    cp templates/Dockerfile-service "${BASE_DIR}/services/$s-service/Dockerfile"
    cp templates/docker-compose-service.yaml "${BASE_DIR}/services/$s-service/docker-compose.yaml"
    mkdir -p "${BASE_DIR}/services/$s-service/src/app"
    cp templates/.env "${BASE_DIR}/services/$s-service/src/.env"
    cp templates/main.py "${BASE_DIR}/services/$s-service/src/main.py"
    cp templates/requirements.txt "${BASE_DIR}/services/$s-service/src/requirements.txt"  
    cp templates/config.py "${BASE_DIR}/services/$s-service/src/app/config.py"      
    cp templates/database.py "${BASE_DIR}/services/$s-service/src/app/database.py"
    touch "${BASE_DIR}/services/$s-service/src/app/repositories.py"    
    touch "${BASE_DIR}/services/$s-service/src/app/routers.py"    
    touch "${BASE_DIR}/services/$s-service/src/app/schemas.py" 
    cp templates/models.py "${BASE_DIR}/services/$s-service/src/app/models.py"        
    touch "${BASE_DIR}/services/$s-service/src/app/events.py"        
    touch "${BASE_DIR}/services/$s-service/src/app/utils.py"        
    mkdir -p "${BASE_DIR}/databases/$s-db"
    cp templates/.env "${BASE_DIR}/databases/$s-db/.env"
    cp templates/Dockerfile-db "${BASE_DIR}/databases/$s-db/Dockerfile"
    cp templates/docker-compose-db.yaml "${BASE_DIR}/databases/$s-db/docker-compose.yaml"
done

consumers="rdv"
for s in $(echo $consumers) 
do
    mkdir -p "${BASE_DIR}/consumers/$s-web/src"
    cp templates/Dockerfile-service "${BASE_DIR}/consumers/$s-web/Dockerfile"
    cp templates/docker-compose-service.yaml "${BASE_DIR}/consumers/$s-web/docker-compose.yaml"
    mkdir -p "${BASE_DIR}/consumers/$s-web/src/app"
    cp templates/main.py "${BASE_DIR}/consumers/$s-web/src/main.py"
    cp templates/requirements.txt "${BASE_DIR}/consumers/$s-web/src/requirements.txt"  
    touch "${BASE_DIR}/consumers/$s-web/src/app/routers.py"    
    touch "${BASE_DIR}/consumers/$s-web/src/app/schemas.py" 
    cp templates/models.py "${BASE_DIR}/consumers/$s-web/src/app/models.py"        
    touch "${BASE_DIR}/consumers/$s-web/src/app/utils.py"        
done

mkdir -p ${BASE_DIR}/infra/event-bus
mkdir -p ${BASE_DIR}/infra/event-store
mkdir -p ${BASE_DIR}/infra/reverse-proxy
