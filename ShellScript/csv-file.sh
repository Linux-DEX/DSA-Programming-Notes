#!/bin/bash

while IFS="," read id name age
do
echo "Id is $id"
echo "Name is $name"
echo "age is $age"
done < sampleTwo.csv

cat sampleTwo.csv | awk 'NR!=1 {print}' | while IFS="," read id name age
do
    echo "id is $id"
done
