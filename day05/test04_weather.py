import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.weather.go.kr/w/observation/land/city-obs.do'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

# 지역, 현재 기온, 습도
table_tr = soup.select("#weather_table > tbody > tr")
datas = []
for i in table_tr :
  loc = i.select_one('th > a').text
  temp = i.select_one('td:nth-child(6)').text
  humi = i.select_one('td:nth-child(11)').text
  datas.append([loc, temp, humi])
print(datas)

weather_tbl = pd.DataFrame(datas, columns=('지역', '현재 기온', '습도'))
weather_tbl.to_csv('day05\\weather_1002.csv', mode='w', encoding='utf-8-sig', index=False)