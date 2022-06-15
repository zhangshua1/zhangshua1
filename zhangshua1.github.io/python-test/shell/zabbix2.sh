#!/bin/bash
YUM="/etc/yum.repos.d/zabbix.repo"
ZABBIX="/etc/zabbix/zabbix_server.conf"
check_system(){
    if [ -e /etc/redhat-release ];then
        sys=`cat /etc/redhat-release |awk '{print $1}' >/dev/null 2>&1`
        if [ $? -eq 0 ];then
            if [ $sys==CentOS ];then
                echo "系统为Centos,可以继续......"
                exit 0
            else
                echo "系统不是centos,安装中断。"
                exit 1
            fi
        else
            echo "这什么鬼系统...."
        fi
    else
        echo "系统不支持！"
        exit 1
    fi
}
check_yum(){
    if [ -e $YUM ];then
        echo "zabbix源已有！"
    else
        rpm -Uvh https://mirrors.aliyun.com/zabbix/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm >/dev/null 2>&1
        sed -i 's#http://repo.zabbix.com#https://mirrors.aliyun.com/zabbix#' $YUM
        wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
        yum makecache >/dev/null 2>&1
        yum install centos-release-scl net-tools lrzsz -y >/dev/null 2>&1
        yum clean all >/dev/null 2>&1
        sed -i 's#enabled=0#enabled=1#g' $YUM
        echo "yum源配置结束。"
    fi
}
check_path(){
    if getenforce 0 >/dev/null 2>&1;then
        sed -i 's#SELINUX=enabled#SELINUX=disabled#g' /etc/selinux/config
    fi
    systemctl stop firewalld >/dev/null 2>&1
    systemctl disable firewalld >/dev/null 2>&1
}
install_et_sql(){
    yum -y install mariadb-server mariadb-devel >/dev/null 2>&1
    if [ $? -eq 0 ];then
        systemctl start mariadb
        systemctl enable mariadb
    else
        echo "数据库安装失败..."
        exit 1
    fi
    sq=`netstat -lntup | grep mysql|awk '{print $4}'|awk -F: '{print $2}'`
    if [ $sq -eq 3306 ];then
        `mysqladmin -u root password`
        mysql -uroot -p123456 -e 'create database zabbix character set utf8 collate utf8_bin;'
        mysql -uroot -p123456 -e "grant all privileges on zabbix.* to zabbix@localhost identified by '123456'"
        mysql -uroot -p123456 -e 'flush privileges;'
        echo "mariadb数据库安装完成...."
        exit 0
    else
        echo "数据库启动失败，请检查..."
        exit 1
    fi

}
install_zabbix(){
    yum install zabbix-web-mysql-scl zabbix-apache-conf-scl -y >/dev/null 2>&1
    if [ $? -eq 0 ];then
        echo "安装zabbix前端...."
        yum install zabbix-get zabbix-sender zabbix-server-mysql zabbix-web zabbix-agent -y >/dev/null 2>&1
        if [ $? -eq 0 ];then
            echo "安装zabbix主服务....."
            cat /etc/zabbix/zabbix_server.conf |sed -i 's/# DBPassword=/DBPassword=123456/g' /etc/zabbix/zabbix_server.conf
            sed -i 's@# DBSocket=@DBSocket=/var/lib/mysql/mysql.sock@g' /etc/zabbix/zabbix_server.conf
            gunzip /usr/share/doc/zabbix-server-mysql-5.0.2/create.sql.gz
            mysql -u zabbix -p123456 zabbix</usr/share/doc/zabbix-server-mysql-5.0.2/create.sql
            sed -i 's#; ##g' /etc/opt/rh/rh-php72/php-fpm.d/zabbix.conf
            sed -i 's#Europe/Riga#Asia/Shanghai#g' /etc/opt/rh/rh-php72/php-fpm.d/zabbix.conf
            systemctl restart zabbix-server zabbix-agent httpd rh-php72-php-fpm
            systemctl enable zabbix-server zabbix-agent httpd rh-php72-php-fpm >/dev/null 2>&1
        else
            echo "zabbix安装失败...."
            exit 1
        fi
        else
            echo "依赖安装失败...."
            exit 1
    fi
    if [ $? -eq 0 ];then
        echo "zabbix安装启动完成..."
    else
        echo "zabbix启动失败...."
        exit 1
    fi
}

cat << EOF
0)检查系统
1)检查YUM源
2)检查环境
3)安装mysql
4)安装zabbix
EOF

if [[ -n $1 ]]; then
     input=$1
     echo "执行操作:$1"
else
     read -p "请选择：" input
fi

case $input in
     0) check_system;;
     1) check_yum;;
     2) check_path;;
     3) install_et_sql;;
     4) install_zabbix;;
esac