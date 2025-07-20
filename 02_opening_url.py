import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
driver.get("https://google.com")
time.sleep(3)
driver.get("https://apple.com")
time.sleep(3)

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()
# driver.close()
driver.quit()