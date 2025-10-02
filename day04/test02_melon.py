import requests
from bs4 import BeautifulSoup
import pandas as pd

## 크롬 사용자인걸 알려주기
header = {'User-agent' : 'Mozilla/5.0'}
req = requests.get('https://www.melon.com/chart/index.htm', headers = header)
soup = BeautifulSoup(req.text, 'html.parser')

table_tr = soup.select('#frm > div > table > tbody > tr')

chart = []
for li in table_tr :
  rank = li.select_one('td:nth-child(2) > div > span.rank').text
  title = li.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
  singers = li.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
  singer_lst = []
  for singer in singers :
    singer_lst.append(singer.text)
  album = li.select_one('td:nth-child(7) > div > div > div > a').text
  chart.append([rank, title, singer_lst, album])
print(chart)

# pandas로 파일 내보내기
melon_chart_tbl = pd.DataFrame(chart, columns = ('순위', '제목', '가수', '앨범'))
melon_chart_tbl.to_csv('day04\\melon_chart_tbl.csv', encoding='utf-8-sig', mode='w', index=False)