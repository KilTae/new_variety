from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import warnings

title = []

browser = webdriver.Safari()
url = f"https://www.coupang.com/np/categories/194282?listSize=120&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=194182&rating=0"
browser.get(url)
button_n = 1
body = browser.find_element(By.CSS_SELECTOR, 'body')
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)

while(button_n < 10):
    items = browser.find_elements(By.CLASS_NAME, "name")
    print(len(items))

    for item in items:
        title.append(item.text)
        print(item.text)


    button_n += 1
    url = 'https://www.coupang.com/np/categories/194282?listSize=120&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=194182&rating=0&page='.format(button_n)
    browser.get(url)
    time.sleep(3)



data = {'title' : title}
df = pd.DataFrame(data)
print(df)
df.to_csv('copang.csv', encoding = 'utf-8-sig')
time.sleep(10)
browser.close()