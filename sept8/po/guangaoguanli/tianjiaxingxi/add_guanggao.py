import time
import os
# from libs.Base_work import admin_login
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get(url)
# 点击广告管理
driver.find_element_by_id('username').click()