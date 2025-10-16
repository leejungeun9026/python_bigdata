import requests
from bs4 import BeautifulSoup
import pymysql

# DB연결 설정
dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "leejungeun"
dbPass = "1234"

# DB연결
con = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, password=dbPass, database="pythondb", charset="utf8")

# cursor객체 생성
cur = con.cursor()

# 쿼리작성
insert_sql="insert into weather_table(loc, temp, humi) values(%s, %s, %s)"

req = requests.get('https://www.weather.go.kr/w/observation/land/city-obs.do')
soup = BeautifulSoup(req.text, 'html.parser')

# 정적 크롤링 (지역, 현재 기온, 습도)
table_tr = soup.select("#weather_table > tbody > tr")
for i in table_tr :
  loc = i.select_one('th > a').text
  temp = float(i.select_one('td:nth-child(6)').text)
  humi = int(i.select_one('td:nth-child(11)').text)

  # 커서를 통해 SQL insert 명령어를 실행
  cur.execute(insert_sql, (loc, temp, humi))
print("저장완료")

# DB 커밋 및 닫기
con.commit()
con.close()