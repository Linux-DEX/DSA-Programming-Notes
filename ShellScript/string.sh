#!/bin/bash

myVar="Hey Linux-DEX, How are you?"

myVarLength=${#myVar}
echo "Length of the myVar is $myVarLength"

echo "Upper case is -------- ${myVar^^}"

echo "Lower case is ---------- ${myVar,,}"

newVar=${myVar/Linux-DEX/Buddy}
echo "New string is --- ${newVar}"

echo "after slice --- ${myVar:0:3}"
