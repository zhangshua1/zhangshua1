#!/bin/bash
    
for ip in {1..100}
do
    echo "==================== host 172.16.1.$ip pub-key start fenfa ==================== "
    sshpass -p123456 ssh-copy-id -i /root/.ssh/id_dsa.pub root@172.16.1.$ip "-o StrictHostKeyChecking=no" &>/dev/null
    echo -e "host 172.16.1.$ip fenfa success."
    echo "==================== host 172.16.1.$ip fenfa end ==================== "
    echo ""
done 