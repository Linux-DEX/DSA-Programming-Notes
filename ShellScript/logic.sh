#!/bin/bash

read -p "what is your age?" age
read -p "your country:" country

if [[ $age -ge 18 ]] && [[ $country == "India" ]]
then
    echo "you can vote"
else 
    echo "you can't vote"
fi

#!/bin/bash

read -p "what is your age?" age
read -p "your country:" country

if [[ $age -ge 18 ]] || [[ $country == "India" ]]
then
    echo "you can vote"
else 
    echo "you can't vote"
fi

age=18
[[ $age -ge 18 ]] && echo "adult" || echo "Minor"
