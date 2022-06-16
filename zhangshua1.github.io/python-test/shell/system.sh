#!/bin/bash 
# 提取性能监控指标（磁盘占用、CPU使用、内存使用） 
DUG=$(df -h | grep "/$" | awk '{print $5}' | awk -F% '{print $1}') 
# yum install sysstat -y
CUG=$(expr 100 - $(mpstat | tail -1 | awk '{print $12}' | awk -F. '{print $1}')) 
MUG=$(expr $(free | grep "Mem:" | awk '{print $3}') \* 100 / $(free | grep "Mem:" | awk '{print $2}'))
# 设置告警日志文件、告警邮箱 
ALOG="/tmp/alert.txt" 
AMAIL="zhsh0127@163.com" 
# 判断是否记录告警 
if [ $DUG -gt 90 ] 
then
    echo "磁盘占用率：$DUG %" >> $ALOG 
fi 
if [ $CUG -gt 80 ] 
then
    echo "CPU使用率：$CUG %" >> $ALOG 
fi 
if [ $MUG -gt 90 ] 
then 
    echo "内存使用率：$MUG %" >> $ALOG fi 
# 判断是否发送告警邮件，最后删除告警日志文件 
if [ -f $ALOG ] 
then
    cat $ALOG | mail -s "Host Alert" $AMAIL
    rm -rf $ALOG 
fi 

