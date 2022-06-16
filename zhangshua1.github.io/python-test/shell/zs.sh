#!/bin/bash
#[ "$#" != "1" ]&& {
#       echo "input error"
#       exit 0
#}
`rpm -qa|grep sshpass >/dev/null`
[ $? -ne 0 ]&&{
        yum install -y sshpass >/dev/null
}
ip=(
        192.168.107.113
)
echo "not the same,IP">bt.csv
#declare -A j=0
for i in ${ip[*]}
do
        sshpass -p193256 ssh root@$ip 'cat sb.txt' >"$i".txt
        echo " ,$i">>bt.csv
        #while read line1
        #do
        #       cat dd.txt|grep $line1 >>xt.csv
        #done<"$ip".txt
        #let j++
#       cat "$ip".txt
#       grep "while read line `cat dd.txt`;do echo $line;done" "$ip".txt >>xt.csv
        cat "$i".txt bz.txt | sort | uniq -d >>xt.csv
        cat bz.txt xt.csv | sort | uniq -u >>bt.csv
done
#echo $j
#grep -vE "$xt.csv" dd.txt >bt.csv