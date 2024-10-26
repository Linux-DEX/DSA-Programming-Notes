#!/bin/bash

set -x

if [[ $# -eq 0 ]]
then
    echo "please provide atleast one argument"
    exit 1
fi

echo "first args -- $1"
echo "second args -- $2"
