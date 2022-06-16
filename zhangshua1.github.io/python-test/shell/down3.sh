#!/bin/bash
#-*-conding:utf-8-*-
TXT=/var/ftp/test
cd $TXT

[ "$#" != "1" ]&& {
        echo "input error"
        echo "(help:script+comparingfile)"
        exit 0
        }

#date=`date +%Y%m%d%H`
#mkdir $date
#chown -R ftptest:ftptest /var/ftp/test
for ip in `cat $TXT/ip_list`
do
address=`echo $ip`
if [ -e $TXT/$address.cfg ]
then
        sudo rm -rf $TXT/$address.cfg
fi
if [ -e $TXT/bt-$address ]
then
        sudo rm -rf $TXT/bt-$address
fi
if [ -e $TXT/$address.zip ]
then
        sudo rm -rf $TXT/$address.zip
fi
expect << EOF
spawn su - root
expect "*Password:"
send "zhangtao@123\r"
sleep 1
spawn ssh admin@$address
set timeout 5
sleep 5
expect "*yes/no)?"
send "yes\r"
expect "*Password:"
send "baisheng@123\r"
expect "*>"
send "ftp 192.168.10.161\r"
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
sleep 1
sudo unzip $TXT/$address.zip -d $TXT
sudo grep -aEv "cipher" $1 >$TXT/ls.txt
sudo grep -aEv "pre-shared-key" $TXT/ls.txt >$TXT/ls1.txt
sudo mv $TXT/vrpcfg.cfg $TXT/$address.cfg
done
if [ $? -eq 0 ]
then
        echo "configuration down source,file is /var/ftp/test/"
        sleep 2
        echo "...Configuration comparison..."
        while read line
        do
                sudo grep "$line" $TXT/$address.cfg >/dev/null 2>&1
                if [ $? -ne 0 ]
                then
                        echo $line >>$TXT/bt-$address
                fi
        done <$TXT/ls1.txt
        sudo rm -rf $TXT/ls.txt
        sudo rm -rf $TXT/ls1.txt
        echo "file is $TXT/bt-$address"
else
        echo "file down fail"
fi