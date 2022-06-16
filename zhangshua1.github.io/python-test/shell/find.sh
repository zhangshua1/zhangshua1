#！/bin/bash
for i in `find / -type f`
do
    grep 'zabbix.php' $i
done