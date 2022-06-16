import json
import random
import re

import redis
import requests

TEL_PATTERN = re.compile(r'1[3-9]\d{9}')


def send_messag(tel, code):
    resp = requests.post(
        url='http://sms-api.luosimao.com/v1/send.json',
        auth=('api', 'key-'),
        data={
            'mobile': tel,
            'message': f'您的短信验证码是{code}，打死也不能告诉别人哦！【铁壳测试】'
        },
        timeout=3,
        verify=False
    )
    return json.loads(resp.text)


def main():
    tel = input('请输入手机号: ')
    if TEL_PATTERN.fullmatch(tel):
        client = redis.Redis(host='120.77.222.217',
                             port=6379,
                             password='1qaz2wsx')
        if client.exists(tel):
            print('请不要在120秒内重复发送短信验证码!!!')
        else:
            code = ''.join(random.choices('0123456789', k=6))
            result = send_messag(tel, code)
            print(result['error'])
            if result['error'] == 0:
                client.set(tel, code, ex=120)
                print('发送成功!!!')
    else:
        print('请输入有效的手机号码!!!')


if __name__ == '__main__':
    main()
