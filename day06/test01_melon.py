# day06//melon.csv '순위', '제목', '가수', '앨범', '좋아요'

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = wd.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/index.htm')
time.sleep(3)

tbody = driver.find_element(By.CSS_SELECTOR, '#frm > div > table > tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

chart = []
for tr in trs :
  rank = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > div > span.rank').text
  title = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
  singer_group = tr.find_elements(By.CSS_SELECTOR, 'td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
  singers = []
  for s in singer_group :
    singers.append(s.text)
  singer_str = '/'.join(singers)
  album = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(7) > div > div > div > a').text
  like = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(8) > div > button > span.cnt').text.replace(',','').replace('"','').strip()
  chart.append([rank, title, singer_str, album, like])
print(chart)

tbl_chart = pd.DataFrame(chart, columns=('순위', '제목', '가수', '앨범', '좋아요'))
tbl_chart.to_csv('day06\\melon.csv', mode='w', encoding='utf-8-sig', index=False)