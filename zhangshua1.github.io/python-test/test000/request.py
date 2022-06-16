import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录后才能访问的网页
url = 'http://192.168.10.221/zabbix.php?action=proxy.list'

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'PHPSESSID=pfpufnoadkcheb8ufb4aup8a39; zbx_sessionid=abedac4363fb5e38eeee91895ab375c5'

#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

#在发送get请求时带上请求头和cookies
resp = requests.get(url, headers = headers, cookies = cookies)

print(resp.content.decode('utf-8'))

#print(resp.content)