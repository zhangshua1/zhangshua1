import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录时需要POST的数据
data = {'j_username':'018644',         
'j_password':'Zs123456',         
'goto:https':'//edesk.shlongtian.com:18080/jsp/Logout.jsp',         
'gotoOnFail:https':'//edesk.shlongtian.com:18080/jsp/Logout.jsp'}
#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
#登录时表单提交到的地址（用开发者工具可以看到）
login_url = 'https://edesk.shlongtian.com:18080/jsp/Logout.jsp'
#构造Session
session = requests.Session()
#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url, data)
#登录后才能访问的网页
url = 'http://ssfw.xmu.edu.cn/cmstar/index.portal'
#发送访问请求
resp = session.get(url)

print(resp.content.decode('utf-8'))

while true:
    