#!/bin/bash

if [[ $UID -eq 0 ]]
then 
    echo "user is root"
else
    echo "user is not root"
fi

echo "The name of the script is: ${0}"
