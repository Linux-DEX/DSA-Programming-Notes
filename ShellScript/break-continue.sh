#!/bin/bash

no=6

for i in 1 2 3 4 5 6 7 8 9
do
    if [[ $no -eq $i ]]
    then 
        echo "$no is found!!!!"
        break
    fi
    echo "number is $i"
done

for i in 1 2 3 4 5 6 7 8 9 10
do
    let r=$i%2
    if [[ $r -eq 0 ]]
    then
        continue
    fi
    echo "odd no. is $i"
done

if [[ $# -eq 0 ]]
then
    exit 1
fi

echo "first args is $1"
echo "second args is $2"

read -p "which site you want to check? " site
ping -c l $site
sleep 5s

if [[ $? -eq 0 ]]
then
    echo "successfull connection to $site"
else 
    echo "unable to connect $site"
fi
