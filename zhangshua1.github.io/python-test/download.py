from lib2to3.pgen2 import driver
from selenium import webdriver

opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)
driver.get('https://javdb.com/v/k4DAe')

