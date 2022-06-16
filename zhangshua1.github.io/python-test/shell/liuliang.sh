eth0的网口上分析报告会输出到这些文件中：（不同的网卡目录是对对应的网卡名称）

 

/sys/class/net/eth0/statistics/rx_packets: 收到的数据包数据
/sys/class/net/eth0/statistics/tx_packets: 传输的数据包数量
/sys/class/net/eth0/statistics/rx_bytes: 接收的字节数
/sys/class/net/eth0/statistics/tx_bytes: 传输的字节数
/sys/class/net/eth0/statistics/rx_dropped: 当收到包数据包下降的数据量
/sys/class/net/eth0/statistics/tx_dropped: 传输包数据包下降的数据量
————————————————

#!/bin/bash
path='/tmp/monitor/network'
mkdir -p $path
R1=`cat /sys/class/net/eth0/statistics/rx_bytes`
T1=`cat /sys/class/net/eth0/statistics/tx_bytes`
sleep 1
R2=`cat /sys/class/net/eth0/statistics/rx_bytes`
T2=`cat /sys/class/net/eth0/statistics/tx_bytes`
TBPS=`expr $T2 - $T1`
RBPS=`expr $R2 - $R1`
TKBPS=`expr $TBPS / 1024`
RKBPS=`expr $RBPS / 1024`
echo "上传速率 eth0: $TKBPS kb/s 下载速率 eth0: $RKBPS kb/s at $(date +%Y%m%d%H:%M:%S)" >>$path/network_$(date +%Y%m%d).log