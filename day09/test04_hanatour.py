from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas
import matplotlib.pyplot as plt
import matplotlib as mpl
import pymysql


# 동적 크롤링으로 하나투어 사이트에 접속하여 (https://www.hanatour.com/)데이터를 수집
# 1. 제주도 검색 -> 호텔 탭을 클릭하여 정보 수집하기
# 2. 호텔명, 별점, 가격을 수집하여 mysql 데이터베이스에 테이블을 명령어를 사용하여 생성 및 저장(테이블 명 : hanaHotel)
# 3. 저장한 테이블에서 별점 정보를 추출하여 matplotlib 를 이용하여 막대그래프와 파이 그래프 그리기


# 세션 시작
driver = webdriver.Chrome()
driver.get("https://www.hanatour.com/")
time.sleep(3)


# 검색
driver.find_element(By.CSS_SELECTOR, 'input#input_keyword').send_keys("제주도")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.btn_search').click()
time.sleep(3)

# 호텔 탭 찾기
tab = driver.find_element(By.CSS_SELECTOR, 'ul.tabs')
tab.find_element(By.XPATH, './/li/a[contains(normalize-space(.), "호텔")]').click()
time.sleep(5)

# 호텔 요소 찾기
hotel_list = driver.find_elements(By.CSS_SELECTOR, 'div.prod_list > ul > li')

# 호텔 정보 배열객체에 담기
datas = []
for li in hotel_list :
  name = li.find_element(By.CSS_SELECTOR, 'div.tit > strong').text
  rating = float(li.find_element(By.CSS_SELECTOR, 'div.rating > strong').text)
  price = li.find_element(By.CSS_SELECTOR, 'div.price strong').text
  price = int(price.replace(',',''))
  datas.append([name, rating, price])



# DB연결
con = pymysql.connect(host='127.0.0.1', 
                      user='leejungeun', 
                      password='1234', 
                      database='pythondb', 
                      charset='utf8')

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS hanaHOTEL")
cur.execute("CREATE TABLE hanaHOTEL (" \
              "NAME VARCHAR(45), " \
              "RATING FLOAT, " \
              "PRICE INT)")

sql_insert = "INSERT INTO hanaHOTEL(NAME, RATING, PRICE) " \
             "VALUES(%s,%s, %s)"

for row in datas :
  cur.execute(sql_insert, (row[0], row[1], row[2]))
con.commit()





# 그래프
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

sql_select = "select floor(stars), count(*) from hanatour_table group by floor(stars)"
cur.execute(sql_select)
result = cur.fetchall()
x = [str(int(i[0]))+' 점대' for i in result]
y = [int(i[1]) for i in result]
print(x, y)

plt.bar(x, y, color='gold', width=0.5)
plt.title('제주도 호텔 별점 분포')
plt.xlabel('별점')
plt.ylabel('개수')
plt.show()

plt.pie(y, labels=x, autopct="%.1f%%")
plt.show()