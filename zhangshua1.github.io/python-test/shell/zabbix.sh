#!/bin/bash
#禁掉selinux和firewall
getenforce 0 >/dev/null 2>&1
sed -i 's#SELINUX=enabled#SELINUX=disabled#g' /etc/selinux/config
systemctl stop firewalld >/dev/null 2>&1
systemctl disable firewalld >/dev/null 2>&1

if [ -e /etc/yum.repos.d/zabbix.repo ];then
    echo "zabbix源已有！"
else
    rpm -Uvh https://mirrors.aliyun.com/zabbix/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm >/dev/null 2>&1
    sed -i 's#http://repo.zabbix.com#https://mirrors.aliyun.com/zabbix#' /etc/yum.repos.d/zabbix.repo
    yum clean all >/dev/null 2>&1
    sed -i 's#enabled=0#enabled=1#g' /etc/yum.repos.d/zabbix.repo
    echo "zabbix源配置结束。"

echo "安装zabbix前端环境"
yum install zabbix-web-mysql-scl zabbix-apache-conf-scl -y >/dev/null 2>&1

#安装数据库
if [ $? -eq 0 ];then
    yum -y install mariadb-server mariadb-devel >/dev/null 2>&1
else
    "zabbix前端环境安装失败！"
    break
    

