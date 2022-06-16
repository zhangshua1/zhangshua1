#!/bin/bash
#Author:zhangshuai
#time:2020-10-19

for (( i=0; i<9; i++ ))
do
    for ((j=0; j<i; j++))
    do
        printf(i"*"j="i*j" ;print" ")
    done
done