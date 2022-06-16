#!/bin/bash
# [ -e "xt" ]&&{
#          rm -rf xt
# }
#declare -A array1
rpm -qa|grep sshpass >/dev/null
[ $? -ne 0 ]&&{
        yum install -y sshpass >/dev/null
}

[ "$#" != "1" ]&& {
        echo "input error"
        exit 0
        }
#sort -u $1 > uniq2
#sort -u $2 > uniq2
ip=(
    192.168.90.158
    192.168.100.22
)
/usr/bin/Expect
set timeout 10
set host "192.168.90.158"
set username "admin"
set password "baisheng@123"
spawn ssh $username@$host dis cu
expect "*Password*" {send "$password\r"}
interact

`echo "IP,not the same">bt.csv`
`echo "not connect IP">nip.csv`
for i in ${ip[*]}
do
        `ping -W 1 -c 2 $i >/dev/null`
        if [ $? -eq 0 ]
        then
                na=`echo $i|awk '{print $3$4}'`
                #sshpass -pbaisheng@123 ssh admin@$i 'dis cu' >>$na'.txt'
                ssh >>$na'.txt'
                while read line1
                do
                        while read line2
                        do
                                if [ "$line1"="$line2" ]
                                then
                                        echo "$i,'same:',$line1" >>bt.csv
                                else
                                        echo "$i,'not the same:',$line1" >>bt.csv
                                fi
                        done <$na'.txt'
                done <$1
        else
                echo "$i" >>noip.csv
        fi
done




# while read line
# do
#         #pas=`echo $line|awk '{print $NF}'`
#         ipa=`echo $line|awk '{print $1}'`
#         na=`echo $line|awk '{print $1}'|awk -F. '{print $3$4}'`
#         #echo $pas
#         #echo $ipa
#         #echo $na
#         sshpass -pbaisheng@123 ssh admin@$ipa 'dis cu' >$na'.txt'
#         cat $na'.txt'|grep -vE "^$" >$na'.csv'
#         #echo `cat as.txt`
#         while read line1
#         do
#                 while read line2
#                 do
#                         if [ "$line1" = "$line2" ]
#                         then
#                                 echo $line1 >>xt
#                         fi
#                 done<$1
#         done<$na'.csv'
#         Except=`sed 's# #|#g' xt`
#         #grep -vE "$Except" $na'.txt' >bt1.txt
#         butong=`grep -vE "$Except" $1`
#         echo $ipa,$butong >>bt.csv
# done<ip.txt
#Except=`sed 's# #|#g' xt`
#grep -vE "$Except" $na'.txt' > bt1.txt
#grep -vE "$Except" $1 >bt