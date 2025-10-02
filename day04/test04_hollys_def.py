import requests
from bs4 import BeautifulSoup
import pandas as pd


def hollys_store(result) :
  for page in range(1, 6) :
    url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store='
    url2 = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' %page
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    tr = soup.select('div.tableType01 > table > tbody > tr')
    for i in tr :
      loc = i.select_one('td:nth-child(1)').text
      name = i.select_one('td:nth-child(2) > a').text
      addr = i.select_one('td:nth-child(4) > a').text
      tel = i.select_one('td:nth-child(6)').text
      result.append([loc, name, addr, tel])
  return

result = []
hollys_store(result)
hollys_df = pd.DataFrame(result, columns=('지역', '매장', '주소', '전화번호'))
print(hollys_df)
hollys_df.to_csv('day04\\hollys_page.csv', mode='w', encoding='utf-8-sig', index=False)
