#!/bin/bash
declare -i uphosts=0
declare -i downhosts=0
declare -i i=100
hostping(){
    if sudo ping -W 1 -c 1 $1 &>/dev/null;then
        echo_color green "$1 is up."
        return 0
    else
        echo_color red "$1 is down."
        return 1
    fi
}
function echo_color() {
        if [ $1 == "green" ]; 
        then         
                echo -e "\033[32;40m$2\033[0m"     
        elif [ $1 == "red" ]; 
        then         
                echo -e "\033[31;40m$2\033[0m"
        fi
}
while [ $i -le 120 ];do
    hostping 192.168.107.$i 
    [ $? -eq 0 ] && let uphosts++ || let downhosts++
    let i++
done

echo "up hosts:$uphosts,down hosts:$downhosts"
