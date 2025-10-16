# 터미널에 명령어 실행하여 설치 > pip install pymysql
import pymysql
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import re

# DB연결 설정
dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "leejungeun"
dbPass = "1234"

# DB연결
con = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, password=dbPass, database="pythondb", charset="utf8")

# cursor객체 생성
cur = con.cursor()

# 쿼리 작성
insert_sql="insert into melon_table(`rank`, `title`, `singer`, `album`, `likes`) " \
"values(%s, %s, %s, %s, %s)"

# 크롤링
driver = wd.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/index.htm')
time.sleep(3)

tbody = driver.find_element(By.CSS_SELECTOR, '#frm > div > table > tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

chart = []
for tr in trs :
  ranks = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > div > span.rank').text
  ranks = int(ranks)
  title = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
  singer_group = tr.find_elements(By.CSS_SELECTOR, 'td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
  singers = []
  for s in singer_group :
    singers.append(s.text)
  singer_str = '/'.join(singers)
  album = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(7) > div > div > div > a').text
  likes = tr.find_element(By.CSS_SELECTOR, 'td:nth-child(8) > div > button > span.cnt').text
  # like 정규화 11,203 -> 11203
  likes = int(re.sub(',','',likes))

  # 커서를 통해 SQL insert 명령어를 실행
  cur.execute(insert_sql, (ranks, title, singer_str, album, likes))
print("저장완료")

# DB 커밋 및 닫기
con.commit()
con.close()

