#!/bin/bash

FILE="/media/xander/Backup/Notes/ShellScript/sample.txt"

for name in $(cat $FILE)
do
    echo "Name is $name"
done
