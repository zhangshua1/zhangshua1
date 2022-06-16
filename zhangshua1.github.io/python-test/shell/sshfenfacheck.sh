#分发公钥检查脚本(批量管理脚本)  --- 串型批量管理
#[root@m01 scripts]# cat check_pub_key.sh 
#!/bin/bash
CMD=$1
for ip in {7,31,41}
do
    echo "==================== host 172.16.1.$ip check ==================== "
    ssh 172.16.1.$ip $CMD 
    echo ""
done 