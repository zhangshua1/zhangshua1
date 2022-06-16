#!/bin/bash
#远程批量执行命令
if [ $# -ne 1 ]
   then
   echo "USAGE:sh $0 command"
   exit 1
fi
for n in 113 115 116
do
  ssh -p22 root@192.168.107.$n $1
done
EOF
