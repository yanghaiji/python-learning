#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: demo02.py
@date: 2022/9/1 
"""

# 获取chrome 驱动
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 访问地址
driver.get("http://www.baidu.com")
# 元素的定位
ele = driver.find_element(By.XPATH, '//*[@id="kw"]')
ele.send_keys("python")
# 点击搜索
driver.find_element(By.XPATH, '//*[@id="su"]').click()

# 元素的定位
ele = driver.find_element(By.XPATH, '//*[@id="kw"]')
ele.send_keys("python22222")
# 点击搜索
driver.find_element(By.XPATH, '//*[@id="su"]').click()

# 后退
driver.back()