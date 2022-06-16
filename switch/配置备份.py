# coding: UTF-8
# UYUN Automation script
# @Author: zhengyd@uyunsoft.cn
# @Date  : 2019/6/28
# 备份网络设备的配置文件

import os
import re
import sys
import time
import json
import chardet
import requests
from concurrent import futures
import _utils.Network as Network

reload(sys)
sys.setdefaultencoding('utf-8')

HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}


def convert_bytes(bytes, unit=None, multiple=1024):
    symbols = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    bytes = float(bytes)
    step = 0
    if not unit:
        while bytes >= multiple and step < len(symbols) - 1:
            bytes /= multiple
            step += 1
        unit = symbols[step]
    else:  # convert to specific unit
        index_of_unit = symbols.index(unit)
        while len(symbols) - 1 > step and index_of_unit != step:
            bytes /= multiple
            step += 1
    return '{:.2f} {}'.format(bytes, unit)


def save_to_file(save_dir, file_name, content):
    """保存到文件"""
    try:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        conf_path = os.path.abspath(os.path.join(save_dir, file_name))
        with open(conf_path, 'w') as cf:
            cf.write(content)
        return conf_path
    except Exception as e:
        print('Error, Save to file failed：{}'.format(e))


def save_to_network(host_ip, file_name, content):
    """保存到 Network 接口"""
    try:
        url = BASE_URL.rstrip('/') + '/network/v2/openapi/datasets/configbackup/create?apikey={}'.format(API_KEY)
        data = {'hostIp': host_ip,
                'fileName': file_name,
                'fileContent': content
                }
        resp = requests.post(url, data=json.dumps(data), headers=HEADERS)
        #print resp.text
        resp.raise_for_status()
        print('{}: Save to Network succeed'.format(host_ip))
        return True
    except Exception as e:
        print('{}: Save to  Network failed'.format(host_ip))
        print(e)


def backup_conf(host, user, passwd, ssh_port, enable_passwd=None, save_to='all', **kwargs):
    """备份网络设备的配置"""
    global all_conf_size
    try:
        client = Network.connect(host, user, passwd)
        if not client:  # 连接失败退出
            return
        if client.device_type in ['cisco']:
            conf_name = 'startup'
            code, out = client.run('show running-config', wait=2)
            if code:
                if not enable_passwd:
                    print("Error, {}: need enable password".format(host))
                    return
                print("{} enter enable".format(host))
                if not client.enter_enable(enable_passwd, 3):
                    return
                code, out = client.run('show running-config', wait=2)
                conf_name = 'running'
        elif client.device_type in ['ruijie']:
            code, out = client.run('show running-config')
            conf_name = 'running'
            if code:
                if not enable_passwd:
                    print("Error, {}: need enable password".format(host))
                    return
                if not client.enter_enable(enable_passwd):
                    return
                code, out = client.run('show running-config', wait=2)
        elif client.device_type in ['h3c', 'huawei']:
            conf_name = 'current'
            code, out = client.run('display current-configuration', wait=2)
            if code:
                if client.run('system-view')[0]:
                    print('Error, {}: enter enable failed'.format(host))
                    return False
                code, out = client.run('display current-configuration', wait=2)
        else:
            print('Error, {}: Not support device type:{}'.format(host, client.device_type))
            return
        client.close()

        if not code:
            filename = '{}_{}_{}_{}.txt'.format(host, client.device_type, conf_name, time.strftime('%Y%m%d%H%M%S'))
            out = '\r\n'.join(out)
            print('{}: Get config succeed, {} bytes'.format(host, len(out)))
            all_conf_size += len(out)
            
            try:
                coding = 'ISO-8859-1'
                out = out.decode(coding).encode('utf8')
            except:
                print '{}: decode error, {}'.format(host, chardet.detect(out))
                try:
                    coding = chardet.detect(out).get('encoding') or 'gbk'
                    out = out.decode(coding).encode('utf8')
                except:
                    pass

            file_path = None
            if save_to == 'network':    # 保存到Network接口
                save_state = save_to_network(host, filename, out)
            elif save_to == 'local':    # 保存到本地文件
                save_state = file_path = save_to_file(save_path, filename, out)
            else:                       # 默认同时保存到Network和本地
                save_state = save_to_network(host, filename, out)
                file_path = save_to_file(save_path, filename, out)

            if save_state:
                SUCCESS_HOSTS.append(host)
            if file_path:
                backup_paths.append(file_path)
                print('{}: Save to file succeed, {}'.format(host, file_path))

            return save_state
        else:
            print("Error, {}: cmd error".format(host))
    except Exception as err:
        print('{}: Backup error: {}'.format(host, err))


if __name__ == '__main__':
	
    save_path = '/tmp/network_device_backup'
    start_time = time.time()
    SUCCESS_HOSTS = []
    all_conf_size = 0
    backup_paths = []
    save_to = save_to.strip().lower()

    if save_to != 'local':
        BASE_URL = os.getenv('ANT_BASEURL')
        API_KEY = apikey
        if not BASE_URL:
            print 'BASE_URL get failed, exits.'
            sys.exit(1)
        if not API_KEY.strip() or not BASE_URL:
            print 'Save to the network by specifying the API_KEY as necessary, exit.'
            sys.exit(1)

    # IP 去重
    ips = set([i.strip() for i in re.split(r'\s|,|;', ips) if i.strip()])

    # 多线程执行
    with futures.ThreadPoolExecutor(max_workers=15) as executor:
        for ip in ips:
            executor.submit(backup_conf, ip, username, password, int(ssh_port), save_to,debug=False)

    failed_hosts = ' '.join(ips - set(SUCCESS_HOSTS))
    if failed_hosts:
        ExitCode = 1
        print('\nFailed hosts: {}'.format(failed_hosts))
    print("All backup config size: {}".format(convert_bytes(all_conf_size)))
    print('\nDone, Total host: {}, Succeed host: {}, '
          'Failed host: {}, Total time: {:.2f}s\n'.format(len(ips),
                                                          len(SUCCESS_HOSTS),
                                                          len(ips) - len(SUCCESS_HOSTS),
                                                          time.time() - start_time))
    backup_paths = ','.join(backup_paths)
    print backup_paths
