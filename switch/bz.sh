#!/bin/bash
#$1是标准配置
#$2是设备的配置
[ "$#" != "2" ]&& {
        echo "input error"
        exit 0
        }
name=$2
eval "cat $1 |awk '{sub(/^[ \t]+/,"");print $0}'|sed '/^#/d'|tr -d '*' >bz"
eval "cat $2 |awk '{sub(/^[ \t]+/,"");print $0}'|sed '/^#/d'|tr -d '*' >sb"
while read line1
do
        #echo $line\*
        grep "$line1" sb >/dev/null 2>&1
        if [ $? -eq 0 ]
        then
                echo $line1 >>xt-$name
        else
                echo $line1 >>bt-$name
        fi
done<bz
rm -rf ./bz
rm -rf ./sb