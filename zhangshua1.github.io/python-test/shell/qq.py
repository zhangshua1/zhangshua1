import requests
import sys
import os
import json
import logging
# set log
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s,%(filename)s,%(levelname)s,%(message)s',datefmt = '%a, %d %b %Y %H:%M:%S',filename=os.path.join('/usr/lib/zabbix/alertscripts','weixin.log'),filemode='a')
# corpID
corpid='ww83c95b4c3aa5a9b4'
# appSecret
appsecret='Jb-8PKVLVoBa-y_hGz1deDX6_0GyqBBixPBaBM9MhW8'
# appAgentId
agentid=1000002
#fetchAccesstoken
token_url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + appsecret
req=requests.get(token_url)
accesstoken=req.json()['access_token']
#sendData
msgsend_url='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + accesstoken
touser=sys.argv[1]
subject=sys.argv[2]
#toparty='groupID'
message=sys.argv[3]
params={
    "toparty": touser,
    "msgtype": "text",
    "agentid": agentid,
    "text": {"content": message},
    "safe":0
}
req=requests.post(msgsend_url, data=json.dumps(params).encode('utf-8'))
logging.info('sendto:' + touser + ';;subject:' + subject + ';;message:' + message)