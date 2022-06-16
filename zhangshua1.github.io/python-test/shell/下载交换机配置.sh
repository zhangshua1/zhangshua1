#!/bin/bash
cd /var/ftp/test
#date=`date +%Y%m%d%H`
#mkdir $date
chown -R ftptest:ftptest /var/ftp/test
for ip in `cat /var/ftp/test/ip_list`
do
address=`echo $ip`
expect << EOF
spawn ssh admin@$address
set timeout 5
expect "*Username:"
send "admin\r"
expect "*Password:"
send "baisheng@123\r"
expect "*>"
send "ftp 192.168.10.221\r"
expect "*(none)):"
send "ftptest\r"
expect "*Password:"
send "ftptest@123\r"
expect "*ftp]"
sleep 1
send "put vrpcfg.zip /var/ftp/test/$address.zip\r"
sleep 1
expect "*ftp]"
sleep 1
send "quit\r"
sleep 1
expect "*>"
sleep 1
send "quit\r"
expect eof
EOF
done