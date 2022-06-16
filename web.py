#打开3个窗口，通过switch_to_window切换关闭窗口
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com/")
# print (driver.window_handles)
# driver.switch_to_window(driver.window_handles[1])
# driver.close()

# #打开百度首页，输入搜索内容并进行光标移动后回车
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com/")
# element=driver.find_element_by_id('kw')
# element.clear()
# element.send_keys('woqu'.decode('gbk'))
# element.send_keys(Keys.ARROW_DOWN) #光标向下
# element.send_keys(Keys.ENTER) #回车

## 引入WebDriver包
from selenium import webdriver

## 引入WebDriver Keys包
from selenium.webdriver.common.keys import Keys

## 创建浏览器对象
browser = webdriver.Firefox()

## 导航到百度主页
browser.get('https://www.baidu.com')

## 检查标题是否为‘百度一下，你就知道’
assert '百度一下，你就知道' in browser.title

## 找到名字为wd的元素，赋值给elem
elem = browser.find_element_by_name('wd')  # 找到搜索框
elem.send_keys('seleniumhq' + Keys.RETURN)  # 搜索seleniumhq

## 关闭浏览器
browser.quit()