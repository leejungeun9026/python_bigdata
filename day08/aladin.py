
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time

driver = wd.Chrome()
time.sleep(1) #web드라이버에서 기다리는 코드 - 로딩시간
driver.get('https://www.aladin.co.kr/home/welcome.aspx')
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'inputbox_new').send_keys('세븐틴')
driver.find_element(By.CSS_SELECTOR, '#global_search > button').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#keyword_wrap > div.search_result_nav > ul > li:nth-child(9) > a').click()

search = driver.find_element(By.CSS_SELECTOR, "#Search3_Result")
boxs = search.find_elements(By.CLASS_NAME,'ss_book_box')

for box in boxs :
  ul = box.find_element(By.CSS_SELECTOR, 'table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul')
  title = ul.find_element(By.CLASS_NAME, 'bo3')
  
  print(title.text)
