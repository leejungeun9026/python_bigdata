from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas
import matplotlib.pyplot as plt
import matplotlib as mpl
import pymysql

# 제주도 > 호텔 검색
# 호텔이름, 별점, 가격
# 1. 파일 내보내기 hanatour.csv
# 2. 별점 그래프
# 3. db에 테이블 추가하기
# 4. 테이블에서 별점가져온 뒤 별점별 파이그래프

url = 'https://www.hanatour.com/mma/smn/EX00000020'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

# 검색
driver.find_element(By.CLASS_NAME, 'input_keyword').send_keys('제주도')
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'btn_search').click()
time.sleep(5)

# 호텔 탭 이동
tab_ul = driver.find_element(By.CSS_SELECTOR, '#contents > div.js_tabs > ul')
tab_li_hotel = tab_ul.find_element(By.XPATH, ".//li//*[normalize-space(text())='호텔']")
time.sleep(2)
tab_li_hotel.click()
time.sleep(5)


# 리스트 가져오기
pro_lis = driver.find_elements(By.CSS_SELECTOR, '.prod_list > ul > li')

jeju_hotel = []
for li in pro_lis :
  # 호텔이름, 별점, 가격
  name = li.find_element(By.CSS_SELECTOR, 'div.txt_info > div.tit.eps2 > strong').text
  stars = float(li.find_element(By.CSS_SELECTOR, 'div.txt_info > div.rating > strong').text)
  price = li.find_element(By.CSS_SELECTOR, 'div.txt_info > div.price > div > div > strong').text
  price = int(re.sub(r'[^0-9]', '', price))
  jeju_hotel.append([name, stars, price])
driver.close()



# 1. 파일 내보내기 hanatour.csv
tbl_jejuhotel = pandas.DataFrame(jeju_hotel, columns=('이름', '별점', '가격') )
tbl_jejuhotel.to_csv('day07\\hanatour.csv', mode='w', encoding='utf-8-sig', index=False)



# 2. 별점 그래프
x = [i[0] for i in jeju_hotel]
y = [i[1] for i in jeju_hotel]

# 폰트 설정
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

plt.figure(figsize=(16, 8))
plt.bar(x,y)
plt.xlabel('호텔 이름')
plt.ylabel('별점')
plt.title('제주호텔 별점 그래프')
plt.xticks(rotation=45)
plt.show()



# 3. db에 테이블 추가하기
con = pymysql.connect(host='127.0.0.1', 
                      user='leejungeun', 
                      password='1234', 
                      database='pythondb', 
                      charset='utf8')

cur = con.cursor()

# 테이블 생성
cur.execute('drop table if exists hanatour_table')
cur.execute('''
  CREATE TABLE hanatour_table (
    name VARCHAR(100) NOT NULL,
    stars FLOAT NOT NULL,
    price INT NOT NULL,
    PRIMARY KEY (name)
  )
''')

# 파일 가져오기
with open('day07\\hanatour.csv', 'r', encoding='utf-8-sig') as inFp:
  datas = []
  next(inFp)  # 첫 번째 줄(헤더) 건너뛰기
  for data in inFp :
    row = data.strip()
    row_list = row.split(',')
    datas.append(row_list)

# DB insert
insert_sql = 'insert into hanatour_table(name, stars, price) values(%s, %s, %s)'
for row in datas :
  name = row[0]
  stars = row[1]
  price = row[2]
  result = cur.execute(insert_sql, (name, stars, price))
con.commit()




# 4. 테이블에서 별점 select, 별점 파이그래프 그리기
sql = 'select floor(stars), count(*) ' \
      'from pythondb.hanatour_table ' \
      'group by floor(stars)'

cur.execute(sql)
result = cur.fetchall()
con.close()

# 파이 그래프
x = [i[0] for i in result]
y = [i[1] for i in result]

# 폰트 설정
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

plt.pie(y, labels=x, autopct='%.1f%%')
plt.title('점수대별 호텔 비율', fontsize=14)
plt.show()