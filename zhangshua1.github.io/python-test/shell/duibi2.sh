#!/bin/bash

# [ -e "xt" ]&&{
#          rm -rf xt
# }
#declare -A array1
# rpm -qa|grep sshpass >/dev/null
# [ $? -ne 0 ]&&{
#         yum install -y sshpass >/dev/null
# }

[ "$#" != "2" ]&& {
        echo "input error"
        exit 0
        }
#sort -u $1 > uniq2
#sort -u $2 > uniq2
        #pas=`echo $line|awk '{print $NF}'`
        #ipa=`echo $line|awk '{print $1}'`
        #na=`echo $line|awk '{print $1}'|awk -F. '{print $3$4}'`
        #echo $pas
        #echo $ipa
        #echo $na
        #sshpass -p baisheng@123 ssh $ipa 'dis cu' >$na'.txt'
        #echo `cat as.txt`
        while read line1
        do
                if [ grep "$line1" $2 ]
                then
                echo "$line1" >>xt.csv
                else
                echo "$line1" >>bt.csv
                fi
        done<$1
        # Except=`sed 's# #|#g' xt`
        # grep -vE "$Except" $na'.txt' >bt1.txt
        # grep -vE "$Except" $1 >bt2.txt
#Except=`sed 's# #|#g' xt`
#grep -vE "$Except" $na'.txt' > bt1.txt
#grep -vE "$Except" $1 >bt