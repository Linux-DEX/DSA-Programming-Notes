# Quick Command

## Run a new container

+ New Image - `docker run IMAGE`
+ Name Container and Launch Image - `docker run --name CONTAINER IMAGE`
+ Map Container Ports and Launch Image - `docker run -p HOSTPORT:CONTAINERPORT IMAGE`
+ Map ALL Ports and Launch Image - `docker run -P IMAGE`
+ Launch Image as Background Service - `docker run -d IMAGE`
+ Map Local Directory and Launch - `docker run -v HOSTDIR:TARGETDIR IMAGE`

## Manage Containers 

+ List RUNNING Containers - `docker ps`
+ List ALL containers - `docker ps -a`
+ Delete container - `docker rm CONTAINER`
+ Delete a Running Container - `docker rm -f CONTAINER`
+ Stop Container - `docker stop CONTAINER`
+ Start Container - `docker start CONTAINER`
+ Copy File FROM container - `docker cp CONTAINER:SOURCE TARGET`
+ Copy File TO container - `docker cp TARGET CONTAINER:SOURCE`
+ Start Shell inside container - `docker exec -it CONTAINER bash`
+ Rename container - `docker rename OLD NEW`
+ Create new Image from container - `docker commit CONTAINER`

## Manage Images

+ Download Image - `docker pull IMAGE[:TAG]`
+ Upload Image to repository - `docker push IMAGE`
+ Delete Image - `docker rmi IMAGE`
+ List Image - `docker images`
+ Build Image from Docker file - `docker build DIRECTORY`
+ Tag image IMAGE - `docker tag IMAGE NEWIMAGE:TAG`

## Troubleshooting and Information

+ Show logs - `docker logs CONTAINER`
+ Show stats - `docker stats`
+ Show processes - `docker top CONTAINER`
+ Show modifies files - `docker diff CONTAINER`
+ Show mapped ports - `docker port CONTAINER`

## Networking Commands

+ Create Network - `docker network create NETWORK_NAME`
+ List Networks - `docker network ls`
+ Inspect Network - `docker network inspect NETWORK_NAME`
+ Remove Network - `docker network rm NETWORK_NAME`
+ Connect container to network - `docker network connect NETWORK_NAME CONTAINER`
+ Disconnect container from network - `docker network disconnect NETWORK_NAME CONTAINER`

## Docker Build Arguments and Multi-stage Builds

+ Build with build arguments - `docker build --build-arg ARG_NAME=VALUE`
+ Build from a Dockerfile with a specific tag - `docker build -t IMAGE_NAME:TAG`

## **System Overview**

- **Show Docker system-wide information**  `docker system df`
- **Show detailed information about Docker system**  `docker system info`

## **Cleaning Up Docker Resources**

- **Clean up unused data (containers, images, networks, and volumes)**  `docker system prune`  
- **Clean up only unused volumes**  `docker volume prune`
- **Clean up only unused networks**  `docker network prune`
- **Clean up only dangling images**  `docker image prune`
- **Clean up only stopped containers**  `docker container prune`

## **Managing Docker Resources**

- **Show information about disk usage by Docker**  `docker system df`
- **Show information about unused and dangling resources**  `docker system prune -a`  


## **Docker Resource Information**

- **Show information about containers**  `docker ps -a`
- **Show information about images**  `docker images`
- **Show information about volumes**  `docker volume ls`
- **Show information about networks**  `docker network ls`

## **Docker System Maintenance**

- **Remove all stopped containers, unused images, and networks**  `docker system prune -a --volumes`
- **Remove a specific image**  `docker rmi IMAGE_ID`  
- **Remove a specific container**  `docker rm CONTAINER_ID`
- **Remove a specific volume**  `docker volume rm VOLUME_NAME`

## **Swarm Management (if using Docker Swarm)**

- **List active nodes in the Swarm**  `docker node ls`
- **Show information about the current Swarm status**  `docker swarm inspect`
- **Leave the Swarm**  `docker swarm leave`


## **System-Wide Configuration**

- **Set Docker daemon to start on boot**  `sudo systemctl enable docker`
- **Start Docker daemon**  `sudo systemctl start docker`
- **Stop Docker daemon**  `sudo systemctl stop docker`
- **Restart Docker daemon**: `sudo systemctl restart docker`
