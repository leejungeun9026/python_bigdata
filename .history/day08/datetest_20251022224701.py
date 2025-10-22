from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date, timedelta
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

dep_city = '부산'
arr_city = '제주'

tomorrow = date.today() + timedelta(days=1)
year = tomorrow.year
month = tomorrow.month
day = tomorrow.day
str_year_month = str(year) + "." + str(month) + "."

file_name = f'busan_to_jeju_{tomorrow}'

# DB연결
con = pymysql.connect(host="127.0.0.1",
                      user="leejungeun",
                      password="1234",
                      database="pythondb",
                      charset="utf8")

# 테이블 드롭 및 생성
sql_drop = f"DROP TABLE IF EXISTS `{file_name}`"
sql_create = f"""CREATE TABLE `{file_name}` (
                  airline VARCHAR(45),
                  start_time VARCHAR(45),
                  end_time VARCHAR(45),
                  seat_type VARCHAR(45),
                  price INT)"""

cur = con.cursor()
cur.execute(sql_drop)
cur.execute(sql_create)

sql_insert = f"""INSERT INTO
                `{file_name}`(airline, start_time, end_time, seat_type, price)
                value(%s, %s, %s, %s, %s)"""

# 파일 가져오기
with open(f'day08/{file_name}.csv', 'r', encoding='utf-8-sig') as inFp:
  files = []
  next(inFp)  # 첫 번째 줄(헤더) 건너뛰기
  for data in inFp :
    row = data.strip()
    row_list = row.split(',')
    files.append(row_list)

# DB insert
for data in files :
  cur.execute(sql_insert, (data[0], data[1], data[2], data[3], data[4]))
con.commit()


##### bar 차트 #####
# DB에서 가격대별 갯수 가져오기
sql_select = f"""
SELECT
	CASE
		WHEN PRICE > 100000 THEN '10만원 이상'
        WHEN PRICE BETWEEN 90000 AND 100000 THEN '9만원대'
        WHEN PRICE BETWEEN 80000 AND 90000 THEN '8만원대'
        WHEN PRICE BETWEEN 70000 AND 80000 THEN '7만원대'
        WHEN PRICE BETWEEN 60000 AND 70000 THEN '6만원대'
        WHEN PRICE BETWEEN 50000 AND 60000 THEN '5만원대'
        WHEN PRICE BETWEEN 40000 AND 50000 THEN '4만원대'
        WHEN PRICE BETWEEN 30000 AND 40000 THEN '3만원대'
        WHEN PRICE BETWEEN 20000 AND 30000 THEN '2만원대'
        WHEN PRICE BETWEEN 10000 AND 20000 THEN '1만원대'
        ELSE '1만원 이하'
	END AS PRICERANGE,
  COUNT(*)
FROM `{file_name}`
GROUP BY PRICERANGE"""
cur.execute(sql_select)
result = cur.fetchall()

# DataFrame으로 만들어서 배열에 담기
df_result = pd.DataFrame(result, columns=('price', 'count'))
x = df_result['price'].tolist()
y = df_result['count'].tolist()

# 폰트 설정
# font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
font_name = mpl.font_manager.FontProperties(fname='/System/Library/Fonts/AppleSDGothicNeo.ttc').get_name()
mpl.rc('font', family=font_name)

# 차트 생성
plt.bar(x, y)
plt.title(f'{file_name} 가격대별 항공권 개수')
plt.xlabel('가격')
plt.xticks(rotation=45)
plt.ylabel('항공권 수')
plt.show()




##### 파이차트 #####
# 전체 DB 가져와서 DataFrame에 담기
sql_select = f" SELECT * FROM `{file_name}`"
cur.execute(sql_select)
result = cur.fetchall()
df_result = pd.DataFrame(result, columns=('airline', 'start_time', 'end_time', 'seat_type', 'price'))

# airline 개수 구하고 배열에 담기
value_counts = df_result['airline'].value_counts()
x = value_counts.index.tolist()
y = value_counts.tolist()

# 차트 생성
plt.pie(y, labels=x, autopct='%.1f%%')
plt.title(f'{file_name} 항공사별 항공권 비율')
plt.show()