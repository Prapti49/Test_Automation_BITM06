import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)


driver.get("https://www.epassport.gov.bd/onboarding")

try:
    bangladeshi_no = driver.find_element(By.CSS_SELECTOR, "label[for='applying-bangladeshCommon.Labels.No']")
    bangladeshi_no.click()
except Exception as e:
    print("Element 'No' not found with implicit wait.")
bangladeshi_yes = driver.find_element(By.CSS_SELECTOR, "label[for='applying-bangladeshCommon.Labels.Yes']")
bangladeshi_yes.click()