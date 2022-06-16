#!/bin/bash

sql_bck=/home/sql_bck
if [ ! -d $sql_bck ]
then
    mkdir -p $sql_bck
fi

cptime=`date -d "-2 days" +%F`

/usr/bin/expect  << EOF
set timeout 10
spawn scp root@*.*.*.*:/mysql_weekly_bck/${cptime}_weekly_sql.tar.gz $sql_bck
expect "*passphrase*" {send "******\r"}
expect eof
EOF
