import requests
from bs4 import BeautifulSoup

url = 'https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
ul = soup.select('.b-newbook')[0]
li = ul.select('li')

result = []
for i in li :
  title = i.select_one('div.b-text > h4 > a').text
  author = i.select_one('div.b-text > div.b-author').text
  price = i.select_one('div.b-text > div.b-price > strong').text
  result.append([title, author, price])

print(result)