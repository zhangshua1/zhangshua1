#！/bin/bash
declare -i uphosts=0
declare -i downhosts=0

ip=(
    192.168.107.1
    192.168.107.104
    192.168.107.108
    192.168.107.109
    192.168.107.110
)

for i in ${ip[*]};do
    sudo ping -W 1 -c 1 $i &>/dev/null
    if [ $? -eq 0 ];then
        echo "$i is up."
        let uphosts+=1
    else
        echo "$i is down."
        let downhosts+=1
    fi

done
echo "up host: $uphosts,down host:$downhosts"
