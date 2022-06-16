#!/bin/bash
declare -i sum
read -p "please inp"

for (( i=0; i<$1; i++ ))
do
    sum=sum+i
done
echo $sum
