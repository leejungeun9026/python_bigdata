import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.hollys.co.kr/store/korea/korStore2.do'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

#contents > div.content > fieldset > fieldset > div.tableType01 > table

tr = soup.select('div.tableType01 > table > tbody > tr')
stores = []
for i in tr :
  loc = i.select_one('td:nth-child(1)').text
  name = i.select_one('td:nth-child(2) > a').text
  addr = i.select_one('td:nth-child(4) > a').text
  tel = i.select_one('td:nth-child(6)').text
  stores.append([loc, name, addr, tel])
print(stores)

stores_tbl = pd.DataFrame(stores, columns=('지역', '매장명', '주소', '전화번호'))
stores_tbl.to_csv('day04\\hollys_stores.csv', mode='w', encoding='utf-8-sig', index=False)