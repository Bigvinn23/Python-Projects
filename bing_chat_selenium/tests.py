from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.implicitly_wait(10) # seconds
driver.get("https://www.bing.com/chat")

input_shadow_root_1 = driver.find_element(By.CSS_SELECTOR, "#b_sydConvCont>cib-serp").shadow_root
input_shadow_root_2 = input_shadow_root_1.find_element(By.CSS_SELECTOR, "#cib-action-bar-main").shadow_root
input_shadow_root_3 = input_shadow_root_2.find_element(By.CSS_SELECTOR, "cib-text-input").shadow_root

input_box = input_shadow_root_3.find_element(By.ID, 'searchbox')

# input_box.send_keys('Hello')
# input_box.send_keys(Keys.RETURN)

# time.sleep(15)

input_box.send_keys('tell me a joke')
input_box.send_keys(Keys.RETURN)

time.sleep(30)

driver.quit()
