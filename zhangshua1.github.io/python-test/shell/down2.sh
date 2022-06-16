#!/bin/bash
TXT=/var/ftp/test
cd $TXT

[ "$#" != "1" ]&& {
        echo "input error"
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
        rm -rf $TXT/$address.cfg
fi
if [ -e $TXT/bt-$address ]
then
        rm -rf $TXT/bt-$address
fi
if [ -e $TXT/$address.zip ]
then
        rm -rf $TXT/$address.zip
fi
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
sleep 1
unzip $TXT/$address.zip -d $TXT
grep -aEv "cipher" $1 >$TXT/ls.txt
grep -aEv "pre-shared-key" $TXT/ls.txt >$TXT/ls1.txt
mv $TXT/vrpcfg.cfg $TXT/$address.cfg
done
if [ $? -eq 0 ]
then
        echo "配置下载完毕！文件目录：/var/ftp/test/"
        sleep 2
        echo "...进行配置对比..."
        while read line
        do
                grep "$line" $TXT/$address.cfg >/dev/null 2>&1
                if [ $? -ne 0 ]
                then
                        echo $line >>$TXT/bt-$address
                fi
        done <$TXT/ls1.txt
        rm -rf $TXT/ls.txt
        rm -rf $TXT/ls1.txt
        echo "配置对比完成！对比文件在$TXT/bt-$address"
else
        echo "配置下载失败！"
fi