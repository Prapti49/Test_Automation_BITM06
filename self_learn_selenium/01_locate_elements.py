from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")

print("Title is:", driver.title)


# different ways to locate

# driver.find_element("name", "q")
# driver.find_element("id", "search-box")
# driver.find_element("xpath", "//input[@name='q']")
# driver.find_element("css selector", "input[name='q']")

# Interact with Elements
search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium with Python")
search_box.submit()

# Implicit wait:
driver.implicitly_wait(5)

driver.quit()
# driver.close()