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

# DB저장
con = pymysql.connect(host="127.0.0.1", 
                      user="leejungeun", 
                      password="1234", 
                      database="pythondb", 
                      charset="utf8")


table_name = f'{dep_city}_{arr_city}_{tomorrow}'
print(table_name)
sql_drop = f"DROP TABLE IF EXISTS `{table_name}`"
sql_create = f"""CREATE TABLE `{table_name}` (
                  airline VARCHAR(45),
                  start_time VARCHAR(45),
                  end_time VARCHAR(45),
                  seat_type VARCHAR(45),
                  price INT)"""

cur = con.cursor()
cur.execute(sql_drop)
cur.execute(sql_create)

sql_insert = f"""INSERT INTO 
                `{table_name}`(airline, start_time, end_time, seat_type, price) 
                value(%s, %s, %s, %s, %s)"""

# 파일 가져오기
with open(f'day08\\from_부산_to_제주_2025-10-23_filght.csv', 'r', encoding='utf-8-sig') as inFp:
  files = []
  next(inFp)  # 첫 번째 줄(헤더) 건너뛰기
  for data in inFp :
    row = data.strip()
    row_list = row.split(',')
    files.append(row_list)

for data in files :
  cur.execute(sql_insert, (data[0], data[1], data[2], data[3], data[4]))
con.commit()



# 그래프 그리기
x = [i[0] for i in files]
y = [i[4] for i in files]

# 막대그래프
plt.bar(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
