#!/bin/bash

read -p "Enter your marks: " marks

if [[ $marks -gt 80 ]]; then
    echo "1st division"
elif [[ $marks -ge 60 ]]; then
    echo "2nd division"
elif [[ $marks -ge 40 ]]; then
    echo "3rd division"
else
    echo "You are FAIL....."
fi
