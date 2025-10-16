from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd

# 순위, 제목, 별점, 누적관객수 -> naver_movie.csv

# 동적 크롤링
driver = wd.Chrome()
driver.implicitly_wait(2)
driver.get('https://m.entertain.naver.com/movie')
driver.find_element(By.CLASS_NAME, 'Home_button_tab__ku0ce').click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'Home_button_group_more__-kCiW').click()
time.sleep(3)

# 요소 가져오기
ol = driver.find_element(By.CLASS_NAME, "Home_section_ranking_list__nlebp")
lists = ol.find_elements(By.TAG_NAME, 'li')

movie_ranking = []
for li in lists :
  ranking_text = li.find_element(By.CLASS_NAME, 'Home_rank__-0JsA')
  ranking_text = ranking_text.find_element(By.CLASS_NAME, 'blind').text
  ranking = int(re.sub(r'[^0-9]', '', ranking_text))  
  title = li.find_element(By.CLASS_NAME, 'Home_title__p5PQs').text
  stars = float(li.find_element(By.CLASS_NAME, 'Home_number__0A85v').text)
  views_text = li.find_element(By.CLASS_NAME, 'Home_count__R\+hm8').text
  match = re.search(r'(\d+(?:\.\d+)?)', views_text)
  if match:
    num = float(match.group(1))
    if '만' in views_text:
        num *= 10000
    views = int(num)
  movie_ranking.append([ranking, title, stars, views])

tbl_movie = pd.DataFrame(movie_ranking, columns=('순위', '제목', '별점', '누적관객수'))
tbl_movie.to_csv('day06\\naver_movie.csv', mode='w', encoding='utf-8-sig', index=False)
