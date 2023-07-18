from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.edge.options import Options

from bs4 import BeautifulSoup

import json


options = Options()
options.add_argument("--headless")
options.add_argument("disable-gpu")

driver = webdriver.Edge(options=options)
driver.implicitly_wait(10) # seconds

driver.get("https://stardewvalleywiki.com/Stardew_Valley_Wiki")

page_html = driver.page_source

soup = BeautifulSoup(page_html, 'html.parser')

print(soup.prettify())

imgs = soup.find_all('img')
srcs = [("https://stardewvalleywiki.com" + str(img.get('src'))) for img in imgs]

src_json = json.dumps(srcs)

with open ('imgs.json', "w") as outfile:
    outfile.write(src_json)

# time.sleep(10)

driver.quit()
