from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("python")
driver.find_element(By.XPATH, '//*[@id="su"]').click()

driver.quit()
