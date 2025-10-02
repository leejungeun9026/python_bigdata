import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd

driver = wd.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/index.htm')
time.sleep(5)

# //*[@id="frm"]/div/table/tbody
tbody = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')
#lst50 > td:nth-child(7) > div > div > div
datas = []
for tr in trs:
  rank = tr.find_element(By.CLASS_NAME, 'rank').text
  title = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank01').find_element(By.TAG_NAME, 'a').text
  singer = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank02').find_element(By.TAG_NAME, 'a').text
  album = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank03').find_element(By.TAG_NAME, 'a').text
  like = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(8) > div > button > span.cnt').text
  datas.append([rank, title, singer, album, like])
print(datas)

chart100 = pd.DataFrame(datas, columns=('순위', '제목', '가수', '앨범', '좋아요'))
chart100.to_csv('day05\\melon_chart100.csv', mode='w', encoding='utf-8-sig', index=False)