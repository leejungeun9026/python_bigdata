import requests
from bs4 import BeautifulSoup

url = 'http://finance.naver.com/'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

#container > div.aside > div > div.aside_area.aside_popular > table
table = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular > table.tbl_home')
table_tr = table.select('tbody > tr')

rst = []
for i in table_tr :
  name = i.select_one('th > a').text
  value = i.select_one('td:nth-child(2)').text
  updown = i.select_one('td:nth-child(3) > em > span').text
  change = i.select_one('td:nth-child(3) > span').text.strip()
  rst.append([name, value, updown, change])

print(rst)