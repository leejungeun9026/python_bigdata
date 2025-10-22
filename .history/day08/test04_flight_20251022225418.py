from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date, timedelta
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

##### 1. 크롤링 / 2. 파일내보내기 / 3. DB저장 / 4. 그래프 #####
##### 내일 기준 부산 출발 -> 제주 도착하는 편도 비행기 검색하기 #####

# 변수 초기화
dep_city = '부산'
arr_city = '제주'

tomorrow = date.today() + timedelta(days=1)
year = tomorrow.year
month = tomorrow.month
day = tomorrow.day
str_year_month = str(year) + "." + str(month) + "."

file_name = f'busan_to_jeju_{tomorrow}'





##### 1. 크롤링 #####
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





##### 2. 파일내보내기 #####
df = pd.DataFrame(datas, columns=('항공사', '출발시간', '도착시간', '좌석타입', '가격'))
df.to_csv(f'day08/{file_name}.csv', mode='w', encoding='utf-8-sig', index=False)





##### 3. DB저장 #####
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

# insert SQL
sql_insert = f"""INSERT INTO
                `{file_name}`(airline, start_time, end_time, seat_type, price)
                value(%s, %s, %s, %s, %s)"""

# DB insert
for data in datas :
  cur.execute(sql_insert, (data[0], data[1], data[2], data[3], data[4]))
con.commit()





##### 4. 그래프 #####
# 1) bar차트
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




# 2) 파이차트
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