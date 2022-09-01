from selenium import webdriver
from selenium.webdriver.common.by import By

# 获取chrome 驱动
driver = webdriver.Chrome()
# 访问地址
driver.get("http://www.baidu.com")
# 元素的定位
ele = driver.find_element(By.XPATH, '//*[@id="kw"]')
ele.send_keys("python")
# 点击搜索
driver.find_element(By.XPATH, '//*[@id="su"]').click()
# 退出
# driver.quit()
