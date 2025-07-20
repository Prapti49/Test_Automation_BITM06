from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()


# driver.close()
# driver.quit()