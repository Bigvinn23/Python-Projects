from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# start a webdriver session
driver = webdriver.Chrome()

url = "https://www.selenium.dev/selenium/web/web-form.html"
driver.get(url)

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")

time.sleep(1)

submit_button.click()

time.sleep(3)

driver.quit()