#!/bin/bash
function echo_color() {
        if [ $1 == "green" ]; 
        then         
                echo -e "\033[30;40m$2\033[0m"     
        elif [ $1 == "red" ]; 
        then         
                echo -e "\033[31;40m$2\033[0m"
        elif [ $1 == "yell" ];
        then
                echo -e "\033[33;40m$2\033[0m"
        elif [ $1 == "blue" ];
        then
                echo -e "\033[34;47m$2\033[5m"
        elif [ $1 == "purple" ];
        then
                echo -e "\033[35;40m$2\033[0m"
        elif [ $1 == "sgreen" ]
        then
                echo -e "\033[36;40m$2\033[0m"
        elif [ $1 == "write" ];
        then
                echo -e "\033[37;40m$2\033[0m"
fi 
}
echo_color blue "nidaye"
