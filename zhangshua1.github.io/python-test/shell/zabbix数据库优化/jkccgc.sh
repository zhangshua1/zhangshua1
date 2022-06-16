#!/bin/bash
mkdir -p /usr/local/msmtp/etc
cat > /root/.msmtprc << EOF
host mail.xxxx.com
tls off
auth plain
from zabbix@xxxx.com
user zabbix
password xxxxxx

EOF


cat > /root/.muttrc << EOF
set sendmail="/usr/local/msmtp/bin/msmtp"
set use_from=yes
set from=zabbix@xxxx.com
set envelope_from=yes

EOF

cat >  /usr/local/msmtp/etc/msmtprc  << EOF
defaults 
account zabbix
host mail.xxx.com
from zabbix@xxx.com       
auth login
port 25
tls off
user zabbix@xxx.com 
password  xxxxx
account default : zabbix
logfile /usr/local/msmtp/log/msmtp.log

EOF

mkdir -p /usr/local/msmtp/log
echo 'set sendmail="/usr/local/msmtp/bin/msmtp"' >>/etc/Muttrc
echo "set use_from=yes" >>/etc/Muttrc
echo 'set realname="zabbix@xxxx.com"' >>/etc/Muttrc
echo 'set editor="vim"' >>/etc/Muttrc


tar jxvf msmtp-1.4.30.tar.bz2
cd msmtp-1.4.30
./configure --prefix=/usr/local/msmtp
make
sleep 3 
make install
sleep 3
cd ..
tar zxvf mutt-1.5.21.tar.gz 
cd mutt-1.5.21
./configure --prefix=/usr/local/mutt
make
sleep 3
make install
sleep 3
cd ..
ln -s /usr/local/msmtp/bin/msmtp /usr/bin

echo  测试  | /usr/local/mutt/bin/mutt  -s  "测试"  xxx@xxxxx.com