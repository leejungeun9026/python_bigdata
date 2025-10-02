import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.weather.go.kr/w/observation/land/city-obs.do'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

trs = soup.select('#weather_table > tbody > tr')
weather = []
for i in trs :
  loc = i.select_one('th > a').text
  temp = i.select_one('td:nth-child(6)').text
  hum = i.select_one('td:nth-child(10)').text
  weather.append([loc, temp, hum])

weather_tbl = pd.DataFrame(weather, columns=('지역', '기온', '습도'))
weather_tbl.to_csv('day04\\weather.csv', mode='w', encoding='utf-8-sig', index=False)