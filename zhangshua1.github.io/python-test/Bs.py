import re
import requests
import os
from bs4 import BeautifulSoup

LOGIN_URL = 'http://yingxiao.chewumi.com/login.php'
DATA = {"username":'accountID',"passwd":'passwd'}
HEADERS = { 
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' #模拟登陆的浏览器  
           }
RES = requests.post(LOGIN_URL,data=DATA,headers=HEADERS)  #模拟登陆操作
print (RES.text)

loginAccount: "zhongruan"
credential: "Admin_1234"
captchaCredential: ""
isAgreePrivacyStatement: false