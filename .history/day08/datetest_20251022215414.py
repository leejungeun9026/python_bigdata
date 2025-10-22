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


# 그래프 그리기
x = []
for i in files :
  a = int(int(i[4])/10000)


df = pd.read_csv(f'day08/{file_name}.csv', header=1)
print(df)
