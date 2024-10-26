#!/bin/bash

declare -A myArray
myArray=( [name]=Linux-DEX [age]=22 [city]=bangalore )

echo "Name is ${myArray[name]}"
echo "Age is ${myArray[age]}"
