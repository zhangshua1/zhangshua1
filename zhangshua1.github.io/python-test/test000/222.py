from selenium import webdriver
import requests
import time

# def main():
#     b = webdriver.Chrome()
#     b.get('http://www.baidu.com')
#     time.sleep(5)
#     b.quit()

def req():
    a = webdriver.Chrome()
    c = a.get('http://www.baidu.com')
    d = requests.URLRequired(c)
    print(d)

if __name__ == '__main__':
    # main()
    req()