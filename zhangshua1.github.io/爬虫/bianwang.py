# -*- coding:utf8 -*-
 
import re
import time
import json
import redis
import pymongo
import hashlib
import datetime
import requests
from lxml import etree
 
 
class BiAnWang(object):
 
    def __init__(self):
        self.StartUrl = "http://pic.netbian.com/"
        self.Header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
        }
 
    def RunMain(self):
        response = requests.get(url = self.StartUrl, headers = self.Header).content.decode("gbk")
        html = etree.HTML(response)
        MaxPage = html.xpath('//div[@class="wrap clearfix"]/div/div[4]/a[10]/text()')[0]
        # print(MaxPage)
        self.GetPage(MaxPage)
 
    def GetPage(self,MaxPage):
        for i in range(1,int(MaxPage)):
            if i == 1:
                Url = self.StartUrl + "index.html"
            else:
                Url = self.StartUrl + "index_%s.html"%i
 
            self.JpgUrl(Url)
 
    def JpgUrl(self,Url):
        response = requests.get(url = Url, headers = self.Header).content.decode("gbk")
        html = etree.HTML(response)
        JpgLink = html.xpath('//div[@class="wrap clearfix"]/div/div[3]/ul/li/a/@href')
        for url in JpgLink:
            JpgLinks = "http://pic.netbian.com" + url
            self.JpgInfo(JpgLinks)
 
    def JpgInfo(self,JpgLinks):
        #print(JpgLinks)
        try:
            response = requests.get(url = JpgLinks, headers = self.Header).content.decode("gbk")
            html = etree.HTML(response)
            JpgName = html.xpath('//div[@class="wrap clearfix"]/div/div[2]/div/div[1]/h1/text()')[0]
            JpgUrl = html.xpath('//div[@class="wrap clearfix"]/div/div[2]/div/div[2]/a/img/@src')[0]
            JpgUrls = "http://pic.netbian.com" + str(JpgUrl)
            self.download(JpgName,JpgUrls)
        except IndexError:
            pass
        
    def download(self,JpgName,JpgUrls):
        session = requests.session()
        #a为文件扩展名.jpg
        a = JpgUrls[-4:]
        response = session.get(JpgUrls, headers=self.Header).content
        with open("netbian/%s" % JpgName + a, "wb") as f:
            f.write(response)
            print("图片下载成功")
        time.sleep(1)

if __name__ == "__main__": 
   bian= BiAnWang()
   bian.RunMain()