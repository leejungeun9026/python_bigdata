import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd

url= 'https://smartplace.naver.com/bizes/place/9967126?bookingBusinessId=1192929'

driver = wd.Chrome()
driver.implicitly_wait(2)
driver.get(url)
time.sleep(2)

driver.find_element(By.CLASS_NAME, 'Modal_btn_confirm__JBzc2').click()
time.sleep(5)

driver.find_element(By.CLASS_NAME, 'input_id').send_keys('2_jungeun')
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'input_pw').send_keys('@rmwlfk26')
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'btn_login').click()
time.sleep(10)