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