from cgitb import html
from email import header
import encodings
from unicodedata import name
import urllib.request
import re

def download_html(url):
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/103.0.0.0 Safari/537.36"
    }
    req=urllib.request.Request(url = url, headers=header)
    response=urllib.request.urlopen(req)
    html=response.read().decode("utf-8")
    return html
for i in range(1,7):
    #url='https://javdb.com/actors/kzx6?page={}'.format(i)
    url='https://javdb.com/actors/0dKX?page={}'.format(i)
    html=download_html(url)
    name=re.findall(r'<a href="(.*?)" class="box" title="(.*?)">',html)
    # wz=re.findall(r'<a href="(.*?)" class="box"',html)
    for j in list(name):
        wz_zh='https://javdb.com{}'.format(j[0])
        j_zh=list(j)
        j_zh[0]=wz_zh
        #print(wz_zh)
        # html_1=download_html(wz_zh)
        # dz=re.findall(r'data-clipboard-text="(.*?)" type',html_1)
        # dz_zh=list(dz)
        # print(dz_zh)
        with open('桃乃木香奈.txt','a+',encoding='utf8') as f:
            f.write(str(j_zh) + "\n")

