import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.weather.go.kr/w/observation/land/city-obs.do'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

trs = soup.select('#weather_table > tbody > tr')
weather = []
for tr in trs :
  th = tr.select_one('th').text
  tds = tr.select('td')
  weather.append([th, tds[4].text, tds[-4].text])

weather_tbl = pd.DataFrame(weather, columns=('지역', '기온', '습도'))
weather_tbl.to_csv('day04\\weather2.csv', mode='w', encoding='utf-8-sig', index=False)