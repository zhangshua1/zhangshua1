from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.execute_script('window.open()')
driver.switch_to_window(driver.window_handles[0])
print(driver.page_source)
input = driver.find_element_by_id('kw')
time.sleep(2)
input.send_keys('python')
input.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
response = requests.get("https://www.zhihu.com/explore",headers=headers)
# with open('dog.jpg','wb') as f:
#     f.write(response.content)
#     f.close
html=response.text
soup=BeautifulSoup(html,'lxml')
# print(soup.find_all('span'))


