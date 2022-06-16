#!/bin/bash 
DATE=$(date +%F_%H-%M-%S) 
HOST=192.168.107.111 
DB=zs 
USER=root 
PASS=123456 
MAIL="zhsh0127@163.com" 
BACKUP_DIR=/data/db_backup 
SQL_FILE=${DB}_full_$DATE.sql 
BAK_FILE=${DB}_full_$DATE.zip 
cd $BACKUP_DIR 
if mysqldump -h$HOST -u$USER -p$PASS --single-transaction --routines --triggers -B $DB > $SQL_FILE; then
    zip $BAK_FILE $SQL_FILE && rm -f $SQL_FILE     
    if [ ! -s $BAK_FILE ]; then             
        echo "$DATE 备份文件不存在" | mail -s "mysql备份失败" $MAIL     
    fi
else     
    echo "$DATE 成功" | mail -s "mysql备份成功" $MAIL 
fi 
find $BACKUP_DIR -name '*.zip' -ctime +14 -exec rm {} \; 