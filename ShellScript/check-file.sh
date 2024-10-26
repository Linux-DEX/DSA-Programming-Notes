#!/bin/bash

FILEPATH="/home/xander/Downloads/Resume.pdf"

if [[ -f $FILEPATH ]]
then
    echo "File exist"
else
    echo "File not exist"
    exit 1
fi
