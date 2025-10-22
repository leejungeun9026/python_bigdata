from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date, timedelta
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

# 동적크롤링/파일내보내기/DB저장/그래프
# 내일 부산 출발 -> 제주 도착하는 편도 비행기 검색하기
dep_city = '부산'
arr_city = '제주'

tomorrow = date.today() + timedelta(days=1)
year = tomorrow.year
month = tomorrow.month
day = tomorrow.day
str_year_month = str(year) + "." + str(month) + "."


# 세션 시작
driver = webdriver.Chrome()
driver.get('https://flight.naver.com/')
time.sleep(10)



# 팝업 유무 확인
try:
    btn_popup_close = driver.find_element(By.CLASS_NAME, 'FullscreenPopup_close')
    btn_popup_close.click()
    print("팝업 닫음")
except Exception:
    print("팝업 없음")
time.sleep(5)



# 편도 선택
driver.find_element(By.XPATH, '//button[@data-testid="tab-OW"]').click()
time.sleep(0.5)

# 출발지 선택
driver.find_element(By.XPATH, '//button[@data-testid="select-departure-city"]').click()
time.sleep(3)
driver.find_element(By.XPATH, "//ul/li/button[contains(normalize-space(.), '"+dep_city+"')]").click()
time.sleep(1)

# 도착지 선택
driver.find_element(By.XPATH, '//button[@data-testid="select-arrival-city"]').click()
time.sleep(3)
driver.find_element(By.XPATH, "//ul/li/button[contains(normalize-space(.), '"+arr_city+"')]").click()
time.sleep(1)

# 가는 날 선택
driver.find_element(By.XPATH, '//button[@data-event-area-code="one.depdate1"]').click()
time.sleep(3)

# 달력에서 내일 날짜 찾기
# 전체 달력
calendar_wrap = driver.find_element(By.XPATH, '//*[@data-event-area-code="cal.calendar"]')
# yyyy.mm 찾기
find_month = calendar_wrap.find_elements(By.XPATH, ".//div[text()='"+str_year_month+"']")
# 달력 테이블 찾기
find_table = calendar_wrap.find_element(By.XPATH, ".//div[text()='" + str_year_month + "']/following-sibling::table")
# 날짜 찾기
find_day = find_table.find_element(By.XPATH, ".//*[text()='"+ str(day) +"']")
find_day.click()
time.sleep(1)
# 검색
driver.find_element(By.XPATH, '//*[@data-event-area-code="one.search"]').click()
time.sleep(5)



# 스크롤하기
previous_scroll_height = driver.execute_script("return document.body.scrollHeight")
scroll_pause_time = 2
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(scroll_pause_time)
    current_scroll_height = driver.execute_script("return document.body.scrollHeight")
    if current_scroll_height == previous_scroll_height:
        break    
    previous_scroll_height = current_scroll_height

flight_list = driver.find_elements(By.XPATH, "//*[contains(@class, 'domestic_Flight')]")



# 데이터 저장
datas = []
for li in flight_list :
  airline = li.find_element(By.XPATH,".//*[contains(@class, 'airline_name')]").text

  route_time = li.find_element(By.XPATH,".//*[contains(@class, 'route_Route')]")
  times = route_time.find_elements(By.XPATH, ".//*[contains(@class, 'route_time')]")
  start_time = times[0].text
  end_time = times[1].text

  seat_type = li.find_element(By.XPATH, ".//*[contains(@class, 'domestic_type')]").text
  price = li.find_element(By.XPATH, ".//*[contains(@class, 'domestic_num')]").text
  price = int(price.replace(",", ""))
  datas.append([airline, start_time, end_time, seat_type, price])



# 파일 내보내기
df = pd.DataFrame(datas, columns=('항공사', '출발시간', '도착시간', '좌석타입', '가격'))
df.to_csv('day08\\from_%s_to_%s_%s_filght.csv' %(dep_city, arr_city, tomorrow), mode='w', encoding='utf-8-sig', index=False)



# DB연결
con = pymysql.connect(host="127.0.0.1", 
                      user="leejungeun", 
                      password="1234", 
                      database="pythondb", 
                      charset="utf8")

# 테이블 드롭 및 생성
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

# DB insert
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
