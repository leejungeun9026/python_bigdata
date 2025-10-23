from selenium import webdriver as wd
from selenium.webdriver.common.by import By  # 셀레니움 문법사용
from selenium.webdriver.common.keys import Keys
import time
import re

import matplotlib as mpl
import matplotlib.pyplot as plt

# 인터파크 투어 - 제주도 검색 - 제주도 호텔 정보 출력

driver = wd.Chrome()
driver.get('https://www.hanatour.com/mma/smn/EX00000020')

# 검색창 id = 'txtHeaderInput'에 제주도 값 입력
driver.find_element(By.ID, 'input_keyword').send_keys('제주도')
# 검색버튼 id = 'btnHeaderInput'을 클릭
driver.find_element(By.CSS_SELECTOR, '.btn_search').click()
# 호텔 정보만 볼수 있게 호텔이란 글자의 a태그 클릭
driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/ul/li[3]/a').click()

time.sleep(2)

hotels = driver.find_elements(By.CLASS_NAME, 'txt_info')
# print(hotels)

time.sleep(2)

# 호텔명, 성급, 금액, 별점
datas = []
for res in hotels:
    hName = res.find_element(By.CSS_SELECTOR, '.tit').text
    price = res.find_element(By.CSS_SELECTOR, '.price').text
    price = re.sub('\n','',price)
    star = res.find_element(By.CSS_SELECTOR, 'div.rating > strong').text
    
    datas.append([hName, price, star])
print(datas)
