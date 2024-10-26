#!/bin/bash
myArray=(1 2 203.3333 hello "shell script")

echo "Value of 3rd index ${myArray[3]}"

echo "All the values in array are ${myArray[*]}"

echo "length of array is ${#myArray[*]}"

echo "${myArray[*]:1}"

echo "value  from index 2-3 ${myArray[*]:2:2}"

myArray+=( new 45 99)
echo "Value of new array is ${myArray[*]}"
