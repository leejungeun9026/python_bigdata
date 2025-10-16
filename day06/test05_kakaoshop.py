from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd
import pymysql

# DB연결
con = pymysql.connect(host="127.0.0.1", 
                      user="leejungeun", 
                      password="1234", 
                      database="pythondb", 
                      charset="utf8")
cur = con.cursor()

# 커서를 통해 쿼리 실행
# 기존 테이블 드롭
cur.execute('drop table if exists kakaoshop')
# 테이블 생성
cur.execute('create table kakaoshop(ranking int, shop varchar(45), product varchar(255), price int)') 

# 쿼리
insert_sql = "insert into kakaoshop(ranking, shop, product, price) values(%s, %s, %s, %s)"

# 동적 크롤링
driver = wd.Chrome()
driver.implicitly_wait(2)
driver.get('https://store.kakao.com/home/best?tab=contProduct&groupId=all&period=HOURLY')
time.sleep(3)

# 스크롤하기
# 현재 페이지의 전체스크롤
pre_height = driver.execute_script("return document.body.scrollHeight")

interval = 2
while True :
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  time.sleep(interval)
  # 현재 스크롤 높이
  curr_height = driver.execute_script("return document.body.scrollHeight")
  if curr_height == pre_height :
    break
  pre_height = curr_height

# 요소 가져오기
ul = driver.find_element(By.CSS_SELECTOR, '.list_productcmp')
list = ul.find_elements(By.CSS_SELECTOR, 'li.ng-star-inserted:not(.item_etc)')
for li in list :
  ranking = li.find_element(By.CLASS_NAME, 'badge_rank').text
  store_name = li.find_element(By.CLASS_NAME, 'tit_store').text
  product_name = li.find_element(By.CLASS_NAME, 'name_product').text
  price = li.find_element(By.CSS_SELECTOR, '.txt_price > .emph_price').text
  price = re.sub(r'[^0-9]', '', price)

  # DB insert
  cur.execute(insert_sql, (ranking, store_name, product_name, price))
print("저장완료")


# DB 커밋 및 닫기
con.commit()
con.close()