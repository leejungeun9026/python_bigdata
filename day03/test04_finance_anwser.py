import requests
from bs4 import BeautifulSoup

code = [252670, 251340]
lst = []
for i in code :
  url = 'https://finance.naver.com/item/main.naver?code=' + str(i)
  req = requests.get(url)
  soup = BeautifulSoup(req.text,'html.parser')

  kodex = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').text
  today = soup.select_one('div > p.no_today > .no_up > .blind').text
  lst.append([kodex, today])
print(lst)

