#!/bin/bash
id=$(snmpwalk -v 2c -c Admin@123  10.200.250.5 1.3.6.1.4.1.2011.6.139.13.   3.10.1.5 | cut -f1 -d "=" | cut -f10 -d ".")
id_array=(${id})
sum=$(snmpwalk -v 2c -c Admin@123  10.200.250.5 1.3.6.1.4.1.2011.6.139.13.3.10.1.5 | wc -l) 
name=$(snmpwalk -v 2c -c Admin@123  10.200.250.5 enterprises.2011.6.139.13.3.10.1.5 | awk  '{print $4}' | sed 's/"//g')
name_array=($name)
printf '{\"data\":[ '
for ((i=0;i<$sum;i++))
do 
    printf "{\"{#APID}\":\"${id_array[$i]}\",\"{#APNAME}\":\"${name_array[$i]}\" }"
      
    if [ $i -lt $[ $sum-1 ] ];then
printf ','
fi
done
printf " ]}"
